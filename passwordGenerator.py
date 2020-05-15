import random
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowchar= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
          'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
          'z']
upchar= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
         'Z']
symbols=['!','"','#','$','%','&','\',''','(',')','*','+',',',
         '-','.','/',':',';','?','@','[','\\',',',']','^','_','`','{','|','}'
         '~']
possible=lowchar+upchar
random.shuffle(possible)
initial=12
pas=[]
print("Did you know a strong password is of the length 12 with random letters,numbers and characters")
a=int(input(("How long would you like length of yours? NOTE WE STRONGLY RECOMMEND LENGTH OF 12 : ")))
initial=a
for i in range((initial)//2):
    pas.append(random.choice(possible))
    pas.append(random.choice(symbols))
random.shuffle(pas)
print("Password has been generated as: {0}".format("".join(pas)))
print("#########################################")
s=input("Do you want to store your password?")
if s=='yes' or s=='YES' or s=='y':
    c=input("Can i know the name of the website this password is for?")
    file=open('passwords.txt','a')
    file.write("Password for: {0} || password:{1}".format(c,"".join(pas))+"\n")
    file.close()
    input("Generated!! press any key to exit")
else:
    input(("Okay! press any key to exit"))