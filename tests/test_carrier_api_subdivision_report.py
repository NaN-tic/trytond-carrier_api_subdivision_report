#!/usr/bin/env python
# This file is part carrier_api_subdivision_report module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class CarrierApiSubdivisionReportTestCase(unittest.TestCase):
    'Test Carrier API Subdivision Report module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('carrier_api_subdivision_report')

    def test0005views(self):
        'Test views'
        test_view('carrier_api_subdivision_report')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            CarrierApiSubdivisionReportTestCase))
    return suite
