import pytest

from complete_json import complete_json


@pytest.mark.parametrize(
    'input_json',
    [
        '""',
        '{}',
        '[]',
        '[{}]',
        '[{}, {}]',
        '[{}, {}, {}]',
        '{"one": {}}',
        '{"one": {}, "two": {}}',
        '{"one": {}, "two": []}',
        '[{"one": {}, "two": []}]',
    ],
)
def test_completed(input_json: str) -> None:
    assert complete_json(input_json) == input_json
