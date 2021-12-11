"""Contains tests for finpack/core/cli.py
"""
__copyright__ = "Copyright (C) 2021 Matt Ferreira"

import os
import unittest
from importlib import metadata

from docopt import docopt

from finpack.core import cli


class TestCli(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.DATA_DIR = "temp"
        cls.DATA = cls.DATA_DIR + "/data.csv"

        os.mkdir(cls.DATA_DIR)
        with open(cls.DATA, "w") as openFile:
            openFile.write(
                "name,type,category,sub_category,description,2021-01-01,2021-12-01\n"
            )
            openFile.write(
                "Checking 1,asset,Cash and Cash Equivalents,Checking Accounts,,1000.00,2000.00"
            )

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.DATA)
        os.rmdir(cls.DATA_DIR)

    def test_version_option(self):
        argv = ["--version"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["--version"])

    def test_init_no_options(self):
        argv = ["init"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["init"])

    def test_init_with_filepath_option(self):
        argv = ["init", "--filepath=temp/data.csv"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["init"])
        self.assertEqual(args["--filepath"], "temp/data.csv")

    def test_init_with_sample_dataset_option(self):
        argv = ["init", "--sample-dataset"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["init"])
        self.assertTrue(args["--sample-dataset"])

    def test_init_with_overwrite_option(self):
        argv = ["init", "--overwrite"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["init"])
        self.assertTrue(args["--overwrite"])

    def test_balsheet_no_option(self):
        argv = ["balsheet"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["balsheet"])

    def test_balsheet_with_filepath_option(self):
        argv = ["balsheet", "--filepath=temp/data2.csv"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["balsheet"])
        self.assertEqual(args["--filepath"], "temp/data2.csv")

    def test_balsheet_with_levels_default(self):
        argv = ["balsheet"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["balsheet"])
        self.assertEqual(args["--levels"], "3")

    def test_balsheet_with_levels_option(self):
        argv = ["balsheet", "--levels=2"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["balsheet"])
        self.assertEqual(args["--levels"], "2")

    def test_balsheet_with_date_default(self):
        argv = ["balsheet"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["balsheet"])
        self.assertEqual(args["--date"], "today")

    def test_balsheet_with_date_option(self):
        argv = ["balsheet", "--date=2021-12-01"]

        args = docopt(cli.__doc__, argv=argv)

        self.assertTrue(args["balsheet"])
        self.assertEqual(args["--date"], "2021-12-01")
