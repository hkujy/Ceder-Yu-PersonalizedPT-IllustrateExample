"""
    The script is created to illustrate for the path recommendation example
"""
import rankpath
from Read import read_para, read_path, read_pas
import MyOutPut

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

    MyOutPut.pas(passengers)
    MyOutPut.recommend_path(passengers)
    MyOutPut.check_para(passengers)


    print("Complete")


    pass
