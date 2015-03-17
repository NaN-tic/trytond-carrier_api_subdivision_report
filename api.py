#This file is part carrier_api_subdivision_report module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['CarrierApi', 'CarrierApiSubdivisionReport']
__metaclass__ = PoolMeta


class CarrierApi:
    __name__ = 'carrier.api'
    subdivisions = fields.One2Many('carrier.api.subdivision.report', 'api',
        'Subdivisions')


class CarrierApiSubdivisionReport(ModelSQL, ModelView):
    'Carrier API Subdivision Report'
    __name__ = "carrier.api.subdivision.report"
    api = fields.Many2One('carrier.api', 'Carrier API', ondelete='CASCADE',
        select=True, required=True)
    subdivision = fields.Many2One('company.subdivision', 'Subdivision',
        ondelete='CASCADE', select=True, required=True)
    directory = fields.Char('Directory', required=True,
        help='Directory name (without "/")')
    active = fields.Boolean('Active')

    @staticmethod
    def default_active():
        return True
