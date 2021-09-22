from jinja2 import Template

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getage(self):
        return self.age

    def getname(self):
        return self.name

person=Person('sayan',28)
tm=Template("my name is {{ per.getname() }} and I'm {{ per.getage() }} yrs old")
msg=tm.render(per=person)
print(msg)