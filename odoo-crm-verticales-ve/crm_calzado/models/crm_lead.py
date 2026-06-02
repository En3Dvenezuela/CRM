# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_calzado = fields.Boolean(string='Venta de Calzado')

    calzado_genero = fields.Selection([
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
        ('unisex', 'Unisex'),
        ('niño', 'Niño'),
        ('niña', 'Niña'),
    ], string='Género')

    calzado_categoria = fields.Selection([
        ('running', 'Running'),
        ('basketball', 'Basketball'),
        ('training', 'Training / Gym'),
        ('lifestyle', 'Lifestyle / Casual'),
        ('soccer', 'Fútbol'),
        ('tennis', 'Tennis'),
        ('outdoor', 'Outdoor / Trail'),
        ('skate', 'Skate'),
        ('formal', 'Formal'),
        ('sandalias', 'Sandalias'),
    ], string='Categoría')

    calzado_marca_id = fields.Many2one('calzado.marca', string='Marca Preferida')
    calzado_modelo_interes_id = fields.Many2one('calzado.modelo', string='Modelo de Interés')

    talla_us = fields.Char(string='Talla US')
    talla_eu = fields.Char(string='Talla EU')
    talla_mx = fields.Char(string='Talla MX')
    largo_pie_cm = fields.Float(string='Largo Pie (cm)')
    ancho_pie = fields.Selection([
        ('narrow', 'Estrecho (B/2A)'),
        ('medium', 'Medio (D)'),
        ('wide', 'Ancho (2E)'),
        ('extra_wide', 'Extra Ancho (4E)'),
    ], string='Ancho del Pie')

    tipo_pisada = fields.Selection([
        ('neutra', 'Neutra'),
        ('pronadora', 'Pronadora'),
        ('supinadora', 'Supinadora'),
    ], string='Tipo de Pisada')

    arco_pie = fields.Selection([
        ('bajo', 'Arco Bajo / Plano'),
        ('medio', 'Arco Medio / Normal'),
        ('alto', 'Arco Alto'),
    ], string='Arco del Pie')

    rango_precio = fields.Selection([
        ('economico', 'Económico (< $80)'),
        ('medio', 'Medio ($80 - $150)'),
        ('alto', 'Alto ($150 - $250)'),
        ('premium', 'Premium (> $250)'),
    ], string='Rango de Precio')

    canal_compra = fields.Selection([
        ('tienda_fisica', 'Tienda Física'),
        ('online', 'Online'),
        ('whatsapp', 'WhatsApp'),
        ('instagram', 'Instagram'),
        ('redes', 'Redes Sociales'),
    ], string='Canal de Compra')

    interesa_personalizacion = fields.Boolean(
        string='Interesa Personalización 3D',
        help='Cliente interesado en personalización 3D (servicio En3D)'
    )

    cliente_fidelidad_nivel = fields.Selection([
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
    ], string='Nivel de Fidelidad')

    referido_por = fields.Many2one('res.partner', string='Referido por')

    @api.onchange('largo_pie_cm')
    def _onchange_largo_pie(self):
        """Aproximación simple talla US según cm (adulto)"""
        if self.largo_pie_cm:
            # Talla US hombre ≈ (cm - 22) / 0.667 + 4
            us = round((self.largo_pie_cm - 22) / 0.667 + 4, 1)
            self.talla_us = str(us)
            self.talla_eu = str(round(us + 33))
            self.talla_mx = str(round(us + 1.5, 1))
