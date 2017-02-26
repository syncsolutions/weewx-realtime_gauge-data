#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
#                     Installer for Realtime gauge-data
#
# Version: 0.2.7                                        Date: 26 February 2017
#
# Revision History
#   26 February 2017    v0.2.7
#       - bumped version number only
#   22 February 2017    v0.2.6
#       - reworked Groups
#   21 February 2017    v0.2.5
#       - trimmed a number of config options
#   20 February 2017    v0.2.4
#       - bumped version number only
#   20 February 2017    v0.2.3
#       - removed min_interval config option
#   19 February 2017    v0.2.2
#       - added mile to string formats
#   15 February 2017    v0.2.1
#       - minor formatting changes
#   24 January 2017      v0.2
#       - updated weewx.conf options
#   10 January 2017      v0.1
#       - initial implementation
#

import weewx

from distutils.version import StrictVersion
from setup import ExtensionInstaller

REQUIRED_VERSION = "3.4.0"
RTGD_VERSION = "0.2.7"

def loader():
    return RtgdInstaller()

class RtgdInstaller(ExtensionInstaller):
    def __init__(self):
        if StrictVersion(weewx.__version__) < StrictVersion(REQUIRED_VERSION):
            msg = "%s requires weeWX %s or greater, found %s" % ('Rtgd ' + RTGD_VERSION,
                                                                 REQUIRED_VERSION,
                                                                 weewx.__version__)
            raise weewx.UnsupportedFeature(msg)
        super(RtgdInstaller, self).__init__(
            version=RTGD_VERSION,
            name='Rtgd',
            description='weeWX support for near realtime updating of the SteelSeries Weather Gauges.',
            author="Gary Roderick",
            author_email="gjroderick@gmail.com",
            report_services=['user.rtgd.RealtimeGaugeData'],
            config={
                'RealtimeGaugeData': {
                    'date_format': '%Y.%m.%d %H:%M',
                    'rtgd_path': '/home/weewx/public_html',
                    'StringFormats': {
                        'degree_C': '%.1f',
                        'degree_F': '%.1f',
                        'degree_compass': '%.0f',
                        'hPa': '%.1f',
                        'inHg': '%.3f',
                        'inch': '%.2f',
                        'inch_per_hour': '%.2f',
                        'km_per_hour': '%.0f',
                        'km': '%.1f',
                        'mbar': '%.1f',
                        'meter': '%.0f',
                        'meter_per_second': '%.1f',
                        'mile': '%.1f',
                        'mile_per_hour': '%.0f',
                        'mm': '%.1f',
                        'mm_per_hour': '%.1f',
                        'percent': '%.0f',
                        'uv_index': '%.1f',
                        'watt_per_meter_squared': '%.0f'
                    },
                    'Groups': {
                        'group_altitude': 'foot',
                        'group_pressure': 'hPa',
                        'group_rain': 'mm',
                        'group_speed': 'km_per_hour',
                        'group_temperature': 'degree_C'
                    }
                }
            },
            files=[('bin/user', ['bin/user/rtgd.py'])]
        )
