#!/usr/bin/python3

print("""The following is your daily Customer Service task checklist calculator - """.format())
print("\n")

a = int(input("Q1: List the amount of emails responded to: "))
print("\n")
b = int(input("Q2: List the amount of emails initiated and sent out: "))
print("\n")
c = int(input("Q3: List the number of answered incoming calls: "))
print("\n")
d = int(input("Q4: List the number of outgoing calls: "))
print("\n")
e = int(input("Q5: List the number of warranty RA creations: "))
print("\n")
f = int(input("Q6: List the number of warranty/replacements shipped: "))
print("\n")
g = int(input("Q7: List the number of sales orders completed and shipped: "))
print("\n")
h = int(input("Q8: List the number of resolved customer's complaint/problem: "))
print("\n")

print("Great Job! Your daily task calculation is: ")
print(a + b + c + d + e + f + g + h)

if __name__ == "__main__":
    ()
