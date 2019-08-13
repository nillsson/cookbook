import xml.etree.ElementTree as et

tree = et.parse("03.xml")

root = tree.getroot()

for e in root.iter("Name"):
    print(e.text)

for stu in root.iter("Student"):
    name = stu.find("Name")

    if name != None:
        name.set("test", name.text*2)

stu = root.find("Student")

#新建一个子元素
e = et.Element("Adder")
e.attrib = {"mimi" : "yiyi"}
e.text = "lloyd"

stu.append(e)

#一定需要写回文件，否则修改无效
tree.write("03.xml")