import base64
import math


def asciitrun():
    b = input("请输入ascii待转换: ")
    bres = [int(x) for x in b.split(' ')]
    res = []
    for m in bres:
        res.append(chr(m))
    print(''.join(res))


def bintrun():
    a = int(input("请输入?进制:"))
    b = input("请输入待转换数字: ")
    bres = [x for x in b.split(' ')]
    for i in range(0, len(bres)):
        print(int(bres[i], a), end="")
    print('\n')


def base64trun():
    b = input("请输入待转换Base64:")
    print("base64解码结果是:", end='')
    print(base64.b64decode(b + '=' * (4 - len(b) % 4)))


def morsetrun():
    CODE = {"----.": "9",
            "...-": "V",
            "-.": "N",
            ".-.": "R",
            "-----": "0",
            "---..": "8",
            "--..": "Z",
            "....-": "4",
            "..---": "2",
            ".----": "1",
            "...": "S",
            ".--.": "P",
            "-...": "B",
            "-": "T",
            "..-": "U",
            "...--": "3",
            ".--": "W",
            ".....": "5",
            "--.-": "Q",
            "..": "I",
            "---": "O",
            "--": "M",
            "--...": "7",
            "-.-": "K",
            ".-": "A",
            "-..": "D",
            "--.": "G",
            "-..-": "X",
            ".": "E",
            ".---": "J",
            "-....": "6",
            "-.-.": "C",
            "-.--": "Y",
            "..-.": "F",
            "....": "H",
            ".-..": "L",
            ".-.-.-": ".",
            "..--..": "?",
            "-.-.--": "!",
            "-.--.": "(",
            ".--.-.": "@",
            "---...": ":",
            "-...-": "=",
            "-....-": "-",
            "-.--.-": ")",
            "--..--": ",",
            ".----.": "'",
            "..--.-": "_",
            "...-..-": "$",
            }
    b = input('请输入Morse code: ')
    b = b.strip()
    bres = [x for x in b.split(' ')]
    print('转换结果是:')
    for i in range(0, len(bres)):
        print(CODE[bres[i].upper()], end='')
    print('\n')


def fencetrun():
    a = input("请输入待破解的栅栏密码:")
    a = a.strip()
    num = len(a)  # 字符串的长度
    error = 0
    for m in range(2, num):
        n = int(num / m)
        if num % m == 0:
            print("\n栅栏数:", n)
            for i in range(m):  # 大循环，栅栏行数
                char = ''  # 初始化
                for j in range(i, num, m):  # 小循环, i 字符串a[i],num 循环次数， m 跳步数
                    char = char + a[j]
                print(char, end="")
        elif num % m != 0:
            error = error + 1
            if error == (num - 2):
                print("该密码不是标准的栅栏密码")
    print("\n")


def caesartrun():
    Ciphertext = input("请输入Caesar's cipher:")
    Ciphertext = Ciphertext.strip()
    for i in range(1, 26):
        print(chr(65 + i) + ":", end=" ")
        y = []
        for a in Ciphertext:
            x = ord(a)
            if (65 <= x <= 90):
                x = x + i
                if x > 90:
                    x = x - 90 + 65 - 1
                    y.append(chr(x))
                else:
                    y.append(chr(x))
            elif (97 <= x <= 122):
                x = x + i
                if x > 122:
                    x = x - 122 + 97 - 1
                    y.append(chr(x))
                else:
                    y.append(chr(x))
        end = ''.join(y)
        print(end + "\n")


def Bacontrun():
    CODE = {"aaaaa": "A",
            "aaaab": "B",
            "aaaba": "C",
            "aaabb": "D",
            "aabaa": "E",
            "aabab": "F",
            "aabba": "G",
            "aabbb": "H",
            "abaaa": "I",
            "abaab": "J",
            "ababa": "K",
            "ababb": "L",
            "abbaa": "M",
            "abbab": "N",
            "abbba": "O",
            "abbbb": "P",
            "baaaa": "Q",
            "baaab": "R",
            "baaba": "S",
            "baabb": "T",
            "babaa": "U",
            "babab": "V",
            "babba": "W",
            "babbb": "X",
            "bbaaa": "Y",
            "bbaab": "Z"}
    a = input("请输入Bacon's cipher:").lower()
    a = ''.join([x for x in a if x != " "])
    for i in range(0, len(a), 5):
        print(CODE[a[i:i + 5]], end="")
    print("\n")


