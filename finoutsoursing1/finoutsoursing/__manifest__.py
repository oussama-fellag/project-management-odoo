

{
    'name' : 'FInoutsoursing',
    'version': '1.0.0',
    'category': 'finoutsoursing',
    'summary': 'Sales internal machinery',
    'description': """
     This module contains my project
     """,
    'depends': ['base' ,'sale_management', 'project'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/clientspec.xml',
    ],

    'demo': [
        'demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application' : True,
    'sequence' : -100,

}
