def is_intersection(list1,list2):
    set1=set(list1)
    set2=set(list2)
    
    intersection_set=set1.intersection(set2)
    intersection_list=list(intersection_set)
    return intersection_list
    
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]

result=is_intersection(list1,list2)
print("intersection of list1 and list2 is :",result)