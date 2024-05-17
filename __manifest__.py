{
    'name': 'Real Estate Advertisement',
    'version': '1.0',
    'summary': 'Manages your Real Estate Ads',
    'category': 'Sales',
    'author': 'Renato Monroy',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_views.xml',
        'views/estate_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'estate/static/src/xml/**/*',
            'estate/static/src/js/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
