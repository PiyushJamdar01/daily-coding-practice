def palindrome(x:int) -> bool:
    
    num = str(x)
    
    reversed_num = num[::-1]
    
    if num == reversed_num:
        return True
    else:
        return False
    
if __name__=="__main__":
    
    num = 121
    
    result = palindrome(num)
    
    print(result)