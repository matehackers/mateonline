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
logger = logging.getLogger('routers.items')

from typing import Optional

from fastapi import (
    APIRouter,
    Query,
    Path,
)

from mateonline.models.item import Item

router = APIRouter()

@router.get("/")
async def read_items(
    skip: int = 0,
    limit: int = 10,
    q: Optional[list[str]] = Query(
        None,
        min_length = 3,
        max_length = 50,
        title = "Query string",
        description = """Query string for the items to search in the da\
tabase that have a good match""",
        alias = "item-query",
        # ~ regex="^fixedquery$",
        deprecated = True,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.post("/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@router.get("/{item_id}")
async def read_user_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=1),
    needy: str,
    skip: int = 0,
    limit: Optional[int] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": """This is an amazing item that ha\
s a long description"""})
    return item

@router.put("/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: Optional[str] = None,
    item: Optional[Item] = None,
):
    results = {"item_id": item_id, **item.dict()}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
