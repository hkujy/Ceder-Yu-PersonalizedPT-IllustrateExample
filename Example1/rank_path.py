"""
    This is to rank different paths
"""

def sort_path(_paths, sort_type: str):
    """
        sort the path based on either weighted or non weighted path cost
        when sort_type = non weighted, it refers to the shortest path
    :param _paths:
    :param sort_type:
    :return:
    """
    return sorted(_paths, key=lambda _paths: _paths.cost[sort_type])


def get_acceptable_paths(_paths, _jnd):
    """
        get the candidate acceptable set of paths
        where each attribute is within the set
    :param _paths:
    :param _jnd:
    :return:
    """
    # step 1: obtain the minimum value for each cost attributes
    min_vector = {'Travel': 100000, 'Fare': 100000, 'Comfort': 10000}
    for key in min_vector:
        min_vector[key] = min(_paths, key=lambda _paths: _paths.att[key])
    with open(".\OutPut\check_min.csv","wt") as f:
        print("This file checks the minimum value of each attributes", file=f) 
        print("Key,MinVal", file=f)
        for key in min_vector:
            print("{0},{1}".format(key, min_vector[key].att[key]), file=f)

    # step 2: compare the cost attributes with the minimum one
    acceptable_paths = []
    for p in _paths:
        is_acceptable = True
        for key in min_vector:
            if p.att[key] > _jnd[key]:
                is_acceptable = False
                p.isAcceptable = False
        if is_acceptable:
            acceptable_paths.append(p)
            p.isAcceptable = True
    if len(acceptable_paths) == 0:
        print("No path satisfy the JND conditions")
    return acceptable_paths


def lex_order_sort(_paths, _order, _jnd):
    """
        given the order return the ordered paths set
    :param _paths:
    :param _order:
    :return:
    """
    ranked = []
    for p in _paths:
        p.status = False
    count = 0

    min_vector = {'Travel': 100000, 'Fare': 100000, 'Comfort': 10000}
    for key in min_vector:
        min_vector[key] = min(_paths, key=lambda _paths: _paths.att[key])

    ranked = []
    for key in _order:
        if count >= len(_paths):
            continue
        count += 1
        jnd_set = {}
        for p in _paths:
            if p.id not in ranked and p.att[key] - min_vector[key].att[key] > min_vector[key].att[key] * _jnd[key]:
                jnd_set.update({p.id: p.att[key]})

        if len(jnd_set) > 0:
            sort_set = sorted(jnd_set.values(), reverse=True)
            for val in sort_set:
                for p in jnd_set:
                    if jnd_set[p] == val:
                        ranked.insert(0, p)

    for p in _paths:
        if p.id not in ranked:
            ranked.insert(0, p.id)

    rankedpath = []
    for pi in ranked:
        rankedpath.append([ps for ps in _paths if ps.id == pi])

    return rankedpath


def lex_oder(_paths, _order, _jnd_abs, _jnd_percentage):
    """
        find path order based on the proposed method
    :param _paths:
    :return:
    """
    # step 1: compare JND value with the minimum cost : return candidate path set
    acceptable_paths = get_acceptable_paths(_paths, _jnd_abs)
    # step 2: given candidate path set, use lex order method to compare
    ranked_path = lex_order_sort(acceptable_paths, _order, _jnd_percentage)

    return ranked_path