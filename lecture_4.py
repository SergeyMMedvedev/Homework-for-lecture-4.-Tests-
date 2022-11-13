from collections import defaultdict


def get_geo_logs_by_country(country, geo_logs):
    return list(filter(
        lambda visit: list(*visit.values())[1] == country, geo_logs))


def get_unique_ids(ids):
    d_ids = {}
    for geo_ids in ids.values():
        for geo_id in geo_ids:
            d_ids[geo_id] = True
    return list(d_ids.keys())


def get_stats(queries):
    words_amount = defaultdict(float)
    for query in queries:
        words_amount[len(query.split())] += 1
    overall = sum(words_amount.values())
    result = []
    for qty, freq in words_amount.items():
        percent = freq / overall * 100
        result.append(f'Запросы с количеством слов "{qty}" встречаются в {percent:.2f}% случаев.')
    return '\n'.join(result)
