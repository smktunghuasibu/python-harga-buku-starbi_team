import pytest
from harga_buku import *  # Replace `your_module` with the actual module name where the function is defined
from unittest.mock import patch
from io import StringIO

@pytest.mark.parametrize("jenisbuku, kuantiti, expected_potongan_harga, expected_harga", [
    (1, 10, (6.00 * 0.1) * 10, (6.00 * 10) - ((6.00 * 0.1) * 10)),  # Test for book type 1
    (2, 5, (7.50 * 0.08) * 5, (7.50 * 5) - ((7.50 * 0.08) * 5)),   # Test for book type 2
    (3, 8, (8.90 * 0.05) * 8, (8.90 * 8) - ((8.90 * 0.05) * 8)),   # Test for book type 3 (other types)
    (1, 0, 0.0, 0.0),  # Edge case: quantity = 0, book type 1
    (2, 0, 0.0, 0.0),  # Edge case: quantity = 0, book type 2
    (3, 0, 0.0, 0.0),  # Edge case: quantity = 0, other book types
])
def test_harga_bayaran(jenisbuku, kuantiti, expected_potongan_harga, expected_harga):
    assert harga_bayaran(jenisbuku, kuantiti) == (expected_potongan_harga, expected_harga)

@pytest.fixture
def mock_harga_bayaran():
    with patch("harga_buku.harga_bayaran", return_value=(5.0, 55.0)) as mock:
        yield mock

def test_main_valid_input(mock_harga_bayaran):
    # Mock user inputs: `jenisbuku = 1`, `kuantiti = 10`
    with patch("builtins.input", side_effect=["1", "10"]), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()  # Call the main function

        # Capture the printed output
        output = mock_stdout.getvalue()

        # Check if the output contains expected strings
        assert "Senarai belian buku:" in output
        assert "Potongan harga yang diperoleh ialah RM 5.0" in output
        assert "Jumlah harga yang perlu dibayar ialah RM 55.0" in output
        mock_harga_bayaran.assert_called_once_with(1, 10)

def test_main_invalid_input_then_valid(mock_harga_bayaran):
    # Mock user inputs: invalid `jenisbuku = 4`, then valid `jenisbuku = 2`, `kuantiti = 5`
    with patch("builtins.input", side_effect=["4", "2", "5"]), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()  # Call the main function

        # Capture the printed output
        output = mock_stdout.getvalue()

        # Check for prompt to enter correct number, then successful processing
        assert "Sila masukkan nombor 1 hingga 3 sahaja." in output
        assert "Potongan harga yang diperoleh ialah RM 5.0" in output
        assert "Jumlah harga yang perlu dibayar ialah RM 55.0" in output
        mock_harga_bayaran.assert_called_once_with(2, 5)
