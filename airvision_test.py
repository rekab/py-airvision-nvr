import airvision
import os
import pprint
import time
import unittest


os.environ['TZ'] = 'PST8PDT'
time.tzset()


SERVER_UPDATE = [{'action': 'update',
           'data': [{'_id': 'deadbeef',
                     'bitRate': 2048,
                     'brightness': 50,
                     'broadcastEnabled': False,
                     'channel0Available': False,
                     'channel1Available': True,
                     'channel2Available': False,
                     'contrast': 50,
                     'controllerId': 'deadbeef',
                     'cpuUsage': 84,
                     'denoise': 50,
                     'enableAutomaticUpdate': False,
                     'enableFullTimeRecord': False,
                     'enableMotionRecord': True,
                     'fovangle': 0.8203,
                     'fovradius': 151.98647,
                     'fovrotation': -0.20652,
                     'frameRate': 25,
                     'gamma': 0,
                     'host': '192.168.1.53',
                     'hue': 50,
                     'manufacturer': 'Ubiquiti Networks, Inc.',
                     'manufacturerUrl': 'http://www.ubnt.com',
                     'mapId': 'deadbeef',
                     'memoryUsage': 81,
                     'modelDescription': '',
                     'modelName': 'airCam',
                     'modelNumber': '',
                     'modelUrl': 'http://www.ubnt.com/video',
                     'name': 'front',
                     'ntpProbeStatus': 'ntp.sts.ok',
                     'ntpServer': None,
                     'nvrUuid': 'f00d',
                     'orientation': 0,
                     'postPaddingSecs': 1,
                     'prePaddingSecs': 2,
                     'provisioned': True,
                     'refreshRate': 60,
                     'rtspPort': 0,
                     'rxBytes': 33215,
                     'saturation': 50,
                     'schedule': None,
                     'sharpness': 50,
                     'sshPort': 22,
                     'state': 1,
                     'streamChannel': 1,
                     'streams': {'0': {'channel': 0,
                                       'height': 720,
                                       'port': 554,
                                       'proto': 'rtsp',
                                       'uri': '/live/ch00_0',
                                       'width': 1280},
                                 '1': {'channel': 1,
                                       'height': 368,
                                       'port': 554,
                                       'proto': 'rtsp',
                                       'uri': '/live/ch01_0',
                                       'width': 640}},
                     't': 'camera',
                     'timezone': None,
                     'txBytes': 139433,
                     'uptime': 1376410701,
                     'username': 'ubnt',
                     'uuid': 'feedbeef',
                     'verifiedNvrs': ['f00d'],
                     'version': {'build': '17961',
                                 'full': 'v1.2',
                                 'v': 'v1.2'},
                     'volume': 50,
                     'x': 0.19577815,
                     'y': 0.88990426,
                     'zones': [{'_id': 'deadbeef',
                                'coords': [{'x': 0.7580244122965641,
                                            'y': 0.0},
                                           {'x': 0.5721066907775768,
                                            'y': 0.2347266881028939},
                                           {'x': 0.2528254972875226,
                                            'y': 0.2845659163987138},
                                           {'x': 0.07368896925858952,
                                            'y': 0.22990353697749197},
                                           {'x': 0.002034358047016275,
                                            'y': 0.3062700964630225},
                                           {'x': 0.0018083182640144665,
                                            'y': 0.364951768488746},
                                           {'x': 0.22400542495479203,
                                            'y': 0.4071543408360129},
                                           {'x': 0.25361663652802896,
                                            'y': 0.6294212218649518},
                                           {'x': 0.21360759493670886,
                                            'y': 0.7584405144694534},
                                           {'x': 0.0,
                                            'y': 0.720056270096463},
                                           {'x': 0.0, 'y': 1.0},
                                           {'x': 1.0, 'y': 1.0},
                                           {'x': 1.0, 'y': 0.0}],
                                'isDefault': False,
                                'name': 'front',
                                'sensitivity': 5,
                                't': 'zone'}]}]}]


SERVER_ADD = [{'action': 'add',
           'data': [{'cameraUuid': 'feedbeef',
                     'isStart': True,
                     'motionData': 'AAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAGAAAAAAAAAAAABAAAAAAAAAAAAASQAAAAAAAAAAAEkAAAAAAAAAAABIAAAAAAAAAAAAyAAAAAAAAAAAAAgAAAAAAAAAAAAIEAAAAAAAAAMACBAAAAAAAAAAAAAQAAAIAAAAAAAAEAAAC/AAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAFCAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAACAAgAAAAAAAAAAwIIAAAAAAAAAB/8SAAAAAAAAAAz/8gAAAAAAAAAc99IAAAAAAAAAHAeSAAAAAAAAADgD0gAAAAAAAAAwB/QAAAAAAAAAMYAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAPAAAAAAAAAAAAD4QAAAAAAAAAAAfMAAAAAAAAAAAPnAAAAAAAAAAABwgAAAAAAAAAABgQAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                     't': 'motion',
                     'timestamp': 1376779754,
                     'zoneValues': {'deadbeef': 1},
                     'zones': ['deadbeef']}]}]

class WhateverTest(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testGetMotionEvents(self):
    conn = airvision.AirvisionNVRConnection(None, None)
    state = airvision.State()
    msg = conn._ExtractServerMessage(SERVER_UPDATE)
    state.UpdateFromServerMessage(msg)
    msg = conn._ExtractServerMessage(SERVER_ADD)
    events = airvision.GetMotionEvents(state, msg)
    self.assertEqual(len(events), 1)
    event = events[0]
    self.assertEqual(event.zones, 'front')
    self.assertEqual(event.time, ' 3 49 PM')

#  def testLoginAndWebsocket(self):
#    self.server = airvision.Server(SERVER_URL, SERVER_USER, SERVER_PASSWORD)
#    cookie = airvision.Login(self.server)
#    socket = airvision.Connect(self.server, cookie)
#    airvision.Subscribe(socket, cookie, ['camera', 'motion'])
#    print 'Got: %s' % socket.recv()


if __name__ == '__main__':
  unittest.main()
