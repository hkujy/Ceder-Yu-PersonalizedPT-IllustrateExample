import random
import rank_path
import pandas as pd
class ParaClass:
    """
        parameters  class
    """
    # define ini function for different input parameters
    def __init__(self):
        self.value = {'Fare': -999, 'Travel': -999, 'Comfort':-999}
        self.weight = {'Fare': -999, 'Travel': -999, 'Comfort':-999}
        self.jnd_per = {'Fare': -999, 'Travel': -999, 'Comfort':-999}
        self.jnd_abs ={'Fare': -999, 'Travel': -999, 'Comfort': -999}

        # read default jnd_per and jnd_abs values
        data = pd.read_excel('Data.xlsx', 'default_Jnd', index_col=0)

        self.jnd_abs = {'Fare': data['Abs']['Fare'],
                      'Travel': data['Abs']['Travel'],
                      'Comfort': data['Abs']['Comfort']}
        self.jnd_per = {'Fare': data['Per']['Fare'],
                      'Travel': data['Per']['Travel'],
                      'Comfort': data['Per']['Comfort']}
        self.value = {'Fare': data['value']['Fare'],
                    'Travel': data['value']['Travel'],
                    'Comfort': data['value']['Comfort']}

        self.weight = {'Fare': data['weight']['Fare'],
                    'Travel': data['weight']['Travel'],
                    'Comfort': data['weight']['Comfort']}

class PathClass:
    """
        define class for path
    """

    def __init__(self, _id, _travel, _fare, _comfort):
        self.id = _id
        # att : stands for attributes
        self.att = {'Travel': _travel, 'Fare': _fare,'Comfort':_comfort}
        self.cost ={'Weight': -1, 'NonWeight': -1}
        self.status = False   # Whether the path has been checked in the ordering method
        self.isAcceptable = True   # Whether the paths is a candidate/acceptable path

    def get_cost(self, _para: ParaClass):
        """
            get the weighted cost associated with a path
        :param _para:
        :return:
        """
        self.cost['Weight'] = self.att['Fare']* _para.weight['Fare'] \
                             + self.att['Travel'] * _para.value['Travel'] * _para.weight['Travel'] \
                             + self.att['Comfort'] * _para.value['Comfort'] * _para.weight['Comfort']

        self.cost['NonWeight'] = self.att['Fare'] \
                                 + self.att['Travel'] * _para.value['Travel'] \
                                 + self.att['Comfort'] * _para.value['Comfort']

    def output(self):
        """
            define ouput the path
        :return:
        """
        pass

class PasClass:
    """
        passenger class
    """
    def __init__(self, _id, _paths=[]):
        self.id = _id
        self.paths = []
        self.order = ['Fare', 'Travel', 'Comfort']
        self.jnd = {'Fare': -1, 'Travel': -1, 'Comfort': -1}
        self.acceptable = {'Fare': -1, 'Travel': -1, 'Comfort': -1}

        self.ordered_paths = []
        self.shortest_paths = []
        self.shortest_weighted_paths = []

        self.para = ParaClass()
        if len(_paths) > 0:
            for p in range(0, len(_paths)):
                self.paths.append(PathClass(_paths[p].id,_paths[p].att['Travel'],
                                            _paths[p].att['Fare'], _paths[p].att['Comfort']))

    def update_path_cost(self):
        """
            update path cost based on the input weighing parameters
        :return:
        """
        for i in range(0, len(self.paths)):
            self.paths[i].get_cost(self.paths[i],self.para)


    def update_oder(self):
        """
            update order list based on the weighting parameter
        :return:
        """
        self.order = sorted(self.order, reverse=True, key=lambda item: self.para.weight[item])

    def order_routes(self):
        self.ordered_paths = []
        """
            process the computation for one passenger
        :return:
        """
        self.shortest_weighted_paths = rank_path.sort_path(self.paths, 'Weight')
        self.shortest_paths = rank_path.sort_path(self.paths, 'NonWeight')
        self.ordered_paths = rank_path.lex_oder(self.paths, self.order, self.acceptable, self.jnd)

    def print_path_screen(self, print_case ="all"):
        """

            print the passengers' path on scree
        :return:
        """
        # print shortest path
        if print_case == "all" or print_case == "shortest":
            num = 1
            max_num = len(self.paths)
            print("Pas={0},shortest_non_weight=(".format(self.id), end=',')
            for p in self.shortest_paths:
                if num < max_num:
                    print('{0},'.format(p.id), end=',')
                else:
                    print('{0})'.format(p.id))
                num += 1
        # print weighted path
        if print_case == "all" or print_case == "weighted":
            num = 1
            max_num = len(self.paths)
            print("Pas={0},shortest_weight=(".format(self.id), end='')
            for p in self.shortest_weighted_paths:
                if num > max_num:
                    continue
                if num < max_num:
                    print('{0},'.format(p.id), end='')
                else:
                    print('{0})'.format(p.id) )
                num += 1
        # print ordered path
        if print_case == "all" or print_case == "ordered":
            num = 1
            max_num = len([ps for ps in self.paths if ps.isCandy is True])
            print("Pas={0},ordered_path=(".format(self.id), end='')
            for p in self.ordered_paths:
                if num > max_num:
                    continue
                if num < max_num:
                    print('{0},'.format(p[0].id),end='')
                else:
                    print('{0})'.format(p[0].id))
                num += 1


    def print_path_file(self, print_case ="all"):
        """

            print the passengers' path on scree
        :return:
        """
        # print shortest path
        with open(".\OutPut\PathComb.txt", "a") as f:
            if print_case == "all" or print_case == "shortest":
                num = 1
                max_num = len(self.paths)
                print("Pas={0},shortest_non_weight=(".format(self.id), end=',', file=f)
                for p in self.shortest_paths:
                    if num < max_num:
                        print('{0},'.format(p.id), end=',', file=f)
                    else:
                        print('{0})'.format(p.id),file=f)
                    num += 1
            # print weighted path
            if print_case == "all" or print_case == "weighted":
                num = 1
                max_num = len(self.paths)
                print("Pas={0},shortest_weight=(".format(self.id), end='', file=f)
                for p in self.shortest_weighted_paths:
                    if num > max_num:
                        continue
                    if num < max_num:
                        print('{0},'.format(p.id), end='',file=f)
                    else:
                        print('{0})'.format(p.id), file=f)
                    num += 1

        # print ordered path
            if print_case == "all" or print_case == "ordered":
                num = 1
                max_num = len([ps for ps in self.paths if ps.isCandy is True])
                print("Pas={0},ordered_path=(".format(self.id), end='', file=f)
                for p in self.ordered_paths:
                    if num > max_num:
                        continue
                    if num < max_num:
                        print('{0},'.format(p[0].id),end='', file=f)
                    else:
                        print('{0})'.format(p[0].id),file=f)
                    num += 1
    pass
