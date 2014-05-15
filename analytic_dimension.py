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


class analytic_dimension(osv.Model):
    _name = "analytic.dimension"

    _columns = dict(
        name=fields.char("Name", size=128, translate=True, required=True),
        validated=fields.boolean("Validated"),
        nc_ids=fields.one2many("analytic.code", "nd_id", "Codes"),
        ns_id=fields.one2many("analytic.structure", "nd_id", "Structures"),
        ns1_id=fields.one2many(
            'analytic.structure',
            'nd_id',
            u"Structures 1",
            domain=[('ordering', '=', 1)],
            auto_join=True
        ),
        ns2_id=fields.one2many(
            'analytic.structure',
            'nd_id',
            u"Structures 2",
            domain=[('ordering', '=', 2)],
            auto_join=True
        ),
        ns3_id=fields.one2many(
            'analytic.structure',
            'nd_id',
            u"Structures 3",
            domain=[('ordering', '=', 3)],
            auto_join=True
        ),
        ns4_id=fields.one2many(
            'analytic.structure',
            'nd_id',
            u"Structures 4",
            domain=[('ordering', '=', 4)],
            auto_join=True
        ),
        ns5_id=fields.one2many(
            'analytic.structure',
            'nd_id',
            u"Structures 5",
            domain=[('ordering', '=', 5)],
            auto_join=True
        ),
    )

    _sql_constraints = [
        ('unique_name', 'unique(name)', u"Name must be unique"),
    ]
