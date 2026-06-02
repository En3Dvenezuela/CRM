# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_funeraria = fields.Boolean(string='Servicio Funerario')

    funeraria_modalidad = fields.Selection([
        ('prevenido', 'Prevenido (Plan a futuro)'),
        ('necesidad', 'Necesidad Inmediata'),
        ('traslado', 'Traslado/Repatriación'),
    ], string='Modalidad')

    funeraria_servicio_tipo = fields.Selection([
        ('inhumacion', 'Inhumación'),
        ('cremacion', 'Cremación'),
        ('embalsamamiento', 'Embalsamamiento'),
        ('traslado_nacional', 'Traslado Nacional'),
        ('traslado_internacional', 'Traslado Internacional / Repatriación'),
        ('servicio_completo', 'Servicio Completo'),
    ], string='Tipo de Servicio')

    # Datos del fallecido (sólo en necesidad inmediata)
    fallecido_nombre = fields.Char(string='Nombre del Fallecido')
    fallecido_cedula = fields.Char(string='Cédula del Fallecido')
    fallecido_fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    fallecido_fecha_fallecimiento = fields.Datetime(string='Fecha de Fallecimiento')
    fallecido_lugar = fields.Char(string='Lugar de Fallecimiento')
    fallecido_causa = fields.Char(string='Causa del Fallecimiento')

    # Servicio
    plan_id = fields.Many2one('crm.funeraria.plan', string='Plan Contratado')
    cementerio_id = fields.Many2one('crm.funeraria.cementerio', string='Cementerio/Destino')
    velatorio_sala = fields.Char(string='Sala de Velatorio')
    velatorio_fecha = fields.Datetime(string='Fecha y Hora de Velatorio')
    sepelio_fecha = fields.Datetime(string='Fecha y Hora de Sepelio')

    # Documentación
    acta_defuncion = fields.Boolean(string='Acta de Defunción Entregada')
    permiso_inhumacion = fields.Boolean(string='Permiso de Inhumación')
    permiso_cremacion = fields.Boolean(string='Permiso de Cremación')

    # Contacto familiar
    familiar_responsable = fields.Char(string='Familiar Responsable')
    familiar_parentesco = fields.Selection([
        ('conyuge', 'Cónyuge'),
        ('hijo', 'Hijo/Hija'),
        ('padre', 'Padre/Madre'),
        ('hermano', 'Hermano/Hermana'),
        ('otro', 'Otro'),
    ], string='Parentesco')
    familiar_telefono = fields.Char(string='Teléfono del Familiar')

    urgencia = fields.Selection([
        ('alta', '🔴 Alta - Servicio en menos de 24h'),
        ('media', '🟡 Media - Servicio en 1-3 días'),
        ('baja', '🟢 Baja - Planificación'),
    ], string='Urgencia', default='media')

    @api.onchange('funeraria_modalidad')
    def _onchange_modalidad(self):
        if self.funeraria_modalidad == 'necesidad':
            self.urgencia = 'alta'
        elif self.funeraria_modalidad == 'prevenido':
            self.urgencia = 'baja'
