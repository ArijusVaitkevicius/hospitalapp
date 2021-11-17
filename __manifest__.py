# -*- coding: utf-8 -*-
{
    'name': "Hospital App",

    'summary': """Manage hospital""",

    'description': """
        Hospital module for managing hospital:
            - patients
    """,

    'author': "Arijus Vaitkevičius",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/user_inherited_view.xml',
        'views/doctor_type_view.xml',
        'views/doctor_view.xml',
        'views/diagnosis_view.xml',
        'views/prescription_view.xml',
        'views/receptionist_view.xml',
        'views/appointment_view.xml',
        'views/drug_view.xml',
        'views/prescription_line_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install': True,
}