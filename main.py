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

    str = input("输入需要转换的字符串或0x开头的地址:")
    startPos = int(input("请输入十六进制偏移位置:0x"),16)
    outStr = ""
    colCount = 0
    if isAddress(str):
        for index in range(len(str)-2,0,-2):
            outStr += template.format("0x"+str[index:index+2])
        outStr = "// {} - {:#3x}\n{}".format(str,startPos+int((len(str)-2)/2),outStr)

    else:
        for oneChar in str:
            outStr += template.format(hex(ord(oneChar)))
            colCount += 1
            if colCount > 3:
                outStr+="\n"
                colCount = 0
        outStr+=template.format(hex(0))
        outStr = '// "{}" - {:#3x}\n{}'.format(str, startPos + len(str)+1, outStr)

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
