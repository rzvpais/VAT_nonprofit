# -*- encoding: UTF-8 -*-
##############################################################################
#
#
##############################################################################
from odoo import models, fields

class Product(models.Model):
    _inherit = 'product.product'
    
    tva = fields.Float(string='Tva')
