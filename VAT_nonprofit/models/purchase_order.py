# -*- encoding: UTF-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015-Today Laxicon Solution.
#    (<https://fundatiaethos.ro>)
#    rzvpais@gmail.com
#
##############################################################################
from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order.line"

    pret_furnizor = fields.Float(string='Pret Furnizor')


