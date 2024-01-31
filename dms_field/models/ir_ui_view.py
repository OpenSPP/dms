# Copyright 2020 Creu Blanca
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    type = fields.Selection(selection_add=[("dms_tree", "DMS Tree")])
