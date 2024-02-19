from io import StringIO
from unittest.mock import patch
from student import main, Brawler

def test_main():
    expected_output = "Aragorn wins with 16 power over Gimli's 14\nLegolas wins with 49 power over Frodo's 6\n"

    with patch('sys.stdout', new=StringIO()) as fake_out:
        main()
        assert fake_out.getvalue() == expected_output

# Run the test
test_main()
