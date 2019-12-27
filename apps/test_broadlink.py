import broadlink
from my_credits import (
    WIFI_SSID,
    WIFI_PASSWORD,
    WIFI_SECIRITY_MODE
)

broadlink.setup(WIFI_SSID, WIFI_PASSWORD, WIFI_SECIRITY_MODE)

try:
    device = broadlink.discover(timeout=1)[0]
    device.auth()
except IndexError:
    print("Broadlink is turned of")

import ipdb; ipdb.set_trace()