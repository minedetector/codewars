def pos_average(s):
    s = s.split(", ")
    counter = 0
    total = 0
    for i in range(len(s)):
        for x in range(i+1, len(s)):
            for y in range(len(s[0])):
                if s[i][y] == s[x][y]:
                    counter += 1
                total += 1
    return round((counter / total)*100, 10)

print(pos_average("0, 0, 1"))