list1 = open("urls/test1.txt", "r")
list1 = list1.readlines()
list2 = open("urls/test2.txt", "r")
list2 = list2.readlines()
list3 = open("urls/test3.txt", "r")
list3 = list3.readlines()
list4 = open("urls/test4.txt", "r")
list4 = list4.readlines()
list5 = open("urls/test5.txt", "r")
list5 = list5.readlines()
list6 = open("urls/test6.txt", "r")
list6 = list6.readlines()
list7 = open("urls/test7.txt", "r")
list7 = list7.readlines()
list8 = open("urls/test8.txt", "r")
list8 = list8.readlines()
list9 = open("urls/test9.txt", "r")
list9 = list9.readlines()
list10 = open("urls/test10.txt", "r")
list10 = list10.readlines()
list11 = open("urls/test11.txt", "r")
list11 = list11.readlines()
# print(list1)

listTotal = list1+list2+list3+list4+list5+list6+list7+list8+list9+list10+list11
mylist = list(dict.fromkeys(listTotal))
print(len(mylist))

lengOfTemp  = len(mylist) //3

listTemp1 = [ x for x in mylist[:lengOfTemp]]
listTemp2 = [ y for y in mylist[lengOfTemp:2 * lengOfTemp]]
listTemp3 = [ z  for z in mylist[2*lengOfTemp:]]
# print(listTemp1)
# print(len(listTemp1))
# print(len(listTemp2))
# print(len(listTemp3))
# print(len(listTemp1) + len(listTemp2) + len(listTemp3))
# for l in mylist:
#     print(l)

with open("result/input1.txt", "w") as f:
    for item in listTemp1:
        f.write(item)
with open("result/input2.txt", "w") as f:
    for item in listTemp2:
        f.write(item)
with open("result/input3.txt", "w") as f:
    for item in listTemp3:
        f.write(item)