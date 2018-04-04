"""
    This is to rank different paths
"""
import numpy as np


def shortest(_paths, type: str):
    # print("Before Sort")
    # for p in _paths:
    #     print(p.id)
    sort_path = sorted(_paths, key=lambda _paths: _paths.cost[type])
    # print("After Sort")
    # for p in sort_path:
    #     print(p.id)
    print("Complete shortest path ranking")

    return sort_path

    pass


def get_candidate_path(_paths, _jnd):
    """
        get the candidate set of paths
    :param _paths:
    :param _jnd:
    :return:
    """
    # step 1: obtain the minimum value for each cost attributes
    min_vector = {'Travel': 100000,
                  'Fare': 100000,
                  'Wait': 10000,
                  'Transfer': 10000}
    for key in min_vector:
        min_vector[key] = min(_paths, key=lambda _paths: _paths.att[key])
        print("Key = {0}, MinValue = {1}", key, min_vector[key].att[key])

    # step 2: compare the cost attributes with the minimum one
    candidate_paths = []
    for p in _paths:
        is_candy = True
        for key in min_vector:
            # if key == 'Transfer':
            #     continue
            # if abs(p.att[key] - min_vector[key].att[key]) / min_vector[key].att[key] > _jnd[key]:
            if p.att[key] - min_vector[key].att[key] > _jnd[key]:
                is_candy = False
        if is_candy:
            candidate_paths.append(p)
    # TODO: write log data for check
    if len(candidate_paths) == 0:
        print("No path satisfy the JND conditions")

    return candidate_paths


def lex_order(_paths, _order):
    """
        given the order return the ordered paths set
    :param _paths:
    :param _order:
    :return:
    """
    ranked = []
    path_status = [False] * len(_paths)
    for p in _paths:
        p.status = False
    count = 0
    for key in _order:
        print(key)
        if count >= len(_paths):
            continue
        ranked.append(min([l for l in _paths if l.status is False], key=lambda _paths: _paths.att[key]))
        min([l for l in _paths if l.status is False], key=lambda _paths: _paths.att[key]).status = True
        count += 1

    return ranked
    pass


def compare_oder(_paths, _order, _jnd):
    """
        find path order based on the proposed method
    :param _paths:
    :return:
    """
    # step 1: compare JND value with the minimum cost : return candidate path set
    candy_path = get_candidate_path(_paths, _jnd)
    # step 2: given candidate path set, use lex order method to compare
    ranked_path = lex_order(candy_path, _order)

    return ranked_path
    pass

# def lex_oder_jnd(_paths, _order, _jnd):
#