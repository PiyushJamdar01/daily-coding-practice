import time 
def merge_sorted_list(list1, list2):
    
    i = 0 
    j = 0
    empty_list = []
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            empty_list.append(list1[i])
            i += 1
            
        else:
            empty_list.append(list2[j])
            j +=1
            
    while i < len(list1):
        empty_list.append(list2[j])
        
        i += 1

        
    while j < len(list2):
        empty_list.append(list2[j])
        
        j += 1
        
    return empty_list

if __name__ == "__main__":
    
    
    list1 = sorted([int(x) for x in input("Enter the 1 list:").split()])
    list2 = sorted([int(x) for x in input("Enter the 2 list:").split()])
    
    start_time = time.perf_counter()

    result = merge_sorted_list(list1 , list2)  

    print(result)
        
    end_time = time.perf_counter()
    
    print(f" Execution time is {end_time - start_time:.10} seconds")
        
        