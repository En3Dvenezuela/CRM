# -*- coding: utf-8 -*-
from odoo import models, fields


class CrmFunerariaPlan(models.Model):
    _name = 'crm.funeraria.plan'
    _description = 'Plan Funerario'
    _order = 'sequence, name'

    name = fields.Char(string='Nombre del Plan', required=True)
    sequence = fields.Integer(default=10)
    code = fields.Char(string='Código')

    nivel = fields.Selection([
        ('basico', 'Básico'),
        ('estandar', 'Estándar'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    ], string='Nivel', default='estandar')

    precio_usd = fields.Monetary(string='Precio USD', currency_field='currency_id')
    cuota_mensual_usd = fields.Monetary(string='Cuota Mensual USD', currency_field='currency_id')
    meses_financiamiento = fields.Integer(string='Meses de Financiamiento')

    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.ref('base.USD', raise_if_not_found=False)
    )

    descripcion = fields.Html(string='Descripción')

    incluye_traslado = fields.Boolean(string='Incluye Traslado')
    incluye_ataud = fields.Boolean(string='Incluye Ataúd')
    incluye_velatorio = fields.Boolean(string='Incluye Sala de Velatorio')
    incluye_carroza = fields.Boolean(string='Incluye Carroza')
    incluye_flores = fields.Boolean(string='Incluye Arreglos Florales')
    incluye_cremacion = fields.Boolean(string='Incluye Cremación')

    active = fields.Boolean(default=True)
