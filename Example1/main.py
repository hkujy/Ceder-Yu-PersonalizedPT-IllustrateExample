"""
    The script is created to illustrate for the path recommendation example
"""
import rankpath
from Read import read_para, read_path, read_pas

if __name__ == "__main__":
    """
         main program 
    """
    default_para = read_para()
    paths = read_path()
    # check the read path set
    with open("check_path.csv", "wt") as f:
        print("id,fare,travel,wait,transfer,walk,weight_cost,non_weight_cost", file=f)
        for p in paths:
            print("{0},{1},{2},{3},{4},{5}".format(p.id, p.att['Fare'], p.att['Travel'], p.att['Wait'],
                                                           p.att['Transfer'], p.att['Walk']), file=f)

    passengers = read_pas(paths, default_para)
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
    with open("check_para.csv", "wt") as f:
        print("Weight,A,B", file=f)
        keys = passengers[0].para.weight.keys()
        for r in keys:
            print("{0},{1},{2}".format(r, passengers[0].para.weight[r], passengers[1].para.weight[r]), file=f)

    with open("result_paths.csv", "wt") as f:
        print("Rank,A,B,non_weight,weight", file=f)
        nump = len(passengers[0].ordered_path)
        for p in range(0, nump):
            print("{0},{1},{2},{3},{4}".
                  format(p, passengers[0].ordered_path[p].id, passengers[1].ordered_path[p].id,
                         passengers[0].ordered_path[p].cost['NonWeight'],
                         passengers[1].ordered_path[p].cost['Weight']), file=f)


    print("Complete")


    pass
