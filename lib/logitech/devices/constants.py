#
#
#

DEVICE_STATUS = type('DEVICE_STATUS', (),
				dict(
					UNKNOWN=None,
					UNAVAILABLE=-1,
					CONNECTED=0,
					# ACTIVE=1,
				))


from collections import defaultdict

DEVICE_STATUS_NAME = defaultdict(lambda x: None)
DEVICE_STATUS_NAME[DEVICE_STATUS.UNAVAILABLE] = 'disconnected'
DEVICE_STATUS_NAME[DEVICE_STATUS.CONNECTED] = 'connected'
# DEVICE_STATUS_NAME[DEVICE_STATUS.ACTIVE] = 'active'

del defaultdict