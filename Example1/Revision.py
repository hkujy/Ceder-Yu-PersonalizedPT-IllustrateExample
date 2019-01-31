"""

    The revision is the main script for revising the manuscript for the second round submission

"""
from MyClass import PasClass
import  TestOnePara as test

def revision_main(_paths, _para):
    """

    :param _paths:  input path
    :param _para:  input default parameters
    :return:
    """

    num_pas = 10  # number of passengers to be tested
    # step1, generate passenger
    weight_cases = []
    weight_paths = []

    open(".\OutPut\PathComb.txt","w").close()
    with open(".\OutPut\PathComb.txt", "wt") as f:
        print("results for addressing the reviewers' comments", file=f)

    for id in range(0, num_pas):
        pas = PasClass(id, _paths)
        pas.para.gen_random_weight()
        weight_cases.append(pas.para.weight)
        test.main(pas)
        weight_paths.append(pas.shortest_weight)
        pas.print_path_screen(print_case="weighted")
        pas.print_path_file(print_case="weighted")

