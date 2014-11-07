# -*- coding: utf-8 -*-
{
    'name': "mrp_iceproducts",

    'summary': """
        This adds fields relevant to the product line
    """,

    'description': """
        This module was created to have a place to house the latest
        product information from the database.
    """,

    'author': "John Walsh",
    'website': "http://github.com/michaeljohn32",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',   
        'view/iceproducts_view.xml',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
