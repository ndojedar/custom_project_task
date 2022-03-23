# -*- coding: utf-8 -*-
# from odoo import http


# class CustomProjectTask(http.Controller):
#     @http.route('/custom_project_task/custom_project_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_project_task/custom_project_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_project_task.listing', {
#             'root': '/custom_project_task/custom_project_task',
#             'objects': http.request.env['custom_project_task.custom_project_task'].search([]),
#         })

#     @http.route('/custom_project_task/custom_project_task/objects/<model("custom_project_task.custom_project_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_project_task.object', {
#             'object': obj
#         })
