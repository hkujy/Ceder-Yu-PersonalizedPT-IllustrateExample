"""
    The script is created to illustrate for the path recommendation example
"""
import rankpath
from Read import read_para, read_path, read_pas
import MyOutPut
import Revision as revise

def two_pas_case(paths, default_para):
    """
        This two pas case is the case study for the first version
    :return:
    """
    passengers = read_pas(paths, default_para)

    for o in passengers:
        print("*********start to compare Passengers {0} ************".format(o.id))
        o.order_routes()
    # print suggested path
    MyOutPut.pas(passengers)
    MyOutPut.recommend_path(passengers)
    MyOutPut.check_para(passengers)


if __name__ == "__main__":
    """
         main program 
    """
    # step 1: read over parameters and path information
    default_para = read_para()
    paths = read_path()
    # check the read path set

    print("start the two passenger case")
    # two_pas_case(paths, default_para)

    print("Complete the two passenger case")

    print("Start the revision main case")
    revise.revision_main(paths,default_para)

    print("Complete the revision main case")

    print("Complete")


    pass
