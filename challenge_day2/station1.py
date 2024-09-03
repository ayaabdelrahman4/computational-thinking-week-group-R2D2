#"observation challege station 1" 
def solution_station1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

# Test cases
print(solution_station1(0))  # Output: 0
print(solution_station1(6))  # Output: 8
print(solution_station1(8))  # Output: 21
print(solution_station1(28)) # Output: 317811
print(solution_station1
      (62)) # Output: 10610209857723
