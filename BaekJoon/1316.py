word_count = int(input())
group_word_count = 0
for index in range(0 , word_count) :
    word = input()
    comp = 0
    list = []
    for i in range(0,len(word)) :
        if not list.__contains__(word[i]) :
            list.append(word[i])
        else :
            if word[i] != list.__getitem__(len(list)-1) :
                break
        if i == len(word)-1 :
            group_word_count += 1

print(group_word_count)