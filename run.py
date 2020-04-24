# -*- coding: utf-8 -*-

import coding

for i in range(0, 1000):
    print("欢迎使用✨北极熊编码转换器✨")
    print("✨" * 50)
    print("0✨退出程序\n"
          "1✨ascii码转化\n"
          "2✨二进制转化为字符\n"
          "3✨base64解码\n"
          "4✨摩斯密码\n"
          "5✨栅栏密码\n"
          "6✨凯撒密码\n"
          "7✨培根密码\n"
          "8✨当铺密码\n"
          "9✨进制转换\n"
          "10✨unicode\n"
          "11✨W型栅栏加密\n"
          "12✨字符串转ACSll")
    print("✨" * 50)
    number = int(input("请输入选择的功能: "))
    if number == 0:
        break
    elif number == 1:
        coding.asciitrun()
    elif number == 2:
        coding.bintrun()
    elif number == 3:
        coding.base64trun()
    elif number == 4:
        coding.morsetrun()
    elif number == 5:
        coding.fencetrun()
    elif number == 6:
        coding.caesartrun()
    elif number == 7:
        coding.Bacontrun()
    elif number == 8:
        coding.dangputrun()
    elif number == 9:
        coding.Hex()
    elif number == 10:
        coding.unicode()
    elif number == 11:
        coding.WWW()
    elif number == 12:
        coding.ACSLL()