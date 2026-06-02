# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AutopartesVehiculo(models.Model):
    _name = 'autopartes.vehiculo'
    _description = 'Vehículo del Cliente'
    _rec_name = 'display_name'

    partner_id = fields.Many2one('res.partner', string='Propietario')
    marca = fields.Char(string='Marca', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    anio = fields.Integer(string='Año', required=True)
    version = fields.Char(string='Versión / Trim')
    vin = fields.Char(string='VIN (Número de Serie)', size=17)
    placa = fields.Char(string='Placa')
    motor = fields.Char(string='Motor (cilindrada)')
    transmision = fields.Selection([
        ('manual', 'Manual'),
        ('automatica', 'Automática'),
        ('cvt', 'CVT'),
        ('dct', 'DCT/DSG'),
    ], string='Transmisión')
    combustible = fields.Selection([
        ('gasolina', 'Gasolina'),
        ('diesel', 'Diésel'),
        ('hibrido', 'Híbrido'),
        ('electrico', 'Eléctrico'),
        ('gnv', 'GNV'),
    ], string='Combustible')
    kilometraje = fields.Integer(string='Kilometraje')
    color = fields.Char(string='Color')

    display_name = fields.Char(compute='_compute_display_name', store=True)

    @api.depends('marca', 'modelo', 'anio', 'placa')
    def _compute_display_name(self):
        for v in self:
            partes = [v.marca, v.modelo, str(v.anio) if v.anio else '']
            if v.placa:
                partes.append(f"({v.placa})")
            v.display_name = ' '.join(p for p in partes if p)
