#!/usr/bin/env python
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
logger = logging.getLogger('mateonline')

try:
    from .controllers.api import api
    from .models.user import user
except Exception as e:
    logger.critical(repr(e))
    raise

def main():
    logging.info(u"Iniciando MateOnLine...")
    logger.info(u"Iniciando MateOnLine...")
    pass
    logger.info(u"Encerrando MateOnLine...")
    return 0

if __name__ == '__main__':
    main()

