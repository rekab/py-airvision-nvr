py-airvision-nvr
================

Python script to receive updates from an AirVision NVR (v2.0.0)

## Pre-reqs
* AirVision v2
 * Tested with 1 camera set to record on motion.
* websocket-client, available at https://github.com/liris/websocket-client
* Tested with Python 2.7.3

## Usage

```
python motion.py --server=https://airvision-nvr:7443 \
                 --user=airvision@example.org \
                 --password=hunter2 \
                 --command='/usr/bin/espeak "motion detected in %(zones)s at %(time)s"'
```

## Version

Still messy. Hacked up one Saturday afternoon that I hope someone finds useful.
