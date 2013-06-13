# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 XCG Consulting (www.xcg-consulting.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
from openerp.tools.translate import _


class analytic_code(osv.Model):
    _name = "analytic.code"

    _columns = dict(
        name=fields.char("Name", size=128, translate=True, required=True),
        nd_id=fields.many2one(
            "analytic.dimension", ondelete="restrict"),
        nd_name=fields.related('nd_id', 'name', type="char",
                               string="Dimension Name", store=False),
        description=fields.char('Description', size=512),
    )
