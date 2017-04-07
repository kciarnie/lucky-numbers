from unittest import TestCase

from click.testing import CliRunner

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
        result = runner.invoke(luckynumber.main, "569815571556", "493853289475", "1234567", "472844278465445")
        assert result.exit_code == 0, "%s" % result.exception
