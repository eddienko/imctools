# -*- coding: utf-8 -*-

import sys
import os
import unittest
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .generate_testcase import ParsingTestMCD

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'data',
    )

TESTCASES = ( os.path.join(FIXTURE_DIR,"20170805_p60-63_slide6_ac1_vz.mcd"),
              os.path.join(FIXTURE_DIR,"20170829_20170805_p60-63_slide6_ac1_vz.mcd.pickle") )

class TestMcdParsing(unittest.TestCase):
    """ Compare the current MCD parser results with some stored ones """

    def parser_test(self, Parser):
        fn_mcd, testresults = TESTCASES
        testpickle= ParsingTestMCD(testresults)
        testpickle.read_testdict_pickle(testresults)
        testmcd = ParsingTestMCD(fn_mcd)
        testmcd.read_mcd(fn_mcd, Parser=Parser)
        dict_p = testpickle.testdict
        dict_m = testpickle.testdict
        self.assertSetEqual(set(dict_p['acquisition_ids']), set(dict_m['acquisition_ids']))
        for ac in dict_p['acquisition_ids']:
            ac_p = dict_p['acquisitions'][ac]
            ac_m = dict_m['acquisitions'][ac]
            for a in ['ac_desc', 'ac_rawdim', 'ac_nchan']:
                self.assertEqual(ac_p[a], ac_m[a])
                a= 'ac_channels'
                self.assertDictEqual(ac_p[a], ac_m[a])
