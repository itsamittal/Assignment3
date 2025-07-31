
# coding: utf-8

# In[1]:


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i    
    return result
sample_number = int(input('Enter a number:'))
result = factorial(sample_number)
print(f"The factorial of {sample_number} is: {result}")


# In[2]:


import math

try:
    number = float(input("Enter a number: "))

    if number <= 0:
        print("Please enter a number greater than 0 for log and square root calculations.")
    else:
       
        square_root = math.sqrt(number)

       
        natural_log = math.log(number)

   
        sine_value = math.sin(number)

        print(f"Square root: {square_root}")
        print(f"logarithm: {natural_log}")
        print(f"Sine: {sine_value}")

except ValueError:
    print("Invalid input. Please enter a valid number.")

