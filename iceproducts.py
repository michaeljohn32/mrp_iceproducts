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
from openerp import models, fields

class product_template(models.Model):
    _inherit = 'product.template'

    drawingfilename = fields.Char(string="DrawingFileName")
    productname = fields.Char(string="BOM_ProductDesc")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
