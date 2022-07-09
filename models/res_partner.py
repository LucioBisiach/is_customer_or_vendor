# -*- coding: utf-8 -*-

from odoo import models, fields ,api, _
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_customer = fields.Boolean(string="Is Customer")
    is_vendor = fields.Boolean(string="Is Vendor")

    def write(self, values):
        res = super(ResPartner, self).write(values)
        # if is_customer = True create customer partner and if is_vendor=True create supplier
        if self.is_customer == True and self.customer_rank == 0:
            self.customer_rank = 1
        if self.is_vendor == True and self.supplier_rank == 0:
            self.supplier_rank = 1
        return res
