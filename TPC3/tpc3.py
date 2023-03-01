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

def procByYear(data):
    result = dict()

    for i in data:
        date = int(i['date'][:4])
        result = update(result,date,1)

    return sortDic(result)

def main():
    data = parser("processos.txt")
    result = procByYear(data)
    #print(result)

if __name__ == "__main__":
    main()