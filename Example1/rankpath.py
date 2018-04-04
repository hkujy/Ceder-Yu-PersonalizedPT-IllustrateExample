"""
    This is to rank different paths
"""


def shortest(_paths, type:str):
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


def compare_oder(_paths, _order, _jnd):
    """
        find path order based on the proposed method
    :param _paths:
    :return:
    """
    # step 1: compare JND value with the minimum cost : return candidate path set
    # step 2: given candidate path set, use lex order method to compare



    pass