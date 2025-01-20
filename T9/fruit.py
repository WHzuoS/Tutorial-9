def count_fruit(fruit_list):
    
    fruit_count = {}
    
    for i in fruit_list:
        
        if i not in fruit_count:
            fruit_count[i] = 1
        elif i in fruit_count:
            fruit_count[i] += 1
            
    return fruit_count

def main():
    fruits = ["apple", "banana", "apple", "orange", "banana", "apple", "grape", "orange"]
    print(count_fruit(fruits))
    
main()