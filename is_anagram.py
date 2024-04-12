def is_anagram(str1,str2):
    str1=str1.replace("","").lower()
    str1=str1.replace("","").lower()
    
    if len(str1)!=len(str2):
        return False
    
    char_count1={}
    char_count2={}
    for char in str1:
        char_count1[char]=char_count1.get(char,0)+1
    for char in str2:
        char_count2[char]=char_count2.get(char,0)+1
    return char_count1==char_count2
        
        
str1=input("enter the first string:")
str2=input("enter the second string:")
if is_anagram(str1,str2):
    print("both the string are anagram! ")
else:
    print("both the string are note anagram!")