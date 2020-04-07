
import pandas as pd
from classes import PathClass, PasClass, ParaClass


def get_path_cost(p, _para: ParaClass):
    """
        get the weighted cost associated with a path
    Weight : Weighted Cost 
    NonWeight ： Non weighted cost, only the travel time/ shortest path
    """
    p.cost['Weight'] = p.att['Fare'] * _para.weight['Fare'] \
                       + p.att['Travel'] * _para.value['Travel'] * _para.weight['Travel'] \
                       + p.att['Comfort'] * _para.value['Comfort']*_para.weight['Comfort']

    p.cost['NonWeight'] = p.att['Travel'] * _para.value['Travel'] + p.att['Fare']


def read_pas(_paths, default_para:ParaClass):
    """
        set the two passengers
    :return:
    """
    pas = [PasClass('A'), PasClass('B')]
    # each passenger has all 4 path as options
    for i in range(0, 4):
        pas[0].paths.append(PathClass(_paths[i].id,_paths[i].att['Travel'], _paths[i].att['Fare'], _paths[i].att['Comfort']))
        pas[1].paths.append(PathClass(_paths[i].id,_paths[i].att['Travel'], _paths[i].att['Fare'], _paths[i].att['Comfort']))

    data_weight = pd.read_excel('Data.xlsx', 'PasWeight', index_col=0)
    data_jnd_per = pd.read_excel('Data.xlsx', 'JndPer', index_col=0)
    data_acceptable = pd.read_excel('Data.xlsx', 'Acceptable', index_col=0)

    for i in range(0, 2):
        if i == 0:
            name = 'A'
        if i == 1:
            name = 'B'
        pas[i].jnd = {'Fare': data_jnd_per[name]['Fare'], 'Travel': data_jnd_per[name]['Travel'], 'Comfort': data_jnd_per[name]['Comfort']}
        pas[i].acceptable = {'Fare': data_acceptable[name]['Fare'], 'Travel': data_acceptable[name]['Travel'], 'Comfort': data_acceptable[name]['Comfort']}

        _w_fare = data_weight[name]['WeightOfFare']
        _w_travel = data_weight[name]['WeightOfTravel']
        _w_comfort = data_weight[name]['WeightOfComfort']

        pas[i].para.value = default_para.value
        pas[i].para.weight = {'Fare': _w_fare,
                              'Travel': _w_travel,
                              'Comfort': _w_comfort}
        for p in pas[i].paths:
            get_path_cost(p, pas[i].para)
        pas[i].update_oder()

    return pas


def read_path():
    """
        read path cost
    """
    data = pd.read_excel('Data.xlsx', 'PathCost')
    num_data_row = data.shape[0]
    path = []
    _id = 0
    for p in range(0, num_data_row):
        _id += 1
        _fare = data['Fare'][p]
        _travel = data['TravelTime'][p]
        _comfort = data['Comfort'][p]
        path.append(PathClass(_id, _travel, _fare, _comfort))

    return path


def read_para():
    """
        function to read para class data
    """
    # read data from excel
    data = pd.read_excel('Data.xlsx', 'Para')
    value_of_travel = data['Value'][0]
    value_of_comfort= data['Value'][1]
    weight_of_fare = data['Value'][2]
    weight_of_travel = data['Value'][3]
    weight_of_comfort = data['Value'][4]

    para = ParaClass()
    para.value = {'Travel': value_of_travel,
                  'Comfort': value_of_comfort}
    para.weight = {'Fare': weight_of_fare,
                   'Travel': weight_of_travel,
                   'Comfort': weight_of_comfort}

    return para