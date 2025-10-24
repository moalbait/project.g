
def func(first, last ):
    first_name = first
    last_name = last
    print("Hello " + first_name + " " + last_name)
    full_name = first_name + " " + last_name
    return full_name
 

input_first = input("Enter your first name: ")
input_last = input("Enter your last name: ")
full_name = func(input_first, input_last)
print("Your full name is  : "+full_name)


# Create a function that multiplies two provided variables and returns the result.
# Provide the values using keyboard input.

def multiply(var1, var2):
    product = var1*var2
    return product

input_var1 = int(input("Enter the first number to multiply: "))
input_var2 = int(input("Enter the second number to multiply: "))
product_result = multiply(input_var1, input_var2)
print (product_result)