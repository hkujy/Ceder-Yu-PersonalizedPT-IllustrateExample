

class ParaClass:
    """
        class for the parameters
    """
    def __init__(self):
        self.value = {'Travel': -999,
                      'Transfer': -999,
                      'Wait': -999,
                      'Walk': -999}
        self.weight = {'Fare': -999,
                       'Travel': -999,
                       'Wait': -999,
                       'Transfer': -999,
                       'Walk': -999}


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
        self.status = False   # Whether the path has been checked in the ordering method

    def get_cost(self, _para: ParaClass):
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
        self.jnd_abs = {'Fare': -1,
                        'Travel': -1,
                        'Wait': -1,
                        'Walk': -1,
                        'Transfer': -1}
        self.shortest_weight = []
        self.shortest_non_weight = []
        self.order = ['Fare', 'Travel', 'Wait', 'Transfer', 'Walk']
        self.ordered_path = []
        self.para = ParaClass()

    def update_path_cost(self):
        """
            update path cost based on the input weighing parameters
        :return:
        """
        for p in self.paths:
            p.get_cost(self.para)

    def update_oder(self):
        """
            update order list based on the weighting parameter
        :return:
        """
        self.order = sorted(self.order, reverse=True, key=lambda item: self.para.weight[item])

    pass