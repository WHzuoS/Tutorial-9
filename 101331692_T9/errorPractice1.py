def convert_to_int(myString):
    
    try:
        print(int(myString))
        
    except:
        print("Invalid input")
    
    else:
        return int(myString)

def main():
    for i in range(3):
        myString = input("Enter a value: ")
        convert_to_int(myString)
        
main()