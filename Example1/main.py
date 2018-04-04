"""
    The script is created to illustrate for the path recommendation example
"""
import rankpath
from Read import read_para, read_path, set_pas

if __name__ == "__main__":
    """
         main program 
    """
    para = read_para()
    paths = read_path()
    for p in paths:
        p.get_weighted_cost(para)
    # check the read path set
    with open("check_path.csv", "wt") as f:
        print("id,fare,travel,wait,transfer,walk,weight_cost,non_weight_cost", file=f)
        for p in paths:
            print("{0},{1},{2},{3},{4},{5},{6},{7}".format(p.id, p.att['Fare'], p.att['Travel'], p.att['Wait'],
                                                           p.att['Transfer'], p.att['Walk'],
                                                           p.cost['Weight'], p.cost['NonWeight']), file=f)

    passengers = set_pas(paths)
    for o in passengers:
        print("*********start to compare Passengers {0} ************".format(o.id))
        o.shortest_weight = rankpath.shortest(o.paths, 'Weight')
        o.shortest_non_weight = rankpath.shortest(o.paths, 'NonWeight')
        # use absolute jnd_value
        o.ordered_path = rankpath.compare_oder(o.paths, o.order, o.jnd_abs)
    # print suggested path
    with open("RecommandPath.txt", "wt") as f:
        for o in passengers:
            print("Pas={0},shortest_non_weight=(".format(o.id), file=f, end='')
            for p in o.shortest_non_weight:
                print('{0},'.format(p.id), file=f, end='')
            print(')', file=f)
        for o in passengers:
            print("Pas={0},shortest_weight=(".format(o.id), file=f, end='')
            for p in o.shortest_weight:
                print('{0},'.format(p.id), file=f, end='')
            print(')', file=f)
        for o in passengers:
            print("Pas={0}, ordered_path=(".format(o.id), file=f, end='')
            for p in o.ordered_path:
                print('{0},'.format(p.id), file=f, end='')
            print(')', file=f)

    print("Complete")

    pass
