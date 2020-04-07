from classes import PasClass


def pas(passenger: PasClass):
    """
        print the two passengers
    :return:
    """
    outfile = ".\output\\result_pas_path.csv"
    with open(outfile, "wt") as f:
        print("Pas,Path,Fare,Travel,Comfort,Weight_Fare,Weight_Travel,Weight_Comfort,WeightedCost,NonWeightCost",  file=f)
        for o in passenger:
            for p in o.paths:
                print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}".
                      format(o.id, p.id, p.att['Fare'], p.att['Travel'], p.att['Comfort'], o.para.weight['Fare'],
                             o.para.weight['Travel'], o.para.weight['Comfort'],
                             p.cost['Weight'], p.cost['NonWeight']), file=f)


def recommend_path(passengers: PasClass):
    with open(".\OutPut\RecommendPath.txt", "wt") as f:
        for o in passengers:
            num = 1
            max_num = len(o.paths)
            print("Pas={0},shortest_paths=(".format(o.id), file=f, end='')
            print("Pas={0},shortest_paths=(".format(o.id), end='')
            for p in o.shortest_paths:
                if num < max_num:
                    print('{0},'.format(p.id), file=f, end='')
                    print('{0},'.format(p.id), end='')
                else:
                    print('{0})'.format(p.id), file=f)
                    print('{0})'.format(p.id))
                num += 1
        for o in passengers:
            num = 1
            max_num = len(o.paths)
            print("Pas={0},shortest_weight_paths=(".format(o.id), file=f, end='')
            print("Pas={0},shortest_weight_paths=(".format(o.id), end='')
            for p in o.shortest_weighted_paths :
                if num > max_num:
                    continue
                if num < max_num:
                    print('{0},'.format(p.id), file=f, end='')
                    print('{0},'.format(p.id), end='')
                else:
                    print('{0})'.format(p.id), file=f)
                    print('{0})'.format(p.id))
                num += 1
        for o in passengers:
            num = 1
            max_num = len(o.ordered_paths)
            print("Pas={0},lex_ordered_path=(".format(o.id), file=f, end='')
            print("Pas={0},lex_ordered_path=(".format(o.id), end='')
            for p in o.ordered_paths:
                if p[0].isAcceptable:
                    print('{0},'.format(p[0].id), file=f, end='')
                    print('{0},'.format(p[0].id), end='')
                else:
                    continue
                if num==len(o.ordered_paths):
                    print(')',file=f)
                    print(')')
                num += 1


def check_para(passengers:PasClass):

    with open(".\OutPut\check_para.csv", "wt") as f:
        print("Weight,A,B", file=f)
        keys = passengers[0].para.weight.keys()
        for r in keys:
            print("{0},{1},{2}".format(r, passengers[0].para.weight[r], passengers[1].para.weight[r]), file=f)

