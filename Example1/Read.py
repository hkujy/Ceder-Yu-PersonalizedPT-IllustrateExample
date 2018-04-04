
import pandas as pd
from MyClass import PathClass, PasClass, ParaClass


def set_pas(_paths: PathClass):
    """
        set the two passengers
    :return:
    """
    pas = [PasClass('A'), PasClass('B')]
    data = pd.read_csv('Jnd.csv', index_col=0)
    pas[0].jnd = {'Fare': data['A']['Fare'],
                  'Travel': data['A']['Travel'],
                  'Wait': data['A']['Wait'],
                  'Transfer': data['A']['Transfer'],
                  'Walk': data['A']['Walk']}
    pas[1].jnd = {'Fare': data['B']['Fare'],
                  'Travel': data['B']['Travel'],
                  'Wait': data['B']['Wait'],
                  'Transfer': data['B']['Transfer'],
                  'Walk': data['B']['Walk']}
    pas[0].paths = [_paths[0], _paths[1], _paths[2], _paths[3], _paths[4]]
    pas[1].paths = [_paths[5], _paths[6], _paths[7]]
    data = pd.read_csv('Order.csv')
    num_data_row = data.shape[0]
    for i in range(0, num_data_row):
        pas[0].order.append(data['A'][i])
        pas[1].order.append(data['B'][i])


    return pas


def read_path():
    """
        read path cost
    :return:
    """
    data = pd.read_csv('PathCost.csv')
    num_data_row = data.shape[0]
    path = []
    _id = -1
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

    return ParaClass(_vot, _votr, _vowait, _vowalk, _w_fare, _w_travel, _w_wait, _w_transfer, _w_walk)