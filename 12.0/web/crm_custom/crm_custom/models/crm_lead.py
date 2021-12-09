# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, exceptions, _


class Lead(models.Model):
    _inherit = "crm.lead"

    num_unit = fields.Integer(string="Number of units")
    num_blocks = fields.Integer(string="Number of blocks")
    num_residents = fields.Integer(string="Number of residents")
    lobby_type = fields.Selection(
        [('own', 'Own'),
         ('outsourced', 'Outsourced')],
        string="Lobby type")
    lobby_schedule = fields.Selection(
        [('twenty_four', '12 hours'),
         ('twelve', '24 hours')],
        string="Lobby schedule")
