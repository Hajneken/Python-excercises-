
def sortNumbers(weights, condition):
    if condition == "ASC":
        for i in range(1,len(weights)):       # tridici algorit=mus selection sort
            while (weights[i-1] > weights[i] and i> 0): # projizdime cele pole, vnorime while cyklus
                weights[i-1], weights[i] = weights[i], weights[i -1]
                i -= 1
    elif condition == "DESC":
        for i in range(1,len(weights)):       # znovu selection sort, ale tentokrat sestupne
            while (weights[i-1] < weights[i] and i>0):
                weights[i-1], weights[i] = weights[i], weights[i -1]
                i -= 1
    return weights
from operator import itemgetter
 
def sortData(reputation, data, condition):
    l = []
    if len(reputation) != len(data):
        raise ValueError('Invalid input data')
    elif condition == "ASC":
        N = (zip(reputation, data))
        pp = sorted(N, key=itemgetter(0))
        u = [x[1] for x in pp]
        return(u)
    elif condition == "DESC":
        u = (zip(reputation, data))
        pp = sorted(u, key=itemgetter(0), reverse=True)
        #p = sorted(u, reverse = True)
        N = [x[1] for x in pp]
        return(N)
 
print(sortData([2, 3, 4, 4, 5, 19, 2, 1],['Praha', 'Brno', 'Pariz', 'Londyn', 'Bratislava', 'Pelhrimov', 'Jihlava', 'CB'], "ASC"))