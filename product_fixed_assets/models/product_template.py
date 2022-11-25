# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product_fixed_assets(models.Model):
    _inherit = 'product.template'
    _description = 'Bienes de Uso - Productos'

    is_fixed_assets = fields.Boolean('Es bien de uso?')
    period = fields.Date('Período')
    patrimonial_id = fields.Char('Nro ID Patrimonial')
    invoice_id = fields.Char('N° Factura')
    depositary_id = fields.Many2one('hr.employee', string='Depositario')
    supplier_id = fields.Many2one('res.partner', string='Proveedor')
    stock = fields.Selection([('yes', 'Sí'), ('no', 'No')] , string='En Stock?')
    offices = fields.Many2one('offices', string='Sucursal')
    area = fields.Many2one('areas', string='Área')
    alta = fields.Selection([('yes', 'Sí'), ('no', 'No')], string='Alta')


class Office_fixed_assets(models.Model):
    _name = 'offices'
    _description = 'Sucursales Bienes de Uso'

    name = fields.Char('Nombre de la Sucursal')

class Area_fixed_assets(models.Model):
    _name = 'areas'
    _description = 'Áreas Bienes de Uso'

    name = fields.Char('Nombre del Área')