import re

valid = ['2e','1e','50c','20c','10c','5c','2c','1c']

def extra(balance):
    coins = [200,100,50,20,10,5,2,1]
    string = 'maq: "troco = "'

    for i in coins:
        n = balance//i
        balance %= i
        if n>0:
            if i == 200 or i == 100:
                string += f'{n}x{i//100}e,'
            else:
                string += f'{n}x{i:02d}c,'
    string += ' Volte sempre!"'
    string = re.sub(r', V','; V',string)

    print(string)


def main():
    operation = ""
    balance = 0

    operation = input()
    while(operation != "LEVANTAR"):
        operation = input()
    print('maq: "Introduza moedas."')
    while operation != "POUSAR" and operation != "ABORTAR":
            flag = 0
            operation = input()
            coins = re.findall(r'[0-9]+[e|c]',operation)
            invalid = []
            for coin in coins:
                if coin not in valid:
                    invalid.append(coin)
                else:
                    value = re.search(r'([0-9]+)([e|c])',coin)
                    x = int(value.group(1))
                    if value.group(2) == 'e':
                        balance += x*100
                    else:
                        balance += x
                flag = 1
            if flag == 1:
                if invalid != []:
                    print(f'maq: " {invalid} - moeda(s) inválida(s); saldo - {balance//100}e{(balance%100):02d}c"')
                else:
                    print(f'maq: "saldo - {balance//100}e{(balance%100):02d}c"')
            op = re.match(r'([A-Z]+)=?([0-9]*)',operation)
            num = op.group(2)
            if num != "":
                if len(num) == 9:
                    if num[:3] == "601" or num[:3] == "641":
                        print('maq: "Esse número não é permitido neste telefone. Queira discar novo número!"')
                    elif num[:1] == '2':
                        if balance > 25:
                            balance -= 25
                            print(f'maq: "saldo - {balance//100}e{(balance%100):02d}c"')
                        else:
                            print(f'maq: "Saldo insuficiente. Saldo - {balance//100}e{(balance%100):02d}c"')
                    elif num[:3] == '800':
                        print(f'maq: "saldo - {balance//100}e{(balance%100):02d}c"')
                    elif num[:3] == '808':
                        if balance > 10:
                            balance -= 10
                            print(f'maq: "saldo - {balance//100}e{(balance%100):02d}c"')
                        else:
                            print(f'maq: "Saldo insuficiente. Saldo - {balance//100}e{(balance%100):02d}c"')
                elif num[:2] == '00':
                    if balance > 150:
                        balance -= 150
                        print(f'maq: "saldo - {balance//100}e{(balance%100):02d}c"')
                    else:
                        print(f'maq: "Saldo insuficiente. Saldo - {balance//100}e{(balance%100):02d}c"')
                else:
                    print(f'maq: "Número inválido. Saldo - {balance//100}e{(balance%100):02d}c"')
    extra(balance)

if __name__ == "__main__":
    main()