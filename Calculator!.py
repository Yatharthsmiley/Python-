import time
a = input("Type your first no.")
if(a!=float):
    time.sleep(2)
elif(a!=int):
    print("Please, correct your first no.\n By Re-Running the Repl!") and time.sleep(10)
b = input("Type our second no.")
if(b!=float):
    time.sleep(2)
elif(b!=int):
    print("Correct your second no.\nBy Re-Running the Repl!") and time.sleep(10)
print("+ is addition")
time.sleep(2)
print("- is subtraction")
time.sleep(2)
print("* is multiplication")
time.sleep(2)
print("/ is division")
time.sleep(1)
c = input("Enter your sign:  ")
if(c=="+"):
    print("The addition of",float(a),"and",float(b),"is",float(a)+float(b))
elif(c=="-"):
    print("The subtraction of",float(a),"and",float(b),"is",float(a)-float(b))
elif(c=="*"):
    print("The multiplication of",float(a),"and",float(b),"is",float(a)*float(b))
elif(c=="/"):
    print("The division of",float(a),"and",float(b),"is",float(a)/float(b))
time.sleep(5)
exit()