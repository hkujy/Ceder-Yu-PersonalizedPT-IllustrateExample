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


def compare_oder(_paths):
    """
        find path order based on the proposed method
    :param _paths:
    :return:
    """
    # Step 1: cmpar

    pass