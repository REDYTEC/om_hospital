{
    'name': "Hospital Management",
    'author': 'RED Y TEC',
    'version': '14.0.1.0.0',
    'summary': 'Hospital Management Software',
    'sequence': 20,
    'description': """Longer Description""",
    'category': 'Productivity',
    'website': 'http://www.redytec.com',
    'depends': [
        'sale',
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient_view.xml',
        'views/sale.xml',
        'view/kids_view'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto:install': False,
}
