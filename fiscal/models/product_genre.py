# Copyright (C) 2019  Renato Lima - Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class ProductGenre(models.Model):
    _name = 'fiscal.product.genre'
    _order = 'code'
    _description = 'Fiscal Product Genre'

    code = fields.Char(
        string='Code',
        required=True,
        index=True)

    name = fields.Char(
        string='Name',
        required=True,
        index=True)

    @api.model
    def _name_search(self, name, args=None, operator='ilike',
                     limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('code', operator, name)
                      ('name', operator, name)]

        recs = self._search(expression.AND([domain, args]), limit=limit,
                            access_rights_uid=name_get_uid)
        return self.browse(recs).name_get()

    @api.multi
    def name_get(self):
        return [(r.id,
                u"{0} - {1}".format(r.code, r.name))
                for r in self]