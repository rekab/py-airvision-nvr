import argparse
import airvision
import os
import time

def SetupFlags():
  parser = argparse.ArgumentParser(
      description='Connects to a v2.0.0 Airvision NVR and '
          'runs a command when motion is detected.')
  parser.add_argument('--server',
      help='NVR server URL (e.g. https://server:port/).',
      default='https://airvision-nvr:7443/', required=True)
  parser.add_argument('--user', help='NVR username/email address.',
      required=True)
  parser.add_argument('--password', help='NVR password.', required=True)
  parser.add_argument('--cooldown',
    help='Number of seconds to wait before running the command '
    'again for the same zone(s)', default=60)
  parser.add_argument('--command',
      help='Command to run. Can take python formatted strings '
          '%%(zone)s for the zone name and %%(time)s for the time',
      default='espeak "motion detected in %(zones)s at %(time)s"')
  return parser.parse_args()


class Cooldown(object):

  def __init__(self):
    self._times = {}

  def Update(self, key, duration):
    prev = self._times.get(key, 0)
    self._times[key] = time.time()
    return int(duration) <= (time.time() - prev)


def main():
  flags = SetupFlags()
  if not flags.server.endswith('/'):
    flags.server = flags.server + '/'

  server = airvision.Server(flags.server, flags.user, flags.password)
  conn = airvision.CreateAirvisionNVRConnection(server)
  conn.Subscribe(['camera', 'motion'])
  state = airvision.State()
  cooldown = Cooldown()
  while True:
    msg = conn.Read()
    print 'msg=%s' % msg
    state.UpdateFromServerMessage(msg)
    for motion_event in airvision.GetMotionEvents(state, msg):
      if cooldown.Update(motion_event.zones, flags.cooldown):
        command = flags.command % motion_event.__dict__
        print 'running command=%s' % command
        status = os.system(command)
        print 'command exited with %d' % status
      else:
        print 'cooldown still active for "%s"' % motion_event.zones


if __name__ == '__main__':
  main()
