import re
import statistics

def parser(file):
    f = open(file)
    data = []

    for line in f:
        data.append(line.rstrip().split(','))

    f.close()    
    return data


def toDict(data):
    result = []
    header = []

    difList = []
    difListInt = []

    act = 0

    needle = -1
    needleInterval = -1

    for i in data[0]:
        if i != "":
            header.append(i)

    errors = []
    for i in range(len(header)):
        if "}" in header[i] and header[i-1][-1].isdigit():
            errors.append(header[i])
            header[i-1] += "," + header[i]

    for i in errors:
        header.remove(i)

    data.pop(0)

    for person in data:
        dic = {}
        j = 0
        for i in header:
            r1 = re.search(r'[A-Za-z]+{([0-9]+)}',i)
            r2 = re.search(r'[A-Za-z]+{([0-9]+),([0-9]+)}',i)
            op = re.search(r'([A-Za-z]+){([0-9]+,*[0-9]*)}::([A-Za-z]+)',i)

            if r1 != None:
                i = re.sub(r'{\d+}',"",i)
                needle = i
                num = int(r1.group(1))
                for k in range(j,j+num):
                    difList.append(int(person[k]))

            if r2 != None:
                i = re.sub(r'{\d+,\d+}',"",i)
                needleInterval = i
                min = int(r2.group(1))
                max = int(r2.group(2))
                for k in range(j,j+(max)):
                    if(person[k]!= ""):
                        difListInt.append(int(person[k]))
                j += max-1

            if op != None:
                if op.group(3) == "sum":
                    i = op.group(1) + "_sum"
                    if difList != []:
                        soma = sum(difList)
                    elif difListInt != []:
                        soma = sum(difListInt)
                    dic[i] = soma
                elif op.group(3) == "media":
                    i = op.group(1) + "_media"
                    if difList != []:
                        media = statistics.mean(difList)
                    elif difListInt != []:
                        media = statistics.mean(difListInt)
                    dic[i] = media
            else:
                if i == needle:
                    dic[i] = difList
                elif i == needleInterval:
                    dic[i] = difListInt
                else:
                    dic[i] = person[j]
            difList = []
            difListInt = []
            j+= 1
        result.append(dic)
        
    return result

def json(result, name):
    file = open(name,"w")

    fileContent = "[\n"
    indexList = -1

    for dic in result:
        indexList += 1
        fileContent += "    {\n"
        indexDic = -1
        for key in dic:
            indexDic += 1
            if indexDic == len(dic)-1:
                if type(dic[key]) in [list,int,float]:
                    fileContent += f'       "{key}": {dic[key]}\n'
                else:
                    fileContent += f'       "{key}": "{dic[key]}"\n'
            else:
                if type(dic[key]) in [list,int,float]:
                    fileContent += f'       "{key}": {dic[key]},\n'  
                else:
                    fileContent += f'       "{key}": "{dic[key]}",\n'
        if indexList == len(result)-1:
            fileContent += "    }\n"
        else:
            fileContent += "    },\n"
    fileContent += "]\n"

    file.write(fileContent)
    file.close()


def main():
    file1 = parser("alunos.csv")
    file2 = parser("alunos2.csv")
    file3 = parser("alunos3.csv")
    file4 = parser("alunos4.csv")
    file5 = parser("alunos5.csv")
    json(toDict(file1),"alunos.json")
    json(toDict(file2),"alunos2.json")
    json(toDict(file3),"alunos3.json")
    json(toDict(file4),"alunos4.json")
    json(toDict(file5),"alunos5.json")


if __name__ == "__main__":
    main()