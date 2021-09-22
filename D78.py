#template

from jinja2 import Template

name= input("enter name: ")
tm=Template("hello {{name}}")
msg=tm.render(name=name)
print(msg)