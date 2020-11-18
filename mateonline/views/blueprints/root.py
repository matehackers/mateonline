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

from quart import (
    Blueprint,
    render_template,
    abort,
)

from jinja2 import TemplateNotFound

logger = logging.getLogger('blueprints.root')

bp = Blueprint(
    'root',
    'index',
    template_folder = 'templates',
)

@bp.route('/', defaults={'page': 'index'})
@bp.route('/<page>')
async def show(page):
    try:
        return await render_template('{0}.html'.format(page))
    except TemplateNotFound as e:
        logger.warning(
            u"Template não encontrada para {0}: {1}".format(
                str(page),
                repr(e),
            ),
        )
        await abort(404)
