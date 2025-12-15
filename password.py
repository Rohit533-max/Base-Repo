import string
import random  #to choose the random elements form the list s

if __name__ == "__main__":
    s1 = string.ascii_letters   
    #ascii letters contain both upper and lowercase letters
     
    s2 = string.digits
    
    s3 = string.punctuation  
    #punctuation =  special char eg:-> @,#,$
     
    passlen = int(input("Enter the password length\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    
    random.shuffle(s) # to shuffle the list s
    print("".join (s[0:passlen]))

