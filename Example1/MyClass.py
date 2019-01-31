import random
import rankpath
import pandas as pd
class ParaClass:
    """
        parameters  class
    """
    # define ini function for different input parameters
    def __init__(self):
        self.value = {'Fare': -999, 'Travel': -999, 'Wait': -999, 'Transfer': -999,'Walk': -999}
        self.weight = {'Fare': -999, 'Travel': -999, 'Wait': -999, 'Transfer': -999, 'Walk': -999}
        self.jnd_per = {'Fare': -999, 'Travel': -999, 'Wait': -999, 'Transfer': -999,'Walk': -999 }
        self.jnd_abs ={'Fare': -999, 'Travel': -999, 'Wait': -999, 'Transfer': -999,'Walk': -999}

        # read default jnd_per and jnd_abs values
        data = pd.read_excel('Data.xlsx', 'default_Jnd', index_col=0)


        self.jnd_abs = {'Fare': data['Abs']['Fare'],
                      'Travel': data['Abs']['Travel'],
                      'Wait': data['Abs']['Wait'],
                      'Transfer': data['Abs']['Transfer'],
                      'Walk': data['Abs']['Walk']}
        self.jnd_per = {'Fare': data['Per']['Fare'],
                      'Travel': data['Per']['Travel'],
                      'Wait': data['Per']['Wait'],
                      'Transfer': data['Per']['Transfer'],
                      'Walk': data['Per']['Walk']}

        self.value = {'Fare': data['value']['Fare'],
                    'Travel': data['value']['Travel'],
                    'Wait': data['value']['Wait'],
                    'Transfer': data['value']['Transfer'],
                    'Walk': data['value']['Walk']}

        self.weight = {'Fare': data['weight']['Fare'],
                    'Travel': data['weight']['Travel'],
                    'Wait': data['weight']['Wait'],
                    'Transfer': data['weight']['Transfer'],
                    'Walk': data['weight']['Walk']}


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
    def gen_random_weight(self):
        """
            The objective of this function is to generate random weighting parameters
        :return:
        """
        random_nums = []
        for j in range(0, len(self.value)):
            random_nums.append(random.random())
        self.weight['Fare'] = random_nums[0]
        self.weight['Travel'] = random_nums[1]
        self.weight['Wait'] = random_nums[2]
        self.weight['Transfer'] = random_nums[3]
        self.weight['Walk'] = random_nums[4]
        self.normalize_weight()

class PathClass:
    """
        define class for path
    """

    def __init__(self, _id, _travel, _fare, _wait, _transfer, _walk):
        self.id = _id
        # att : stands for attributes
        self.att = {'Travel': _travel, 'Fare': _fare, 'Wait': _wait, 'Walk': _walk, 'Transfer': _transfer}
        self.cost ={'Weight': -1, 'NonWeight': -1}
        self.status = False   # Whether the path has been checked in the ordering method
        self.isCandy = True   # Whether the paths is a candidate path

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
        self.jnd = {'Fare': -1, 'Travel': -1, 'Wait': -1, 'Walk': -1, 'Transfer': -1}
        self.jnd_abs = {'Fare': -1, 'Travel': -1, 'Wait': -1, 'Walk': -1, 'Transfer': -1}
        self.shortest_weight = []
        self.shortest_non_weight = []
        self.order = ['Fare', 'Travel', 'Wait', 'Transfer', 'Walk']
        self.ordered_path = []
        self.para = ParaClass()
        self.choice = OutPutClass()
        if len(_paths) > 0:
            for p in range(0, len(_paths)):
                self.paths.append(PathClass(_paths[p].id,_paths[p].att['Travel'],
                                            _paths[p].att['Fare'], _paths[p].att['Wait'],
                                            _paths[p].att['Transfer'],_paths[p].att['Walk']))

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

    def gen_random_weigtht(cls):
        """
            generate random weighting parametes
        :return:
        """
        cls.para.gen_random_weight()


    def order_routes(self):
        """
            process the computation for one passenger
        :return:
        """
        self.shortest_weight = rankpath.sort_path(self.paths, 'Weight')
        self.shortest_non_weight = rankpath.sort_path(self.paths, 'NonWeight')
        # use absolute jnd_value
        self.ordered_path = rankpath.lex_oder(self.paths, self.order, self.jnd_abs, self.jnd)


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
            for p in self.shortest_non_weight:
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
            for p in self.shortest_weight:
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
            for p in self.ordered_path:
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
                for p in self.shortest_non_weight:
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
                for p in self.shortest_weight:
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
                for p in self.ordered_path:
                    if num > max_num:
                        continue
                    if num < max_num:
                        print('{0},'.format(p[0].id),end='', file=f)
                    else:
                        print('{0})'.format(p[0].id),file=f)
                    num += 1
    pass

class OutPutClass:
    """
        TODO: The class is created for store the output
    """

    # include para input
    def __init__(self, _option_para = ParaClass()):
        self.para = _option_para

