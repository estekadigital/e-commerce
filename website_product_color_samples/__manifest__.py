# -*- coding: utf-8 -*-
{
    'name': "Website product color samples",
    'summary': """Display product color samples in product view on website""",
    'description': """Display product color samples in product view on website""",
    'author': 'Odoo Masters',
    'category': 'eCommerce',
    'version': '14.0',
    'depends': [
        'sale',
        'website_sale',
    ],
    'data': [
        'views/assets.xml',
        'views/templates.xml',
        'views/variant_templates.xml',
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
