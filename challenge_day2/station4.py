
def solution_station4(n):
    number = int(input("Type a number: "))
    
    if number <= 1:
        print(False)
        return
    
    for i in range(2, number):
        if number % i == 0:
            print(False)
            return 
    
    print(True) 
