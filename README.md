# _asm_emitGenerator
对字符串和地址自动生成_asm_emit(0xXX)文本的py脚本

==需要下个剪贴板的库`pyperclip`==
`pip install pyperclip`


- 0x开头将被解析成地址,已小端的方式输出
- 其他的将作为字符串,输出ascii码

- 脚本会自动将文本复制到剪贴板内,按任意键即可关闭
