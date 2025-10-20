# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    planning_count = fields.Integer(
        string='Nombre de plannings',
        compute='_compute_planning_count'
    )

    @api.depends('id')
    def _compute_planning_count(self):
        """Compute the number of planning records for this employee"""
        for employee in self:
            planning_count = self.env['acs.planning'].search_count([
                ('employee_id', '=', employee.id)
            ])
            employee.planning_count = planning_count

    def action_view_planning(self):
        """Action to view all planning records for this employee"""
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("acs_planning.action_acs_planning")
        action['domain'] = [('employee_id', '=', self.id)]
        action['context'] = {
            'default_employee_id': self.id,
            'search_default_employee': 1,
        }
        return action

    def action_print_employee_planning(self):
        """Action to print employee planning report"""
        self.ensure_one()
        return self.env.ref('acs_planning_reports.action_report_employee_planning').report_action(self)


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'

    planning_count = fields.Integer(
        string='Nombre de plannings',
        compute='_compute_planning_count'
    )

    @api.depends('id')
    def _compute_planning_count(self):
        """Compute the number of planning records for this employee"""
        for employee in self:
            planning_count = self.env['acs.planning'].search_count([
                ('employee_id', '=', employee.id)
            ])
            employee.planning_count = planning_count
