import pytest


# Mock for regular test input
def mock_dino_list_in():
    return ["aaabbbbcccc", "abc", "abcddd", "dbca", "fsgjjssss"]


# Expected output for list_in
def mock_dino_list_out():
    return [["aaabbbbcccc", "abc"], ["abcddd", "dbca"]]


# Mock input where duplicates are included
def mock_dino_list_duplicates_in():
    return [
        "aaabbbbcccc",
        "aaabbbbcccc",
        "aaabbbbcccc",
        "abc",
        "abcddd",
        "abcddd",
        "dbca",
        "fsgjjssss",
    ]


# Expected output for list_duplicates_in
def mock_dino_list_duplicates_out():
    return [["aaabbbbcccc", "abc"], ["abcddd", "dbca"]]


# Mock data where a word shares the same letters as multiple other words
def mock_dino_list_many_in():
    return [
        "aaabbbbcccc",
        "abc",
        "abcddd",
        "dbca",
        "fsgjjssss",
        "qwerty",
        "tryewqqq",
        "qwwwwyerrtwe",
        "qwertywwqqq",
    ]


# Mock expected output where words share the same letters as multiple other words
def mock_dino_list_many_out():
    return [
        ["aaabbbbcccc", "abc"],
        ["abcddd", "dbca"],
        ["qwerty", "qwertywwqqq", "qwwwwyerrtwe", "tryewqqq"],
    ]


# Mock for csv input data
def mock_dino_csv_in():
    return [
        "aardonyx",
        "abelisaurus",
        "achelousaurus",
        "achillobator",
        "aralosaurus",
        "aegyptosaurus",
        "agilisaurus",
        "alamosaurus",
        "albertaceratops",
        "albertosaurus",
        "austrosaurus",
        "alioramus",
        "allosaurus",
        "torosaurus",
    ]


# Expected return data
def mock_dino_csv_out():
    return [["allosaurus", "aralosaurus"], ["austrosaurus", "torosaurus"]]

# Mock CSV file data
@pytest.fixture
def mock_csv_data():
    return [
        {
            "name": "aardonyx",
            "diet": "herbivorous",
            "period": "Early Jurassic 199-189 million years ago",
            "lived_in": "South Africa",
            "type": "sauropod",
            "length": "8.0m",
            "species": "celestae",
        },
        {
            "name": "abelisaurus",
            "diet": "carnivorous",
            "period": "Late Cretaceous 70-66 million years ago",
            "lived_in": "South America",
            "type": "theropod",
            "length": "7.4m",
            "species": "comahuensis",
        },
        {
            "name": "achelousaurus",
            "diet": "herbivorous",
            "period": "Late Cretaceous 70-66 million years ago",
            "lived_in": "North America",
            "type": "ceratopsian",
            "length": "7.0m",
            "species": "horneri",
        },
        {
            "name": "achillobator",
            "diet": "carnivorous",
            "period": "Late Cretaceous 90-84 million years ago",
            "lived_in": "Mongolia",
            "type": "theropod",
            "length": "5.0m",
            "species": "giganticus",
        },
        {
            "name": "aralosaurus",
            "diet": "herbivorous",
            "period": "Late Cretaceous 70-66 million years ago",
            "lived_in": "Kazakhstan",
            "type": "sauropod",
            "length": "8.0m",
            "species": "tubiferus",
        },
    ]
