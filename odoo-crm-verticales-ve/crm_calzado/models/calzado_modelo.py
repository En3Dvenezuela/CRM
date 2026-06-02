# -*- coding: utf-8 -*-
from odoo import models, fields


class CalzadoModelo(models.Model):
    _name = 'calzado.modelo'
    _description = 'Modelo de Calzado'

    name = fields.Char(string='Nombre del Modelo', required=True)
    marca_id = fields.Many2one('calzado.marca', string='Marca', required=True)
    sku = fields.Char(string='SKU')
    categoria = fields.Selection([
        ('running', 'Running'),
        ('basketball', 'Basketball'),
        ('training', 'Training'),
        ('lifestyle', 'Lifestyle'),
        ('soccer', 'Fútbol'),
        ('tennis', 'Tennis'),
        ('outdoor', 'Outdoor'),
        ('skate', 'Skate'),
        ('formal', 'Formal'),
    ], string='Categoría')

    genero = fields.Selection([
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
        ('unisex', 'Unisex'),
        ('niño', 'Niño/Niña'),
    ], string='Género')

    precio_usd = fields.Float(string='Precio USD')
    año_lanzamiento = fields.Integer(string='Año de Lanzamiento')
    tecnologia = fields.Char(string='Tecnología (Air, Boost, etc.)')
    imagen = fields.Image(string='Imagen', max_width=400, max_height=400)
    active = fields.Boolean(default=True)
