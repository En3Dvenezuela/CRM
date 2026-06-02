# -*- coding: utf-8 -*-
{
    'name': 'CRM - Venta de Autopartes',
    'version': '18.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'CRM para venta de repuestos y autopartes',
    'description': """
Extiende el CRM de Odoo para venta de autopartes:
- Datos del vehículo del cliente (VIN, marca, modelo, año, motor)
- Tipo de cliente (B2C, taller, flota, mayorista)
- Pieza solicitada con código OEM/aftermarket
- Disponibilidad y tiempo de importación
- Equivalencias y compatibilidad
- Garantía y origen (OEM, aftermarket, usado)
""",
    'author': 'En3D Tecnología C.A.',
    'license': 'LGPL-3',
    'depends': ['crm', 'l10n_ve_crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/crm_stage_data.xml',
        'data/autopartes_data.xml',
        'views/crm_lead_views.xml',
        'views/autopartes_views.xml',
    ],
    'installable': True,
    'application': False,
}
