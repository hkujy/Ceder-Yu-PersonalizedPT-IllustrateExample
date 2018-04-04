

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