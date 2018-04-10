"""
    This is to rank different paths
"""


def sort_path(_paths, sort_type: str):
    """
        sort the path based on either weighted or non weighted path cost
    :param _paths:
    :param sort_type:
    :return:
    """
    return sorted(_paths, key=lambda _paths: _paths.cost[sort_type])
    pass


def get_candidate_path(_paths, _jnd):
    """
        get the candidate set of paths
        where each attribute is within the set
    :param _paths:
    :param _jnd:
    :return:
    """
    # step 1: obtain the minimum value for each cost attributes
    min_vector = {'Travel': 100000, 'Fare': 100000, 'Wait': 10000, 'Transfer': 10000}
    for key in min_vector:
        min_vector[key] = min(_paths, key=lambda _paths: _paths.att[key])
    with open("check_min.csv","wt") as f:
        print("Key,MinVal", file=f)
        for key in min_vector:
            print("{0},{1}".format(key, min_vector[key].att[key]), file=f)

    # step 2: compare the cost attributes with the minimum one
    candidate_paths = []
    for p in _paths:
        is_candy = True
        for key in min_vector:
            # if p.att[key] - min_vector[key].att[key] > _jnd[key]:
            if p.att[key] > _jnd[key]:
                is_candy = False
                p.isCandy = False
        if is_candy:
            candidate_paths.append(p)
            p.isCandy = True
    # TODO: write log data for check
    if len(candidate_paths) == 0:
        print("No path satisfy the JND conditions")
    return candidate_paths


def lex_order(_paths, _order, _jnd):
    """
        given the order return the ordered paths set
    :param _paths:
    :param _order:
    :return:
    """
    ranked = []
    # path_status = [False] * len(_paths)
    for p in _paths:
        p.status = False
    count = 0

    min_vector = {'Travel': 100000, 'Fare': 100000, 'Wait': 10000}
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



        # # add the path that already compaed based on the status
        # ranked.append(min([l for l in _paths if l.status is False], key=lambda _paths: _paths.att[key]))
        # # mark the selected path status to be False
        # min([l for l in _paths if l.status is False], key=lambda _paths: _paths.att[key]).status = True
        # count += 1

    return rankedpath
    pass


def compare_oder(_paths, _order, _jnd_abs, _jnd_percentage):
    """
        find path order based on the proposed method
    :param _paths:
    :return:
    """
    # step 1: compare JND value with the minimum cost : return candidate path set
    candy_path = get_candidate_path(_paths, _jnd_abs)
    # step 2: given candidate path set, use lex order method to compare
    ranked_path = lex_order(candy_path, _order, _jnd_percentage)

    return ranked_path
    pass

# def lex_oder_jnd(_paths, _order, _jnd):
#