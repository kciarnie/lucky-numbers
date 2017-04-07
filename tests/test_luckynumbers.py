from unittest import TestCase

from click.testing import CliRunner

from luckynumber import main

statement = "This script did not do it's job. It needs to add at the minimum the azimov directory"

# Runner variable
runner = CliRunner(echo_stdin=True)


class TestLuckyNumber(TestCase):
    def test_luckynumber(self):
        """
        Tests the lucky numbers app
        :return:
        """
        result = runner.invoke(main, ["569815571556", "493853289475", "1234567", "472844278465445"])
        print(result.output)
        assert result.exit_code == 0, "%s" % result.exception
