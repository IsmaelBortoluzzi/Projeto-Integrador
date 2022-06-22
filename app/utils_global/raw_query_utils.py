def first(query_set):
    try:
        query_set = query_set[0]
    except IndexError:
        query_set = None

    return query_set
