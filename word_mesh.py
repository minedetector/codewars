def word_mesh(arr):
    meshed_string = ""
    remember_len = 0
    for word in range(len(arr)-1):
        for x in range(len(arr[word])):
            #  Checks if from x till the end of the word the other word has the exact same letters, beginning till x
            if arr[word][x:] == arr[word+1][:len(arr[word]) - x]:
                meshed_string += arr[word][x:]
                break
        if len(meshed_string) == remember_len:
            return "failed to mesh"
        remember_len = len(meshed_string)
    return meshed_string

print(word_mesh(["beacon","condominium","umbilical","california"]))
