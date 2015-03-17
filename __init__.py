#This file is part carrier_api_subdivision_report module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .api import *
from .company import *

def register():
    Pool.register(
        CarrierApi,
        CarrierApiSubdivisionReport,
        CompanySubdivision,
        module='carrier_api_subdivision_report', type_='model')
