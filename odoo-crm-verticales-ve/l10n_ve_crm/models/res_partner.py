# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    l10n_ve_doc_type = fields.Selection([
        ('V', 'V - Venezolano'),
        ('E', 'E - Extranjero'),
        ('J', 'J - Jurídico'),
        ('G', 'G - Gobierno'),
        ('P', 'P - Pasaporte'),
    ], string='Tipo de Documento')

    l10n_ve_doc_number = fields.Char(
        string='Número de Documento',
        help='Número de RIF (J/G) o cédula (V/E/P) sin guiones'
    )

    l10n_ve_rif_complete = fields.Char(
        string='RIF/Cédula Completo',
        compute='_compute_rif_complete',
        store=True
    )

    @api.depends('l10n_ve_doc_type', 'l10n_ve_doc_number')
    def _compute_rif_complete(self):
        for partner in self:
            if partner.l10n_ve_doc_type and partner.l10n_ve_doc_number:
                partner.l10n_ve_rif_complete = f"{partner.l10n_ve_doc_type}-{partner.l10n_ve_doc_number}"
            else:
                partner.l10n_ve_rif_complete = False

    @api.constrains('l10n_ve_doc_type', 'l10n_ve_doc_number')
    def _check_doc_number(self):
        for partner in self:
            if not partner.l10n_ve_doc_number:
                continue
            num = partner.l10n_ve_doc_number.strip()
            if partner.l10n_ve_doc_type in ('V', 'E'):
                if not re.match(r'^\d{6,9}$', num):
                    raise ValidationError(
                        'La cédula debe tener entre 6 y 9 dígitos numéricos.'
                    )
            elif partner.l10n_ve_doc_type in ('J', 'G'):
                if not re.match(r'^\d{8,9}$', num):
                    raise ValidationError(
                        'El RIF debe tener entre 8 y 9 dígitos numéricos.'
                    )
