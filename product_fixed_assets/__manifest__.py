# -*- coding: utf-8 -*-
{
    'name': "Bienes de Uso en Productos",

    'summary': """
        Se agrega la sección de bienes de uso en el módulo de product.template""",

    'author': "Exemax - Brenda Gauto",
    'website': "http://www.exemax.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product','hr','sale','stock'],

    # always loaded
    'data': [
        'security/offices_areas_security.xml',
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/areas_offices_views.xml',
    ],
}
