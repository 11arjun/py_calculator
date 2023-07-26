import re

print("Arjun's Calculator")
print ("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")
print("5.Exit")


select = input("Select the operation above: ")
regex = re.sub('[a-z,a-z]','',select)
if select == '5':
                print("Exited !")
elif select == '6' or (6 <= int(select) <= 100):
                print("Error, Please Enter a number 1-4")

if select != '5':
        x =  input(" Enter The value of x: ")
        y =  input(" Enter The value of y: ")

if select == '1' :
            add = int(x) + int(y)
            print("The outcome is :" ,add)
elif select== '2':
                subtract = int(x)- int(y)
                print("The outcome is :" ,subtract)
elif select== '3':
                divide = int(x)/int(y)
                print("The outcome is :" , divide)
elif select=='4':
                multiply = int(x) * int(y)
                print("The outcome is :" ,multiply)


