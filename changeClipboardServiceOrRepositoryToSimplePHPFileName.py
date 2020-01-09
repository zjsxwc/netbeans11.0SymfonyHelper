# -*- coding: utf-8 -*-  
#依赖python2.7 pygtk
#配合NetBeans用于symfony项目，执行本脚本后（Deepin系统快捷键ctrl+shift+y执行.sh文件），
#在执行NetBeans里的navigate/go to file
#鼠标选择文本 -> ctrl+c -> ctrl+shift+y -> ctrl+shift+n -> ctrl+v -> 选择需要的文件
import pygtk
pygtk.require('2.0')
import gtk

def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component
    # with the 'title' method and join them together.
    return ''.join(x.title() for x in components[0:])

clipboard = gtk.clipboard_get()
oldText = clipboard.wait_for_text()
print oldText
if len(oldText):
    newText = oldText
    if ":" in oldText:
        newText = oldText.split(':')[-1]
        if "twig" not in newText:
            newText = newText + ".php"
    else:
        if "." in oldText:
            newText = newText.split('.')[-1]
            newText = to_camel_case(newText)
            newText = newText + ".php"
    print newText
    clipboard.set_text(newText)
    clipboard.store()

