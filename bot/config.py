#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2023 Kaif_00z
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
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBOt/blob/main/LICENSE > .

from decouple import config


class Var:
    REDIS_URI = config("REDIS_URI", default="redis-15810.c11.us-east-1-2.ec2.cloud.redislabs.com:15810")
    REDIS_PASS = config("REDIS_PASS", default="EVUmE5RmQwgsL9Ycp6mzMEBEOmf06cSF")
    API_ID = config("API_ID", default=8781248, cast=int)
    API_HASH = config("API_HASH", default="329a9246cc001b67895fd68a85d0f867")
    BOT_TOKEN = config("BOT_TOKEN", default="6390946641:AAHnKqQNWbDzM-Vm4xqaIsse-iKjuLOzqEY")
    BACKUP = config("BACKUP", default=-1001864097857, cast=int)
    FFMPEG = config("FFMPEG", default="ffmpeg")
    CHAT = config("CHAT", default=-1001822986276, cast=int)
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/37d9d0657d51e01a71f26.jpg"
    )
    LOG_CHANNEL = config("LOG_CHANNEL", default=-1001864097857, cast=int)
    CLOUD = config("CLOUD", default=-1001864097857, cast=int)
    OWNERS = config("OWNERS", default="1174557449")
