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


    passengers = read_pas(paths, default_para)
    for o in passengers:
        print("*********start to compare Passengers {0} ************".format(o.id))
        o.shortest_weight = rankpath.sort_path(o.paths, 'Weight')
        o.shortest_non_weight = rankpath.sort_path(o.paths, 'NonWeight')
        # use absolute jnd_value
        o.ordered_path = rankpath.compare_oder(o.paths, o.order, o.jnd_abs, o.jnd)
    # print suggested path

    MyOutPut.pas(passengers)
    MyOutPut.recommend_path(passengers)
    MyOutPut.check_para(passengers)


    print("Complete")


    pass
