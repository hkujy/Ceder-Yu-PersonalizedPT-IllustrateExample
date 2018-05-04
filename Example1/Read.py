
import pandas as pd
from MyClass import PathClass, PasClass, ParaClass
import numpy


def get_path_cost(p, _para: ParaClass):

    """
        get the weighted cost associated with a path
    :param _para:
    :return:
    """
    p.cost['Weight'] = p.att['Fare'] * _para.weight['Fare'] \
                       + p.att['Travel'] * _para.value['Travel'] * _para.weight['Travel'] \
                       + p.att['Wait'] * _para.value['Wait'] * _para.weight['Wait'] \
                       + p.att['Walk'] * _para.value['Walk']*_para.weight['Walk']



    p.cost['NonWeight'] = p.att['Travel'] * _para.value['Travel'] + p.att['Wait'] * _para.value['Wait']


def read_pas(_paths, default_para:ParaClass):
    """
        set the two passengers
    :return:
    """
    pas = [PasClass('A'), PasClass('B')]
    # pas[0].paths = [_paths[0], _paths[1], _paths[2], _paths[3], _paths[4]]
    # list = _paths.copy()
    # self.att = {'Travel': _travel,
    #             'Fare': _fare,
    #             'Wait': _wait,
    #             'Walk': _walk,
    #             'Transfer': _transfer}
    for i in range(0, 4):
        # def __init__(self, _id, _travel, _fare, _wait, _transfer, _walk):
        pas[0].paths.append(PathClass(_paths[i].id,_paths[i].att['Travel'], _paths[i].att['Fare'], _paths[i].att['Wait'], _paths[i].att['Transfer'],_paths[i].att['Walk']))
        pas[1].paths.append(PathClass(_paths[i].id,_paths[i].att['Travel'], _paths[i].att['Fare'], _paths[i].att['Wait'], _paths[i].att['Transfer'],_paths[i].att['Walk']))
        # pas[1].paths.append(ParaClass(_paths[i].id,_paths[i].travel, _paths[i].fare, _paths[i].wait, _paths[i].transfer,_paths[i].walk))
    # pas[1].paths = list(_paths)
    # pas[0].paths = list(_paths)
        # pas[1].paths.append(_paths[i])
    # pas[0].paths = [_paths[0], _paths[1], _paths[2], _paths[3]]
    # pas[1].paths = [_paths[0], _paths[1], _paths[2], _paths[3], _paths[4]]
    # pas[1].paths = [_paths[0], _paths[1], _paths[2], _paths[3]]
    # pas[1].paths = [_paths[5], _paths[6], _paths[7]]
    # data = pd.read_csv('Order.csv')
    # num_data_row = data.shape[0]
    # for i in range(0, num_data_row):
    #     pas[0].order.append(data['A'][i])
    #     pas[1].order.append(data['B'][i])

    # data_weight = pd.read_csv('Pas_weight.csv', index_col=0)
    data_weight = pd.read_excel('Data.xlsx', 'PasWeight', index_col=0)
    # data_jnd_per = pd.read_csv('Jnd_percentage.csv', index_col=0)
    data_jnd_per = pd.read_excel('Data.xlsx', 'JndPer', index_col=0)
    # data_jnd_abs = pd.read_csv('Jnd_abs.csv', index_col=0)
    data_jnd_abs = pd.read_excel('Data.xlsx', 'JndAbs', index_col=0)
    for i in range(0, 2):
        if i == 0:
            name = 'A'
        if i == 1:
            name = 'B'
        pas[i].jnd = {'Fare': data_jnd_per[name]['Fare'],
                      'Travel': data_jnd_per[name]['Travel'],
                      'Wait': data_jnd_per[name]['Wait'],
                      'Transfer': data_jnd_per[name]['Transfer'],
                      'Walk': data_jnd_per[name]['Walk']}
        pas[i].jnd_abs = {'Fare': data_jnd_abs[name]['Fare'],
                          'Travel': data_jnd_abs[name]['Travel'],
                          'Wait': data_jnd_abs[name]['Wait'],
                          'Transfer': data_jnd_abs[name]['Transfer'],
                          'Walk': data_jnd_abs[name]['Walk']}
        _w_fare = data_weight[name]['WeightFare']
        _w_travel = data_weight[name]['WeightTravel']
        _w_wait = data_weight[name]['WeightWait']
        _w_transfer = data_weight[name]['WeightTransfer']
        _w_walk = data_weight[name]['WeightWalk']
        pas[i].para.value = default_para.value
        pas[i].para.weight = {'Fare': _w_fare,
                              'Travel': _w_travel,
                              'Wait': _w_wait,
                              'Transfer': _w_transfer,
                              'Walk': _w_walk}
        pas[i].para.normalize_weight()
        for p in pas[i].paths:
            get_path_cost(p, pas[i].para)

            # p.get_cost(pas[i].para)
        # pas[i].update_path_cost()
        pas[i].update_oder()

    return pas


def read_path():
    """
        read path cost
    :return:
    """
    # data = pd.read_csv('PathCost.csv')
    data = pd.read_excel('Data.xlsx', 'PathCost')

    num_data_row = data.shape[0]
    path = []
    _id = 0
    for p in range(0, num_data_row):
        _id += 1
        _fare = data['Fare'][p]
        _travel = data['Time'][p]
        _wait = data['Wait'][p]
        _transfer = data['Transfer'][p]
        _walk = data['Walk'][p]
        path.append(PathClass(_id, _travel, _fare, _wait, _transfer, _walk))

    return path


def read_para():
    """
        function to read para class data
    """

    # data = pd.read_csv('Para.csv', header=None, index_col=0)
    data = pd.read_excel('Data.xlsx', 'Para')

    # _vot = data[1]['ValueOfTravel']
    _vot = data['Value'][0]
    _vowait = data['Value'][1]
    _votr = data['Value'][2]
    _vowalk = data['Value'][3]
    _w_fare = data['Value'][4]
    _w_travel = data['Value'][5]
    _w_transfer = data['Value'][6]
    _w_wait = data['Value'][7]
    _w_walk = data['Value'][8]

    para = ParaClass()
    para.value = {'Travel': _vot,
                  'Transfer': _votr,
                  'Wait': _vowait,
                  'Walk': _vowalk}
    para.weight = {'Fare': _w_fare,
                   'Travel': _w_travel,
                   'Wait': _w_wait,
                   'Transfer': _w_transfer,
                   'Walk': _w_walk}

    para.normalize_weight()

    return para