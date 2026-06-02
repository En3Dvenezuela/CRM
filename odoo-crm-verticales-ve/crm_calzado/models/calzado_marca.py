# -*- coding: utf-8 -*-
from odoo import models, fields


class CalzadoMarca(models.Model):
    _name = 'calzado.marca'
    _description = 'Marca de Calzado'

    name = fields.Char(string='Marca', required=True)
    code = fields.Char(string='Código')
    pais_origen = fields.Char(string='País de Origen')
    segmento = fields.Selection([
        ('deportivo', 'Deportivo'),
        ('lifestyle', 'Lifestyle'),
        ('lujo', 'Lujo'),
        ('outdoor', 'Outdoor'),
        ('formal', 'Formal'),
    ], string='Segmento Principal')
    logo = fields.Image(string='Logo', max_width=200, max_height=200)
    active = fields.Boolean(default=True)
