def safe_divide(a, b):
    try:
        quotient = a/b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    else:
        return round(quotient, 2)
    
def main():
    while True:
        a = int(input("Enter the first number (a): "))
        b = int(input("Enter the second number (b): "))
        print(f"Result: {safe_divide(a,b)}")
        exit = input("Do you want to perform another calculation? (type 'quit' to exit): ")
        if exit.lower() == "quit":
            break
        
main()