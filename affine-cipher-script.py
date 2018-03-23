message = input("Enter message to cipher: ")
formula = input("Enter cipher formula using 'c' as the variable (all else should be operators and integers): ")
encrypted = ""  
for i in message:
    if (i != " "):
        wint = int(ord(i.lower())-96)
        formulaNew = ""
        for j in formula:
            if(j.lower() == 'c'):
                j = str(wint)
            else:
                j = j
            formulaNew += j
        encrypted += chr((int(eval(formulaNew)+96)))
    else:
        encrypted += " "
print ("The result is: " + encrypted)