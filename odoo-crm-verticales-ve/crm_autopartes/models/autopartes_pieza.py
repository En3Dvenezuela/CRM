# -*- coding: utf-8 -*-
from odoo import models, fields


class AutopartesPieza(models.Model):
    _name = 'autopartes.pieza'
    _description = 'Pieza de Repuesto'

    name = fields.Char(string='Nombre', required=True)
    codigo_interno = fields.Char(string='Código Interno')
    codigo_oem = fields.Char(string='Código OEM')
    codigos_equivalentes = fields.Text(string='Códigos Equivalentes')

    categoria = fields.Selection([
        ('motor', 'Motor'),
        ('transmision', 'Transmisión'),
        ('suspension', 'Suspensión'),
        ('frenos', 'Frenos'),
        ('electrico', 'Sistema Eléctrico'),
        ('carroceria', 'Carrocería'),
        ('interior', 'Interior'),
        ('aire', 'Aire Acondicionado'),
        ('escape', 'Escape'),
        ('filtros', 'Filtros'),
        ('lubricantes', 'Lubricantes'),
        ('otros', 'Otros'),
    ], string='Categoría')

    marca_repuesto = fields.Char(string='Marca del Repuesto')
    origen = fields.Selection([
        ('oem', 'OEM'),
        ('aftermarket', 'Aftermarket'),
        ('usado', 'Usado'),
        ('remanufacturado', 'Remanufacturado'),
    ], string='Origen', default='aftermarket')

    pais_origen = fields.Char(string='País de Origen')
    precio_costo_usd = fields.Float(string='Costo USD')
    precio_venta_usd = fields.Float(string='Precio Venta USD')

    stock_actual = fields.Integer(string='Stock Actual')
    stock_minimo = fields.Integer(string='Stock Mínimo')

    compatible_marcas = fields.Char(string='Marcas Compatibles')
    compatible_modelos = fields.Text(string='Modelos Compatibles')
    anio_desde = fields.Integer(string='Año Desde')
    anio_hasta = fields.Integer(string='Año Hasta')

    garantia_meses = fields.Integer(string='Garantía (meses)', default=3)
    active = fields.Boolean(default=True)
