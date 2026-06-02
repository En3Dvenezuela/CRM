# -*- coding: utf-8 -*-
{
    'name': 'CRM - Venta de Calzado Retail',
    'version': '18.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'CRM para tiendas de calzado deportivo y retail',
    'description': """
Extiende el CRM de Odoo para venta de calzado retail/deportivo:
- Marca preferida (Nike, Adidas, Skechers, Under Armour, On Running, etc.)
- Talla del cliente con tabla de equivalencias (US/EU/UK/MX)
- Categoría deportiva (running, basketball, training, lifestyle, etc.)
- Tipo de pisada (neutra, pronadora, supinadora)
- Historial de compras y modelos favoritos
- Programa de fidelización y referidos
- Personalización 3D (integración con servicios de En3D)
""",
    'author': 'En3D Tecnología C.A.',
    'license': 'LGPL-3',
    'depends': ['crm', 'l10n_ve_crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/crm_stage_data.xml',
        'data/calzado_marcas_data.xml',
        'views/crm_lead_views.xml',
        'views/calzado_views.xml',
    ],
    'installable': True,
    'application': False,
}
