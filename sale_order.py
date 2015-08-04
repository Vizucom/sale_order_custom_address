# -*- coding: utf-8 -*-
from openerp.osv.orm import Model
from openerp.osv import osv, fields
from openerp.tools.translate import _

class sale_order(osv.Model):

    _inherit = 'sale.order'

    def onchange_use_custom_address(self, cr, uid, ids, use_custom_address, partner_id, context=None):
        
        if use_custom_address and partner_id:
            
            selected_partner = self.pool.get('res.partner').browse(cr, uid, partner_id, context)
            
            res = {
                'value': {
                    'custom_name': selected_partner.name,
                    'custom_street': selected_partner.street,
                    'custom_street2': selected_partner.street2,
                    'custom_city': selected_partner.city,
                    'custom_zip': selected_partner.zip,
                    'custom_country_id': selected_partner.country_id and selected_partner.country_id.id or False,
                }
            }
        else:
            res = {}
        
        return res

    
    _columns = {
        'use_custom_address':   fields.boolean('Use Custom Info', help="Show custom info on the printout instead of the Customer's data"),
        'custom_name':          fields.char('Name', size=128),
        'custom_street':        fields.char('Street', size=128),
        'custom_street2':       fields.char('Street2', size=128),
        'custom_city':          fields.char('City', size=128),
        'custom_zip':           fields.char('Zip', size=128),
        'custom_country_id':    fields.many2one('res.country', 'Country'),
    }

    _defaults = {
        'use_custom_address': False,
    }
