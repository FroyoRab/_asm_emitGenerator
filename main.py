import pyperclip
import os

def generatorAsmEmit():
    template = "_asm _emit({}) "
    print(
'''#########################################

- 0x开头的将作为地址解析,去掉0x后小端存储
- 其他将作为字符串解析,直接转为ascii码存储

#########################################'''
    )

    str = input("输入需要转换的字符串:")
    outStr = ""
    count = 0
    if isAddress(str):
        for index in range(len(str)-2,0,-2):
            outStr += template.format("0x"+str[index:index+2])

    else:
        for oneChar in str:
            outStr += template.format(hex(ord(oneChar)))
            count += 1
            if count > 3:
                outStr+="\n"
                count = 0
        outStr+=template.format(hex(0))

    print(outStr)
    pyperclip.copy(outStr)
    print("已加入剪贴板√")

def isAddress(inStr):
    if inStr[:2]=="0x":
        return True
    else:
        return False

if __name__ == '__main__':
    generatorAsmEmit()
    os.system("pause")