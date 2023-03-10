import matplotlib.pyplot as plt
import numpy as np

def parser(file):
    f = open(file)
    data = []

    for line in f:
        data.append(line.rstrip().split(","))
    
    data.pop(0)
    
    return data

def round (num):
    list = []
    list.append(num)
    my_formatted_list = [ '%.2f' % elem for elem in list ]
    
    return my_formatted_list[0]

def distBySex(data):
    illM = 0
    totalM = 0
    illF = 0
    totalF = 0
    perM = 0
    perF = 0

    info = []

    for line in data:
        if(line[1] == 'M'):
            totalM += 1
            if(line[5] == '1'):
                illM += 1
        else:
            totalF += 1
            if(line[5] == '1'):
                illF += 1
    
    perM = (illM/totalM)*100
    perF = (illF/totalF)*100

    info.append(illM)
    info.append(totalM)
    info.append(perM)
    info.append(illF)
    info.append(totalF)
    info.append(perF)

    return info

def maxMin(data):
    maxC = 0
    maxA = 0

    info = []

    for line in data:
        age = int(line[0])
        if(age>maxA):
            maxA = age
    
        col = int(line[3])
        if(col>maxC):
            maxC = col
    
    info.append(maxA)
    info.append(maxC)

    return info

def ageGroups (maxAge):
    minAge = 30
    
    groups = dict()

    while (minAge <= maxAge):
        groups[minAge] = 0
        minAge += 5
    
    return groups

def colGroups (maxCol):
    minCol = 85

    groups = dict()

    while (minCol <= maxCol):
        groups[minCol] = 0
        minCol += 10
    
    return groups

def distByAge(data):
    maxAge = maxMin(data)[0]
    groups = ageGroups(maxAge)

    for line in data:
        if line[5] == '1':
            age = int(line[0])
            for key in groups:
                if (age >= key and age <= (key+4)):
                    groups[key] += 1
                    break

    return groups

def distByCol(data):
    maxCol = maxMin(data)[1]
    groups = colGroups(maxCol)

    for line in data:
        if line[5] == '1':
            col = int(line[3])
            for key in groups:
                if col >= key and col <= (key + 9):
                    groups[key] += 1
                    break

    return groups

def sexTables(info):
    print()
    print(" >  Distribution of the disease by sex  < \n")
    print("+-----------------------------------------+")
    print("|  Sex  |  Sick  |  Total  |  Percentage  |")
    print("+-----------------------------------------+")
    print("+-----------------------------------------+")
    print("|   M   | {:^6} | {:^7} | {:^12} |".format(info[0],info[1],round(info[2])))
    print("+-----------------------------------------+")
    print("|   F   | {:^6} | {:^7} | {:^12} |".format(info[3],info[4],round(info[5])))
    print("+-----------------------------------------+")

def ageTables(data, groups):
    print("\n")
    print(" >  Distribution of the disease by groups of age  < \n")
    print("+--------------------+")
    print("|   Age   |   Sick   |")
    print("+--------------------+")
    print("+--------------------+")
    for key in groups:
        print("| [{},{}] | {:^8} |".format(key,key+4,groups[key]))
        print("+--------------------+")

def colTables(data, groups):
    print("\n")
    print(" >  Distribution of the disease by groups of cholesterol  < \n")
    print("+--------------------------+")
    print("|  Cholesterol  |   Sick   |")
    print("+--------------------------+")
    print("+--------------------------+")
    for key in groups:
            print("|   [{:^3},{:^3}]   | {:^8} |".format(key,key+9,groups[key]))
            print("+--------------------------+")

            
def sexToGraph(info):
    sexDist = np.array([info[2],info[5]])
    
    mylabels = ["male","female"]
    mycolors = ["blue", "hotpink"]

    plt.pie(sexDist,labels=mylabels, colors=mycolors)
    plt.legend()
    plt.show() 

def main():
    data = parser('myheart.csv')

    sex = distBySex(data)
    age = distByAge(data)
    col = distByCol(data)

    sexTables(sex)
    ageTables(data,age)
    colTables(data,col)

    sexToGraph(sex)

if __name__ == "__main__":
    main()
