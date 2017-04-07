from unittest import TestCase

import sys
from click.testing import CliRunner

# Constant statment
import luckynumber

statement = "This script did not do it's job. It needs to add at the minimum the azimov directory"

# Runner variable
runner = CliRunner(echo_stdin=True)


class TestLuckyNumbers(TestCase):
    def test_luckynumbers(self):
        """
        Tests the lucky numbers app
        :return:
        """
        number_strings = ["569815571556", "4938532894754", "1234567", "472844278465445"]
        for i in number_strings:
            value = None
            try:
                value = int(i)
            except:  # catch *all* exceptions
                e = sys.exc_info()[0]
                print("The current value is not a valid number")

            if value:
                result = runner.invoke(luckynumber.main, i)
                assert result.exit_code == 0, "%s" % result.exception
