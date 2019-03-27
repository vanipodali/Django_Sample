s = 'hello hello'

s = s.split
count = 0
for word in s:
    if word == 'hello':
        count += 1
        print(count)
        if count > 2:
            raise Exception('that there are duplicate words')



