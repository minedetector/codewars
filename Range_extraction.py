def solution(args):
    last = []
    answer = []
    for i in args:
        if len(last) == 0:
            last.append(i)
        elif last[-1] + 1 == i:
            last.append(i)
        else:
            if len(last) == 1:
                answer.append(str(last[0]))
                last[0] = i
            elif len(last) == 2:
                answer.append(str(last[0]))
                answer.append(str(last[1]))
                del last[:]
                last.append(i)
            else:
                answer.append(str(last[0]) + "-" + str(last[-1]))
                del last[:]
                last.append(i)
    if len(last) == 1:
        answer.append(str(last[0]))
    elif len(last) == 2:
        answer.append(str(last[0]))
        answer.append(str(last[1]))
    else:
        answer.append(str(last[0]) + "-" + str(last[-1]))
    return str(",".join(answer))
