"""
    The script is created to illustrate for the path recommendation example
"""
import pandas as pd
import rankpath


class ParaClass:
    """
        class for the parameters
    """

    def __init__(self, _vot, _votr, _vowait, _vowalk, _w_fare, _w_travel, _w_wait, _w_transfer, _w_walk):
        self.value = {'Travel': _vot,
                      'Transfer': _votr,
                      'Wait': _vowait,
                      'Walk': _vowalk}
        self.weight = {'Fare': _w_fare,
                       'Travel': _w_travel,
                       'Wait': _w_wait,
                       'Transfer': _w_transfer,
                       'Walk': _w_walk}
        self.normalize_weight()

    def normalize_weight(self):
        """
            normalized the weighting parameters
        :return:
        """
        sum_value = 0
        for key in self.weight:
            sum_value += self.weight[key]
        if sum_value > 1:
            for key in self.weight:
                self.weight[key] = self.weight[key] / sum_value
        with open("check_para.csv", "wt") as f:
            for key in self.weight:
                print('{0},{1}'.format("Weight" + key, self.weight[key]), file=f)
            for key in self.value:
                print('{0},{1}'.format("ValueOf" + key, self.value[key]), file=f)


class PathClass:
    """
        define class for path
    """

    def __init__(self, _id, _travel, _fare, _wait, _transfer, _walk):
        self.id = _id
        # att : stands for attributes
        self.att = {'Travel': _travel,
                    'Fare': _fare,
                    'Wait': _wait,
                    'Walk': _walk,
                    'Transfer': _transfer}
        self.cost ={'Weight': -1, 'NonWeight': -1}

    def get_weighted_cost(self, _para: ParaClass):
        """
            get the weighted cost associated with a path
        :param _para:
        :return:
        """
        self.cost['Weight'] = self.att['Fare']* _para.weight['Fare'] \
                             + self.att['Travel'] * _para.value['Travel'] * _para.weight['Travel'] \
                             + self.att['Wait'] * _para.value['Wait'] * _para.weight['Wait'] \
                             + self.att['Transfer'] * _para.value['Transfer'] * _para.weight['Transfer'] \
                             + self.att['Walk'] * _para.value['Walk'] * _para.weight['Walk']

        self.cost['NonWeight'] = self.att['Fare'] \
                                 + self.att['Travel'] * _para.value['Travel'] \
                                 + self.att['Wait'] * _para.value['Wait'] \
                                 + self.att['Transfer'] * _para.value['Transfer'] \
                                 + self.att['Walk'] * _para.value['Walk']


class PasClass:
    """
        define class for passengers
    """

    def __init__(self, _id):
        self.id = _id
        self.paths = []
        self.jnd = {'Fare': -1,
                    'Travel': -1,
                    'Wait': -1,
                    'Walk': -1,
                    'Transfer': -1}
        self.shortest_weight = []
        self.shortest_non_weight = []
        self.order = []
    pass


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


if __name__ == "__main__":
    """
         main program 
    """
    para = read_para()
    paths = read_path()
    for p in paths:
        p.get_weighted_cost(para)
    # check the read path set
    with open("check_path.csv", "wt") as f:
        print("id,fare,travel,wait,transfer,walk,weight_cost,non_weight_cost", file=f)
        for p in paths:
            print("{0},{1},{2},{3},{4},{5},{6},{7}".format(p.id, p.att['Fare'], p.att['Travel'], p.att['Wait'],
                                                           p.att['Transfer'], p.att['Walk'],
                                                           p.cost['Weight'], p.cost['NonWeight']), file=f)

    passengers = set_pas(paths)
    for o in passengers:
        o.shortest_weight = rankpath.shortest(o.paths, 'Weight')
        o.shortest_non_weight = rankpath.shortest(o.paths, 'NonWeight')

    # print suggested path
    with open("RecommandPath.txt", "wt") as f:
        for o in passengers:
            print("Pas={0},shortest_non_weight=(".format(o.id), file=f, end='')
            for p in o.shortest_non_weight:
                print('{0},'.format(p.id), file=f, end='')
            print(')', file=f)
        for o in passengers:
            print("Pas={0},shortest_weight=(".format(o.id), file=f, end='')
            for p in o.shortest_weight:
                print('{0}'.format(p.id), file=f, end='')
            print(')', file=f)

    print("Complete")

    pass
