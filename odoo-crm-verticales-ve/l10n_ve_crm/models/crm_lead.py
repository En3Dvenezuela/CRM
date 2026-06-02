# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    l10n_ve_doc_type = fields.Selection([
        ('V', 'V - Venezolano'),
        ('E', 'E - Extranjero'),
        ('J', 'J - Jurídico'),
        ('G', 'G - Gobierno'),
        ('P', 'P - Pasaporte'),
    ], string='Tipo de Documento')

    l10n_ve_doc_number = fields.Char(string='Número de Documento')

    l10n_ve_amount_usd = fields.Monetary(
        string='Monto en USD',
        currency_field='currency_usd_id',
        help='Valor de la oportunidad expresado en USD (referencia)'
    )

    currency_usd_id = fields.Many2one(
        'res.currency',
        string='Moneda USD',
        default=lambda self: self.env.ref('base.USD', raise_if_not_found=False),
        readonly=True
    )

    l10n_ve_exchange_rate = fields.Float(
        string='Tasa BCV (Bs/USD)',
        digits=(16, 4),
        help='Tasa de cambio BCV usada para la conversión'
    )

    @api.onchange('l10n_ve_amount_usd', 'l10n_ve_exchange_rate')
    def _onchange_amount_usd(self):
        for lead in self:
            if lead.l10n_ve_amount_usd and lead.l10n_ve_exchange_rate:
                lead.expected_revenue = lead.l10n_ve_amount_usd * lead.l10n_ve_exchange_rate
