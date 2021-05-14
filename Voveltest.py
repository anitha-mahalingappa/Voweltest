# def my_fun(arg1,arg2):
#     print(arg1)
   
#     if arg1 in arg2:  
#         print("given is an vowel") 
#     else:
#         print("given is not a vowel") 

# my_vowel = input(" please enter the vowel : ")
# print (type(my_vowel))
# my_vov = ("a","e","i","o","u")	
# print(my_vowel)
# my_fun(my_vowel,my_vov)
# my_vowel1 = input(" please enter the vowel : ")
# my_fun(my_vowel1,my_vov)
# print("hello")


#from typing import Any


# duplicates = ['a','b','c','d','d','d','e','a','b','f','g','g','h']

# uniqueItems = list(set(duplicates))

# print (sorted(uniqueItems))


def word():
    user = input("please enter the value : ")
    word_List = ['a','e','i','o','u']
    a = {}.fromkeys(user, 0) 
    for chr in user:
        if chr in word_List:
           a[chr] += 1
                        
            
    print(a)

word()  
                
# def Check_Vow(string, vowels): 
      
#     # casefold has been used to ignore cases 
#     string = string.casefold() 
      
#     # Forms a dictionary with key as a vowel 
#     # and the value as 0 
#     count = {}.fromkeys(vowels, 0) 
      
#     # To count the vowels 
#     for character in string: 
#         if character in count: 
#             count[character] += 1    
#     return count 
      
# # Driver Code 
# vowels = 'aeiou'
# string = "Geeks for Geeks"
# print (Check_Vow(string, vowels)) 





 