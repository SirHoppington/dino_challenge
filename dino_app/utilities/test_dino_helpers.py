from dino_helpers import get_avg, get_same_names, read_csv
from unittest.mock import mock_open, patch, MagicMock

import pytest

from dino_app.conftest import (
    mock_dino_list_in,
    mock_dino_list_out,
    mock_dino_list_duplicates_in,
    mock_dino_list_duplicates_out,
    mock_dino_list_many_in,
    mock_dino_list_many_out,
    mock_dino_csv_in,
    mock_dino_csv_out,
)


@pytest.mark.parametrize(
    "names_input, names_expected",
    [
        (mock_dino_list_in(), mock_dino_list_out()),
        (mock_dino_list_duplicates_in(), mock_dino_list_duplicates_out()),
        (mock_dino_list_many_in(), mock_dino_list_many_out()),
        (mock_dino_csv_in(), mock_dino_csv_out()),
    ],
)
def test_get_same_names(names_input, names_expected):
    assert get_same_names(names_input) == names_expected


@pytest.mark.parametrize(
    "length_input, length_expected",
    [
        ([1.0, 2.0, 3.0], 2.0),
        ([1.0, 33.0, 100.111, 0.0], 33.52775),
        ([40.0, 30.0, 10.0, 5.0, 111.222], 39.2444),
        ([1.0, 1.0, 1.0, 1.0, 1.0], 1.0),
    ],
)
def test_get_avg(length_input, length_expected):
    assert get_avg(length_input) == length_expected


# Test for exception handling for get_avg function
def test_get_avg_zero_div():
    assert get_avg([]) == []


# Test for exception handling for get_avg function
def test_get_avg_type_error():
    assert get_avg(["string", 100.0, "another_string"]) == []


# Test for type error exception handling for get_same_names function
def test_get_same_names_type_error():
    assert get_same_names([1234, "abc", "abcddd", "dbca", "fsgjjssss", ""]) == [
        ["abcddd", "dbca"]
    ]


# Test for function read_csv
def test_read_csv(mock_csv_data):

    # Mock the csv.DictReader to return test data
    csv_dict_reader_mock = MagicMock(return_value=mock_csv_data)
    with patch("csv.DictReader", csv_dict_reader_mock):
        # Mock the open call
        mock_file = mock_open()
        with patch("builtins.open", mock_file):
            result_lengths, result_names = read_csv("mock_file_path")

    assert result_lengths == {
        "celestae": [8.0],
        "comahuensis": [7.4],
        "horneri": [7.0],
        "giganticus": [5.0],
        "tubiferus": [8.0],
    }
    assert result_names == [
        "aardonyx",
        "abelisaurus",
        "achelousaurus",
        "achillobator",
        "aralosaurus",
    ]

    # Assert the mock was called with the correct arguments
    mock_file.assert_called_once_with("mock_file_path", mode="r")
    csv_dict_reader_mock.assert_called_once_with(
        mock_file.return_value.__enter__.return_value
    )
