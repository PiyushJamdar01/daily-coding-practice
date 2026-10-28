# remove duplicate without creating the new list
# the list is already sorted

def removeDuplicate(list):
    if len(list) == 0:
       
        return "List is Emplty"
    
    i = 0
    
    for j in range(1,len(list)):
        if list[j] != list[i]:
            i += 1
            list[i] = list[j] # copy the number
            
    return i + 1

if __name__ == "__main__":
    
    list = [0,0,1,1,1,2,2,3,3,4]
    
    result = removeDuplicate(list)  # when we pass the the list into function the modification happen in existing list python does not create the separate list
                                    # the list outside the function also reflect the changes because both reference point is same list object

    print(f"Unique Elements are {result}")
    
    print(f"Removed the duplicate Element {list[:result]}") 
            