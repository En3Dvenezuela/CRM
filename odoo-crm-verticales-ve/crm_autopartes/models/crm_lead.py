# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_autopartes = fields.Boolean(string='Venta de Autopartes')

    cliente_tipo_auto = fields.Selection([
        ('b2c', 'Consumidor Final'),
        ('taller', 'Taller Mecánico'),
        ('flota', 'Flota Comercial'),
        ('mayorista', 'Mayorista / Distribuidor'),
        ('concesionario', 'Concesionario'),
    ], string='Tipo de Cliente Auto')

    vehiculo_id = fields.Many2one('autopartes.vehiculo', string='Vehículo')
    vehiculo_marca = fields.Char(related='vehiculo_id.marca', store=True)
    vehiculo_modelo = fields.Char(related='vehiculo_id.modelo', store=True)
    vehiculo_anio = fields.Integer(related='vehiculo_id.anio', store=True)

    pieza_solicitada_ids = fields.One2many(
        'autopartes.pieza.solicitada', 'lead_id', string='Piezas Solicitadas'
    )

    origen_repuesto = fields.Selection([
        ('oem', 'OEM (Original de Fábrica)'),
        ('aftermarket', 'Aftermarket'),
        ('usado', 'Usado / Junkyard'),
        ('remanufacturado', 'Remanufacturado'),
    ], string='Origen Preferido', default='oem')

    requiere_importacion = fields.Boolean(string='Requiere Importación')
    tiempo_entrega_dias = fields.Integer(string='Tiempo de Entrega (días)')

    incluye_instalacion = fields.Boolean(string='Incluye Instalación')
    taller_recomendado = fields.Char(string='Taller Recomendado')

    garantia_meses = fields.Integer(string='Garantía (meses)', default=3)


class AutopartesPiezaSolicitada(models.Model):
    _name = 'autopartes.pieza.solicitada'
    _description = 'Pieza Solicitada en Oportunidad'

    lead_id = fields.Many2one('crm.lead', string='Oportunidad', ondelete='cascade')
    pieza_id = fields.Many2one('autopartes.pieza', string='Pieza')
    codigo_oem = fields.Char(string='Código OEM')
    descripcion = fields.Char(string='Descripción')
    cantidad = fields.Integer(string='Cantidad', default=1)
    precio_usd = fields.Float(string='Precio Unitario USD')
    disponible = fields.Selection([
        ('stock', 'En Stock'),
        ('local', 'En Almacén Local'),
        ('importar', 'Por Importar'),
        ('no_disponible', 'No Disponible'),
    ], string='Disponibilidad', default='stock')
