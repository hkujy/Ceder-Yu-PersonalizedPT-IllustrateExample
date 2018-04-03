"""
    This is to rank different paths
"""


def shortest(_paths, rank_weighted: bool):
    # print("Before Sort")
    # for p in _paths:
    #     print(p.id)
    if rank_weighted:
        sort_path = sorted(_paths, key=lambda _paths: _paths.cost_weighted)
    else:
        sort_path = sorted(_paths, key=lambda _paths: _paths.cost_non_weighted)
    # print("After Sort")
    # for p in sort_path:
    #     print(p.id)
    print("Complete shortest path ranking")

    return sort_path

    pass


