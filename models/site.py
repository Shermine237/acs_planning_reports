# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Site(models.Model):
    _inherit = 'site.site'

    agent_planning_count = fields.Integer(
        string='Nombre de plannings agents',
        compute='_compute_agent_planning_count',
        help='Nombre total de plannings pour tous les agents du site'
    )

    @api.depends('agent_ids')
    def _compute_agent_planning_count(self):
        """Compute the total number of planning records for all agents of this site"""
        for site in self:
            if site.agent_ids:
                planning_count = self.env['acs.planning'].search_count([
                    ('employee_id', 'in', site.agent_ids.ids)
                ])
                site.agent_planning_count = planning_count
            else:
                site.agent_planning_count = 0

    def action_view_site_planning(self):
        """Action to view all planning records for agents of this site"""
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("acs_planning.action_acs_planning")
        action['domain'] = [('employee_id', 'in', self.agent_ids.ids)]
        action['context'] = {
            'search_default_employee': 1,
        }
        action['name'] = f'Planning - {self.name}'
        return action

    def action_print_site_planning(self):
        """Action to print site planning report for all agents"""
        self.ensure_one()
        return self.env.ref('acs_planning_reports.action_report_site_planning').report_action(self)
