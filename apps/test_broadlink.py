import broadlink
from my_credits import (
    WIFI_SSID,
    WIFI_PASSWORD,
    WIFI_SECIRITY_MODE,
)
from commands import (
    SAMSUNG_TV_POWER,
    SAMSUNG_TV_ADD_SOUND,
    SAMSUNG_TV_REDUCE_SOUND,
    SUMSUNG_TV_NEXT_CNANNEL,
    SUMSUNG_TV_PREVIOUS_CNANNEL,
)

broadlink.setup(WIFI_SSID, WIFI_PASSWORD, WIFI_SECIRITY_MODE)

try:
    device = broadlink.discover(timeout=5)[0]
    device.auth()
except IndexError:
    print("Broadlink is turned of")

import ipdb; ipdb.set_trace()