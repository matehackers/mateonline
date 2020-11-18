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

import logging
logger = logging.getLogger('routers.root')

from fastapi import (
    APIRouter,
    Form,
)

router = APIRouter()

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
