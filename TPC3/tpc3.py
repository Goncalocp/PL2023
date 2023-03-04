import re

def parser(file):
    f = open(file)
    data = []

    for line in f:
        info = re.search(r'(?P<id>\d*)::(?P<date>\d{4}-\d{2}-\d{2})::(?P<names>.+)[::::|.::]', line)
        if info != None:
            dic = info.groupdict()
            data.append(dic)
    #print(data)
    return data

#{'id': '426', 'date': '1890-10-27', 'names': 'Zeferino Pereira Ramos::Serafim Francisco Pereira Ramos::Albina Goncalves:::'}

def update(dic, newkey, value):
    flag = 0
    for key in dic:
        if(key==newkey):
            dic[key] += value
            flag = 1
    
    if (flag == 0):
        dic[newkey] = value

    return dic

def sortDic(dic):

    sorted_keys = sorted(dic.keys())
    sorted_dic = {key:dic[key] for key in sorted_keys}
    
    return sorted_dic

def sortDicByValue(dic):
    sorted_dic = dict( sorted(dic.items(),key=lambda item: item[1],reverse=True))

    return sorted_dic

def getFirst(num, dic):
    newDic = {}
    i = 0
    for key in dic:
        update(newDic,key,dic[key])
        i += 1
        if i >= num:
            break

    return newDic

def procByYear(data):
    result = dict()

    for i in data:
        date = int(i['date'][:4])
        numProc = len(re.findall(r'Proc',i.get('names')))
        result = update(result,date,numProc)

    return sortDic(result)

def namesFreq(data):
    dicFirstNames = dict()
    dicLastNames = dict()

    result = []

    for i in data:
        first_names = re.findall(r'::([A-Z][a-z][a-z]+)\s+[A-Z]',i.get('names'))
        last_names = re.findall(r'[a-z]+\s([A-Z][a-z][a-z]+)[:|,]+',i.get('names'))
        last_names2 = re.findall(r'[a-z]+\s([A-Z][a-z][a-z]+)::',i.get('names'))
        date = i['date'][:4]
        if date[2:4] == '00':
            x = int(date[0:2])
        else:
            x = int(date[0:2])+1
        if x not in dicFirstNames:
            dicFirstNames[x] = dict()
        if x not in dicLastNames:
            dicLastNames[x] = dict()

        if first_names != []:
           for j in first_names:
                dicFirstNames[x] = update(dicFirstNames[x],j,1)

        if last_names != []:
            for k in last_names:
                dicLastNames[x] = update(dicLastNames[x],k,1)

        if last_names2 != []:
            for k in last_names2:
               dicLastNames[x] = update(dicLastNames[x],k,1)
    
    for key in dicFirstNames:
        dicFirstNames[key] = sortDicByValue(dicFirstNames[key])
    
    for key in dicLastNames:
        dicLastNames[key] = sortDicByValue(dicLastNames[key])
                   
    result.append(sortDic(dicFirstNames))
    result.append(sortDic(dicLastNames))
    return result


def relationsFreq(data):
    result = dict()

    for i in data:
        list = re.findall(r'[a-z],([A-Za-z]+\s*[A-Za-z]*)\.[\s][A-Za-z]',i.get('names'))
        if list != []:
            for j in list:
                result = update(result,j,1)

    return sortDic(result)

def json(data):
    file = open("file.json","w")
    fileContent = "[\n"

    for i in range(0,20):
        dic = data[i]
        fileContent += "    {\n"
        for key in dic:
            if key != 'names':
                fileContent += f'        "{key}": "{dic[key]}",\n'
            else:
                fileContent += f'        "{key}": "{dic[key]}"\n'
        if i<19: fileContent += "    },\n"
        else: fileContent += "    }\n"
    fileContent += "]\n"
    file.write(fileContent)
    file.close()

def procByYearTable(result):

    print()
    print(" >  Frequência de processos por ano*  < \n")
    print("+---------------------------+")
    print("|   Ano  |  Nº de processos |")
    print("+---------------------------+")
    print("+---------------------------+")
    for key in result:
        if result[key] > 0:
            print("|  {:^4}  |       {:^4}       |".format(key,result[key]))
            print("+---------------------------+")
    print("* Apenas são apresentados os anos cujo número de processos é superior a 0\n")

def namesFraqTable(result):
    first_names = result[0]
    last_names = result[1]

    print()
    print(" >  Frequência de nomes próprios e apelidos por século  < \n")
    print("+-------------------------------+")
    print("|  Século  |        Nome        |")
    print("+-------------------------------+")
    print("+-------------------------------+")

    for key in first_names:
        dic = getFirst(5,first_names[key])
        i = 1
        for name in dic:
            if i == 3:
                print("|    {:^2}    |{:^12}({:^6})|".format(key,name,dic[name]))
            else:
                print("|          |{:^12}({:^6})|".format(name,dic[name]))
            i += 1
        print("+-------------------------------+")

    print("+-------------------------------+")
    print("|  Século  |       Apelido      |")
    print("+-------------------------------+")
    print("+-------------------------------+")

    for key in last_names:
        dic = getFirst(5,last_names[key])
        i = 1
        for name in dic:
            if i == 3:
                print("|    {:^2}    |{:^12}({:^6})|".format(key,name,dic[name]))
            else:
                print("|          |{:^12}({:^6})|".format(name,dic[name]))
            i += 1
        print("+-------------------------------+")



def relationsFreqTable(result):

    print()
    print(" >  Frequência de vários tipos de relação  < \n")
    print("+----------------------------------+")
    print("|       Relação      |  Frequência |")
    print("+----------------------------------+")
    print("+----------------------------------+")
    for key in result:
        if result[key] > 0:
            print("|{:^20}|    {:^6}   |".format(key,result[key]))
            print("+----------------------------------+")

def main():
    data = parser("processos.txt")
    result1 = procByYear(data)
    procByYearTable(result1)
    namesFraqTable(namesFreq(data))
    result3 = relationsFreq(data)
    relationsFreqTable(result3)
    json(data)
    

if __name__ == "__main__":
    main()