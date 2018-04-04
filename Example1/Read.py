
import pandas as pd
from MyClass import PathClass, PasClass, ParaClass


def read_pas(_paths: PathClass, default_para:ParaClass):
    """
        set the two passengers
    :return:
    """
    pas = [PasClass('A'), PasClass('B')]
    pas[0].paths = [_paths[0], _paths[1], _paths[2], _paths[3], _paths[4]]
    pas[1].paths = [_paths[0], _paths[1], _paths[2], _paths[3], _paths[4]]
    # pas[1].paths = [_paths[5], _paths[6], _paths[7]]
    # data = pd.read_csv('Order.csv')
    # num_data_row = data.shape[0]
    # for i in range(0, num_data_row):
    #     pas[0].order.append(data['A'][i])
    #     pas[1].order.append(data['B'][i])

    data_weight = pd.read_csv('Pas_weight.csv', index_col=0)
    data_jnd_per = pd.read_csv('Jnd_percentage.csv', index_col=0)
    data_jnd_abs = pd.read_csv('Jnd_abs.csv', index_col=0)
    for i in range (0, 2):
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
        pas[i].update_path_cost()
        pas[i].update_oder()

    return pas


def read_path():
    """
        read path cost
    :return:
    """
    data = pd.read_csv('PathCost.csv')
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

    data = pd.read_csv('Para.csv', header=None, index_col=0)
    _vot = data[1]['ValueOfTravel']
    _votr = data[1]['ValueOfTransfer']
    _vowait = data[1]['ValueOfWait']
    _vowalk = data[1]['ValueOfWalk']
    _w_fare = data[1]['WeightFare']
    _w_travel = data[1]['WeightTravel']
    _w_wait = data[1]['WeightWait']
    _w_transfer = data[1]['WeightTransfer']
    _w_walk = data[1]['WeightWalk']
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