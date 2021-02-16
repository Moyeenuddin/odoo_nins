# -*- coding: utf-8 -*-
{
    'name': "Transaction Report",

    'summary': """ Provides Reports about Journal Card , Customer Transaction, other Transaction """,

    'description':
        """ Provides Reports about Journal Card , Customer Transaction, other Transaction """,


    'author': "Md. Moyeenuddin Khan",
    'website': "http://www.ctechbd.com",

    'category': 'Accounting',
    'sequence': 1,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}