# -*- coding: utf-8 -*-

def post_init_hook(env):
    """
    Post-installation hook to set is_shift_employee to True for all existing employees
    """
    employees = env['hr.employee'].search([('is_shift_employee', '=', False)])
    if employees:
        employees.write({'is_shift_employee': True})
        print(f"Updated {len(employees)} employees with is_shift_employee = True")
