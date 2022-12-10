string1=input("Write the Phrase you want to convert into acronym: ")
string2=string1.split()
a=""
for word in string2:
    a += word[0]
a=a.upper()
print("Final Acronym of {} : {}".format(string1,a))
