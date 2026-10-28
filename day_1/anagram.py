import time 
def anagram(str1,str2):
    
    str1= str1.lower()
    str2= str2.lower()
    
    sorted_str1 = sorted(str1)
    
    sorted_str2 = sorted(str2)
    
    if sorted_str1 == sorted_str2:
        return "The two words are anagram"
    else:
        return "The two are not anagram"
    
if __name__ == "__main__":

    str1 = input("Enter your first word \n")
    str2 = input("Enter your second word \n")

    start_time = time.perf_counter()

    result = anagram(str1,str2)

    print(result)

    end_time = time.perf_counter()

    print(f"The Execution take {end_time - start_time:.10} seconds")
    