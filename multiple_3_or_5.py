def solution(number):
    return sum(set(i for i in range(number) if i % 3 == 0 or i % 5 == 0))

print(solution(10))