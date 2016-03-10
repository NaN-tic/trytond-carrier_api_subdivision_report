#This file is part company_subdivision module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction
from trytond.config import config
import os

__all__ = ['CompanySubdivision']
__metaclass__ = PoolMeta


class CompanySubdivision:
    __name__ = "company.subdivision"

    @classmethod
    def __register__(cls, module_name):
        super(CompanySubdivision, cls).__register__(module_name)
        # create directory
        database_name = Transaction().database.name
        directory = os.path.join(config.get('database', 'path'),
            database_name, "reports")
        if not os.path.isdir(directory):
            os.makedirs(directory)
 
    @classmethod
    def carrier_api_directory(cls, api):
        '''Return report directory from user subdivision and api'''
        pool = Pool()
        User = pool.get('res.user')
        CarrierApiSubdivisionReport  = pool.get('carrier.api.subdivision.report')

        report_directory = None

        user = User(Transaction().user)
        if user.subdivision:
            subdivision_reports = CarrierApiSubdivisionReport.search([
                ('api', '=', api.id),
                ('subdivision', '=', user.subdivision),
                ], limit=1)
            if not subdivision_reports:
                return report_directory
            subdivision_report, = subdivision_reports

            if subdivision_report.directory:
                report_directory = subdivision_report.directory

        return report_directory
