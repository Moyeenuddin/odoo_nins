# -*- encoding: utf-8 -*-

{
    'name': 'Crystal Login',
    'summary': 'The new configurable Odoo Login Screen',
    'version': '10.0.1.0',
    'category': 'Website',
    'summary': """
The new configurable Odoo Login Screen
""",
    'author': "Md. Moyeenuddin Khan",
    'sequence': 1,
    'category': 'Extra Tools',
    'website': 'http://www.ctechbd.com',
    'license': 'AGPL-3',
    'depends': [
    ],
    'data': [
        'data/ir_config_parameter.xml',
        'templates/webclient_templates.xml',
        'templates/website_templates.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
