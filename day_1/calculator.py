import time
class Calculator:
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b
    
    def div(self,a,b):
        if b == 0:
            return "The number cant divide by zero"
        else:
            return a/b
        

if __name__=="__main__":
    
    cal = Calculator()

    num1= float(input("Enter the first number:"))
    num2= float(input("Enter the second number:"))

    print("1. Addition")    
    print("2. Subtraction")    
    print("3. Multiplication")    
    print("4. Division")

    choice = int(input("Enter your choise between 1 to 4:"))
    
    start_time = time.perf_counter()
    
    if choice == 1:
        print("Result",cal.add(num1,num2))
    elif choice == 2:
        print("Result",cal.sub(num1,num2))
    elif  choice == 3:
        print("Result",cal.mul(num1,num2))
    elif choice == 4:
        print("Result",cal.div(num1,num2))
        
    else :
        print("Invalid Choise")
        
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time

    print(f"Execution time {execution_time:10f} seconds")   
        