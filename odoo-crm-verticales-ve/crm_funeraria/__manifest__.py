# -*- coding: utf-8 -*-
{
    'name': 'CRM - Servicios Funerarios',
    'version': '18.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'CRM especializado para funerarias y servicios exequiales',
    'description': """
Extiende el CRM de Odoo para funerarias:
- Tipo de servicio (inhumación, cremación, traslado, repatriación)
- Datos del fallecido (con sensibilidad)
- Modalidad: prevenido (plan futuro) vs necesidad inmediata
- Pólizas y planes funerarios
- Cementerio/destino, fecha y hora del servicio
- Etapas adaptadas al ciclo funerario
""",
    'author': 'En3D Tecnología C.A.',
    'license': 'LGPL-3',
    'depends': ['crm', 'l10n_ve_crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/crm_funeraria_data.xml',
        'data/crm_stage_data.xml',
        'views/crm_lead_views.xml',
        'views/crm_funeraria_views.xml',
    ],
    'installable': True,
    'application': False,
}