def dangputrun():
    DUPU = {'口': '0', '田': '0', '由': '1', '甲': '1', '中': '2', '申': '2', '人': '3', '工': '4',
            '大': '5', '王': '6', '天': '6', '夫': '7', '井': '8', '丰': '8', '羊': '9'}
    b = input('请输入当铺code: ')
    b = b.strip()
    print('转换结果是:')
    for i in range(0, len(b)):
        if(b[i] in DUPU.keys()) == False:
            print(b[i], '不属于当铺密码')
        else:
            print(DUPU[b[i].upper()], end='')
    print('\n')


def Hex():
    dec = int(input("输入数字："))
    print("十进制数为：", dec)
    print("转换为二进制为：", bin(dec))
    print("转换为八进制为：", oct(dec))
    print("转换为十六进制为：", hex(dec))


def unicode():
    print("中文转unicode-请输入待转换的unicode:")
    a = input()
    s = a.encode('utf-8').decode("unicode_escape")
    print(s)


def WWW():
    '''
    WWW型栅栏密码
    '''

    def num(s, n):
        f = len(s) // (n - 1)
        g = len(s) % (n - 1)
        return f, g

    def _list(s, n):
        x, y = num(s, n)
        if y == 0:
            c = [[] for i in range(x + 1)]
            lie = x
        else:
            c = [[] for i in range(x + 2)]
            lie = x + 1
        jk = 0
        if lie % 2 == 0:
            hk = n - y + 1
        else:
            hk = y
        for i in range(1, n + 1):
            for j in range(1, lie + 1):
                if i == 1:
                    if j % 2 != 0:
                        c[j].append(s[jk])
                        jk += 1

                else:

                    if lie % 2 == 0:
                        if y == 0:
                            if i != n:
                                c[j].append(s[jk])
                                jk += 1
                            if i == n:
                                if j % 2 == 0:
                                    c[j].append(s[jk])
                                    jk += 1
                        else:
                            if i != n:
                                if i >= hk:
                                    c[j].append(s[jk])
                                    jk += 1
                            else:
                                if j % 2 == 0:
                                    c[j].append(s[jk])
                                    jk += 1
                    else:
                        if y == 0:
                            if i != n:
                                c[j].append(s[jk])
                                jk += 1
                            if i == n:
                                if j % 2 == 0:
                                    c[j].append(s[jk])
                                    jk += 1
                        else:
                            if i <= hk:
                                c[j].append(s[jk])
                                jk += 1
                            else:
                                if j != lie:
                                    if i < n:
                                        c[j].append(s[jk])
                                        jk += 1
                                    else:
                                        if j % 2 == 0:
                                            c[j].append(s[jk])
                                            jk += 1
        cs = ''
        for i in range(1, len(c)):
            if i % 2 != 0:
                for j in range(0, len(c[i])):
                    cs += c[i][j]
            else:
                for j in range(len(c[i]) - 1, -1, -1):
                    cs += c[i][j]
        print('明文为:{}'.format(cs))

    s = input('请输入密文：')
    n = int(input('栅栏深度：'))
    _list(s, n)


def ACSLL():
    # -*- coding:utf-8 -*-
    print("字符转换acsii--1.1启动")
    print('请输入待转换的ASCII码，每组的ASCII码用空格分开:')

    a = input()
    q = input("是否输入完成 Y OR NO:")

    if q == 'y':

        num = [int(n) for n in a.split()]
        tmp = ''
        for i in num:
            tmp = tmp + chr(i)
        print(tmp)
    else:
        print("没有完成 再见")