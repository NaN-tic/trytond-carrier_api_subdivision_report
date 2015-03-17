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
        cursor = Transaction().cursor
        directory = os.path.join(config.get('database', 'path'),
            cursor.database_name, "reports")
        if not os.path.isdir(directory):
            os.makedirs(directory)
 
    @staticmethod
    def carrier_api_directory(data):
        '''Return report directory (full path) from user subdivision'''
        pool = Pool()
        CarrierApiSubdivisionReport  = pool.get('carrier.api.subdivision.report')
        User = pool.get('res.user')

        report_directory = None

        user = User(Transaction().user)
        if user.subdivision:
            subdivision_reports = CarrierApiSubdivisionReport.search([
                ('api', '=', data.get('api_id')),
                ('subdivision', '=', user.subdivision),
                ], limit=1)
            if not subdivision_reports:
                return report_directory
            subdivision_report, = subdivision_reports

            if subdivision_report.directory:
                directory = subdivision_report.directory
                # create directory
                cursor = Transaction().cursor
                report_directory = os.path.join(config.get('database', 'path'),
                    cursor.database_name, "reports", directory)
                if not os.path.isdir(report_directory):
                    os.makedirs(report_directory)

        return report_directory
