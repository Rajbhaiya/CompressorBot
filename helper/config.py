#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("13675555", cast=int)
    API_HASH = config("c0da9c346d2c45dbc7ec49a05da9b2b6")
    BOT_TOKEN = config("5696982423:AAHZ1XwGXCwVxjtMobLfaGnZUzykNl5_0_s")
    OWNER = config("5591954930", default=1322549723, cast=int)
    LOG = config("-1001877655342", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
