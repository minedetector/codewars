def going_through(arr):
    answer = []
    x = 0
    for i in range(len(arr)-1):
        if i == len(arr) - 1:
            answer.append(arr[i])
            break
        if x == 2:
            x = 0
        if x == 1:
            x = 2
            continue
        if arr[i] == "SOUTH" and arr[i + 1] == "NORTH":
            x = 1
        elif arr[i] == "NORTH" and arr[i + 1] == "SOUTH":
            x = 1
        elif arr[i] == "EAST" and arr[i + 1] == "WEST":
            x = 1
        elif arr[i] == "WEST" and arr[i + 1] == "EAST":
            x = 1
        else:
            answer.append(arr[i])
    return answer


def dirReduc(arr):
    answer = going_through(arr)
    while True:
        if len(answer) == len(going_through(answer)):
            break
        else:
            answer = going_through(answer)

    return answer


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

print(dirReduc(a))
