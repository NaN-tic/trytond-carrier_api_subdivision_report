# This file is part of the carrier_api_subdivision_report module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class CarrierApiSubdivisionReportTestCase(ModuleTestCase):
    'Test Carrier Api Subdivision Report module'
    module = 'carrier_api_subdivision_report'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        CarrierApiSubdivisionReportTestCase))
    return suite