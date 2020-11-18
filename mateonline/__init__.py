# -*- coding: utf-8 -*-
#
#  MateOnLine
#  
#  Copyright 2020 Iuri Guilherme <https://iuri.neocities.org>,
#    Matehackers <https://matehackers.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

__version__ = '0.1.0'

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name)

name = 'mateonline'
version = __version__

try:
    logger.info(u"Iniciando MateOnLine...")
    from mateonline.controllers.fastapi_app import app as api

    logger.info(u"Iniciando MateOnLine Web...")
    from mateonline.controllers.quart_app import app as web
    api.mount("/", web)
except Exception as e:
    logger.critical(repr(e))
    logger.info(u"Encerrando MateOnLine...")
    raise
