# -*- coding: utf-8 -*-
{
    'name': 'Localización Venezolana - CRM',
    'version': '18.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Campos venezolanos para CRM: RIF, cédula, validaciones',
    'description': """
Extiende el CRM de Odoo con campos específicos para Venezuela:
- Tipo de documento (V, E, J, G, P)
- Número de RIF / Cédula con validación
- Validación de teléfonos venezolanos (+58)
- Estados y municipios de Venezuela
- Moneda dual VES/USD en oportunidades
""",
    'author': 'En3D Tecnología C.A.',
    'website': 'https://en3d.com.ve',
    'license': 'LGPL-3',
    'depends': ['crm', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/res_country_state_ve.xml',
        'views/crm_lead_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
