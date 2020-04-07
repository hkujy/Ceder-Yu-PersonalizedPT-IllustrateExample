__author__ = "Yu Jiang, DTU"
__email__ = "yujiang@dtu.dk"
"""
    The script is created to illustrate for the path recommendation example
"""
import rank_path
from read import read_para, read_path, read_pas
import classes
import output
import matplotlib.pyplot as plt

def two_pas_case(paths, default_para):
    """
        Two passeners with different preference are created
    :return:
    """
    passengers = read_pas(paths, default_para)
    for pas in passengers:
        pas.order_routes()
    # print suggested path
    output.pas(passengers)
    output.recommend_path(passengers)
    output.check_para(passengers)

    Pas_A_Sp = passengers[0].shortest_paths[0].id
    Pas_A_Sp = passengers[1].shortest_paths[0].id
    
    Pas_A_wp=[]
    Pas_B_wp=[]
    for p in passengers[0].shortest_weighted_paths:
        Pas_A_wp.append(p.id)
    for p in passengers[1].shortest_weighted_paths:
        Pas_B_wp.append(p.id)

    Pas_A_op = []
    Pas_B_op = []

    for p in range(0,len(passengers[0].ordered_paths)):
        Pas_A_op.append(passengers[0].ordered_paths[p][0].id)
    for p in range(0,len(passengers[1].ordered_paths)):
        Pas_B_op.append(passengers[1].ordered_paths[p][0].id)

    data=[['Shortest Path',Pas_A_Sp,Pas_A_Sp],['Weighted Shortest Path',Pas_A_wp,Pas_B_wp],['Lex Ordered Path',Pas_A_op,Pas_B_op]]
    table = plt.table(cellText=data, colLabels=['Method', 'Pas_A','Pas_B'], loc='center', 
                  cellLoc='center', colColours=[ '#F3CC32','#2769BD', '#DC3735'])
    table.auto_set_font_size(False)

    plt.axis('off')
    plt.show()




if __name__ == "__main__":
    """
         main program 
    """
    # step 1: read over parameters and path information
    default_para = read_para()
    paths = read_path()
    print("------------Start------------")
    two_pas_case(paths, default_para)
    print("------------Cheers------------")
    pass