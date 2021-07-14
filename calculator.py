import sys
x = input()
while x[0:3] != 'see' and x[0:3] != 'def' and x[0:4] != 'calc':
    if x.lower() == 'quit':
        sys.exit()
    else:
        print('undefined')
        x = input()
dic = {}
while x.lower() != 'quit':
    if x[0:3] == 'def':
        if x.count('=') == 1 and x.count('+') == 0 and x.count('-') == 0 and x.count('*') == 0:
            y = x[3:x.index('=')]
            z = x[x.index('=') + 1:]
            y = y.strip()
            z = z.strip()
            if z.isnumeric() != True:
                print('Error')
            else:
                dic[y] = int(z)
                x = input()
    elif x[0:3] == 'see':
        print(format('Variables', '=^21'))
        dict = list(zip(dic.keys(), dic.values()))
        for k in range(0, len(dict)):
            print(dict[k][0] + ' = ' + str(dict[k][1]))
        print('=' * 21)
        x = input()
    elif x[0:4] == 'calc':
        if x.count('+') + x.count('-') + x.count('*') + x.count('/') != 1:
            print('Error')
            x = input()
        elif x.count('+') == 1:
            a = x[4:x.index('+')]
            a = a.strip()
            b = x[x.index('+') + 1:]
            b = b.strip()
            if a in dic and b in dic:
                print(dic[a] + dic[b])
                x = input()
            else:
                print('Error')
                x = input()
        elif x.count('-') == 1:
            a = x[4:x.index('-')]
            a = a.strip()
            b = x[x.index('-') + 1:]
            b = b.strip()
            if a in dic and b in dic:
                print(dic[a] - dic[b])
                x = input()
            else:
                print('Error')
                x = input()
        elif x.count('*') == 1:
            a = x[4:x.index('*')]
            a = a.strip()
            b = x[x.index('*') + 1:]
            b = b.strip()
            if a in dic and b in dic:
                print(dic[a] * dic[b])
                x = input()
            else:
                print('Error')
                x = input()
        elif x.count('/') == 1:
            a = x[4:x.index('/')]
            a = a.strip()
            b = x[x.index('/') + 1:]
            b = b.strip()
            if a in dic and b in dic:
                c = dic[a] / dic[b]
                if dic[b] == 0:
                    print('Error')
                    x = input()
                else:
                    if c != int(c):
                        print(round(c, 2))
                        x = input()
                    else:
                        print(int(c))
                        x = input()
            else:
                print('Error')
                x = input()
    else:
        print('Error')
        x = input()
if x.lower() == 'quit':
    sys.exit()