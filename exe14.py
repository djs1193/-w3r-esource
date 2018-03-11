
# calculating difference in days
#approximating a month has 30 days
#assuming all years 365 days

s1 = input("enter the first date: ")
s2 = input("enter the second date: ")

list_1 = (s1.split())
list_2 = (s2.split())

if (list_1 == list_2):
    print ('the two days are same')

elif((list_1[2] == list_2[2]) and (list_1[1] == list_2[1])):
    diff = abs(int(list_1[0]) - int(list_2[0]))
    print (diff)

elif((list_1[2] == list_2[2])):
    diff = abs((int(list_1[0]) - int(list_2[0]))) + 30*(abs(int(list_1[1]) - int(list_2[1])))
    print (diff)

else:
    diff = abs(int(list_1[0]) - int(list_2[0])) + 30*(abs(int((list_1[1])) - int(list_2[1]))) +365*(abs(int(list_1[2]) - int(list_2[2])))
    print (diff)
