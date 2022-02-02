# -*- coding: utf-8 -*-
# from odoo import http


# class ImOdProjectBpmnBase(http.Controller):
#     @http.route('/im_od_project_bpmn_base/im_od_project_bpmn_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/im_od_project_bpmn_base/im_od_project_bpmn_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('im_od_project_bpmn_base.listing', {
#             'root': '/im_od_project_bpmn_base/im_od_project_bpmn_base',
#             'objects': http.request.env['im_od_project_bpmn_base.im_od_project_bpmn_base'].search([]),
#         })

#     @http.route('/im_od_project_bpmn_base/im_od_project_bpmn_base/objects/<model("im_od_project_bpmn_base.im_od_project_bpmn_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('im_od_project_bpmn_base.object', {
#             'object': obj
#         })
