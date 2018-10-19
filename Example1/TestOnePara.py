"""
    The purpose of the script is record the test one parameter
    This is created to response to the users
    Input is a set of parameter settings
    output is list of path
"""
import pandas as pd
from MyClass import PathClass, PasClass, ParaClass
from Read import get_path_cost

def main(pas:PasClass):
    """

    :param pas:
    :return:
    """
    for p in pas.paths:
        get_path_cost(p, pas.para)
    pas.jnd_abs = pas.para.jnd_abs
    pas.jnd = pas.para.jnd_per
    pas.update_oder()

    pas.order_routes()




