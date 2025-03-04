import pytest

from complete_json import complete_json


@pytest.mark.parametrize(
    'input_json, expected',
    [
        ('{', '{}'),
        ('[', '[]'),
        ('[{', '[{}]'),
        ('[{}, {', '[{}, {}]'),
        ('"', '""'),
        ('{"a', '{"a"}'),
        (r'{"a": "\"hello\", he said', r'{"a": "\"hello\", he said"}'),
    ],
)
def test_completion(input_json: str, expected: str) -> None:
    assert complete_json(input_json) == expected


# todo future tests:
# r'{"a": "\"hello' -> r'{"a": "\"hello\""}'
# '{"a": "\\' -> '{"a": ""}'
# '{"a": 1,' -> '{"a": 1}'
