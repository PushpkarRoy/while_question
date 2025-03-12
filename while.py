#  Q1 print 10 to 15 no. help of while loop ----------------------------------------------------

a = 10
while a <= 15:
    print(a, end=" ")
    a += 1

#  Q2- find cube of no. 1 to 5. ----------------------------------------------------------------
no = 1 
while no <= 5:
    a = (no** 3)  # no * no* no ko or no ** 3 bhi likh sakte hai
    print(a,end=" ")
    no += 1

# Q3 odd no. from 1 to 10 -----------------------------------------------------------------------------

n = 1
while n <= 10:
    print(n, end=" ")
    n += 2

    #    OR 
n =1 
while n <= 10:
    if(n %2 == 0): # equal to value 1 '==' 1, or not equal to 1 '!=' 2
        pass
    else:
        print(n)
    n += 1

# Q4 calculate the product of 1 to 5 --------------------------------------------------------------

pro = 1 
num = 1
while num <= 5:
    pro = pro * num
    num += 1
print(pro)

#  Q5 Reverse the sentance " Hello World" -------------------------------------------------------

sen = input("Enter the word:-  ")
words = sen.split()
for word in words:
    i = len(word) - 1
    while i >= 0:
        print(word[i], end=" ")
        i -= 1
   

#   Q6 consanats the string
#        write a program to count the number of consanents in the word  " "----------------------------

word = input("enter the words:- ")
vowel = "a e i e u"
count = 0
index = 0
while index < len(word):
    if word[index].lower() not in vowel and word[index].isalpha():
        count += 1
    index += 1
print(count)

# Q7 Find first 5 multipal of 3-----------------------------------------

n = int(input("Enter the word:- "))
r = 1

while r <= 5 :
    multipal = (r * n)
    print(multipal, end=" ")
    r += 1

# Q8 write a program to calculate 3 to the power of 4.--------------------

n = int(input("enter the no. :- "))
a = int(input("enter the no. :- "))
result = 1
i = 0
while i < a:
     result *= n
     i += 1
print("The result of", n, "to the power", a, "is:", result)

#  Q9 write a program to check if a given number such a perfect square or not -----------

a = int(input("Write a value or a  no. :="))
b = 1
while b <= a:
    if( b*b == a):
        break
    b +=1
print("The squre of", a,"is",b)

#  or -----------------------------

a = int(input("Write a value or a  no. :="))
b = 1 

while b * b <= a:
    if b * b == a:
        break
    elif (b * b != a):
        statement = False
    b += 1
print("Yes ", a ,"is a perfact squre of ", b)
if statement != False:
    print("it is not a perfact squre")

#  Q10 count occurrenes of a specific character in a string
#  write a program to count occurrencess of the character " s" in the str "Scuess"

str = input("Erite a word in this line:-")
count_of_ste = input("Kya ginna hai bhai tujhe :=")
count = 0
index = 0
while index < len(str):
    if(str[index] == count_of_ste):
        count += 1
    index +=1
print("Your total", count_of_ste,"in your words", str,"is", count )