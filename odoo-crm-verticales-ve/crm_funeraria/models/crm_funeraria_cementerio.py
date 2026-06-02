# -*- coding: utf-8 -*-
from odoo import models, fields


class CrmFunerariaCementerio(models.Model):
    _name = 'crm.funeraria.cementerio'
    _description = 'Cementerio / Destino Final'

    name = fields.Char(string='Nombre', required=True)
    tipo = fields.Selection([
        ('cementerio', 'Cementerio'),
        ('crematorio', 'Crematorio'),
        ('osario', 'Osario'),
        ('mausoleo', 'Mausoleo'),
    ], string='Tipo', default='cementerio')

    state_id = fields.Many2one('res.country.state', string='Estado')
    city = fields.Char(string='Ciudad')
    address = fields.Text(string='Dirección')
    phone = fields.Char(string='Teléfono')
    contact = fields.Char(string='Persona de Contacto')
    active = fields.Boolean(default=True)
