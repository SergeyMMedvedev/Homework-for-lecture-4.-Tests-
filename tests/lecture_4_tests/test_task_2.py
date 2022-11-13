import pytest
from lecture_4 import get_unique_ids


IDS_1 = {'user1': [213, 213, 213, 15, 213],
         'user2': [54, 54, 119, 119, 119],
         'user3': [213, 98, 98, 35]}
IDS_2 = {'user1': [1, 1, 1],
         'user2': [1, 1, 1],
         }
IDS_FIXTURES = [
    (IDS_1, [213, 15, 54, 119, 98, 35]),
    (IDS_2, [1])
]


@pytest.mark.parametrize('ids, expect', IDS_FIXTURES)
def test_get_unique_ids(ids, expect):
    result = get_unique_ids(ids)
    assert result == expect
