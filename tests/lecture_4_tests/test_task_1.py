import pytest
from lecture_4 import get_geo_logs_by_country


GEO_LOGS = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
GEO_LOGS_RU = [
    {'visit1': ['Москва', 'Россия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
GEO_LOGS_IN = [
    {'visit2': ['Дели', 'Индия']},
]
GEO_FIXTURES = [
    ('Россия', GEO_LOGS, GEO_LOGS_RU),
    ('Индия', GEO_LOGS, GEO_LOGS_IN),
    ('Швабия', GEO_LOGS, [])
]


@pytest.mark.parametrize('country, geo_logs, expect', GEO_FIXTURES)
def test_get_geo_logs_by_country(country, geo_logs, expect):
    result = get_geo_logs_by_country(country, geo_logs)
    assert result == expect
