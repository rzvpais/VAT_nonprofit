# -*- encoding: UTF-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015-Today Laxicon Solution.
#    (<http://fundatiaethos.ro>)
#
#
##############################################################################
{
    'name': "VAT Fundatia",
    'author': 'Razvan Pais',
    'category': 'Stock',
    'summary': """Update the delivery slip""",
    'license': 'AGPL-3',
    'website': 'https:fundatiaethos.ro',
    'description': """
    this module is made for VAT non-profit romanian companies
""",
    'version': '10.0.1.0.0',
    'depends': ['purchase','product'],
    'data': [
        'views/purchase_order_view.xml',
		'views/product_view.xml'
        ],
    'images': ['static/src/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
