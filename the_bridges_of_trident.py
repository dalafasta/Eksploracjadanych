import Orange
from collections import Counter
import random
import math

data = Orange.data.Table("bridges.tab")  # @UndefinedVariable

def someData(data, percentage):
    numberOfElements = int(math.ceil((len(data) * percentage)))
    return  random.sample(data, numberOfElements)

#przykladowe instancje
print("Przykladowe instancje: 10% zbioru")
for x in someData(data, 0.1):
    print(x)
########################





#liste wartosci zmiennej celu i histogram zmiennej celu
print("\n")
attr_var = data.domain.features[-1]

print("Lista wartosci zmiennej celu:")
print(attr_var.values)

print("\n")

print ("Histogram zmiennej celu:")
# pylab.hist([d for d in data if d[attr_var] == x])
# pylab.show()
print ("%-15s %s" % ("Wartosc", "L. wystapien"))
for x in attr_var.values:
    print ("%-15s %d" % (x, len([1 for d in data if d[attr_var] == x])))
    

#######################################################





#liczbe, nazwy i typy atrybutow z podzialem na atrybuty ciagle i dyskretne
print("\n")
contiguous = []
discrete = []
undefined = []

for param in data.domain.features:
    #print(param.varType)
    if param.varType == Orange.feature.Type.Continuous:  # @UndefinedVariable
        contiguous.append(param)
    elif param.varType == Orange.feature.Type.Discrete:  # @UndefinedVariable
        discrete.append(param)
    else:
        undefined.append(param)
        
print("Liczba atrybutow:")   
print("Ciagle: " , len(contiguous))
print("Dyskretne: ",  len(discrete))

print("Nazwy atrybutow:")   
print("Ciagle: " , contiguous)
print("Dyskretne: ",  discrete)
########################################################################



#wartosci srednie (lub modalne) dla kazdego atrybutu
print("\n")
average = lambda xs: sum(xs)/float(len(xs))

def mostCommon(dataList):
    data = Counter(dataList)
    #data.most_common()   # Returns all unique items and their counts
    #data.most_common(1)  # Returns the highest occurring item
    return data.most_common(1)

print ("Wartosci srednie (lub modalne) dla kazdego atrybutu")
for x in data.domain.features:
    if x.varType == Orange.feature.Type.Continuous:  # @UndefinedVariable
        print (x.name, average([d[x] for d in data if not d[x].is_special()]))
    elif param.varType == Orange.feature.Type.Discrete:  # @UndefinedVariable
        print (x.name, mostCommon([d[x].value for d in data])[0][0])

        



#######################################################



#liczba brakujacych wartosci dla kazdego atrybutu
print("\n")
print("Liczba brakujacych wartosci dla kazdego atrybutu")
for x in data.domain.features:
    n_miss = sum(1 for d in data if d[x].is_special())
    #print ("%4.1f%% %s" % (100.*n_miss/len(data), x.name))
    print(x.name, n_miss)



#######################################


#przyklad niewielkiej probki instancji
print("\n")
print("Przyklad niewielkiej probki instancji")


#0.25 means 25% of data
pieceOfData = someData(data, 0.25)
print("Liczba probek:", len(pieceOfData))
for x in pieceOfData:
    print(x)


