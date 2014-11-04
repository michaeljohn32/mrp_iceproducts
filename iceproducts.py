#################################################
#  
#   This program is free software: you can
#   redistribute and/or modify it.
#
#
#
#
#
#
#
#
#
###############################################
from openerp import models, fields, api, exceptions

class product_product(models.Model):
    _inherit = 'product.template'

    drawingfilename = fields.Char(string="DrawingFileName")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
