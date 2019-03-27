text1 = 'Hello how are you hello'
text2 = 'hello how are you hello hello'
try:
    with open("file1.log", "r") as f:
        print(f.read())
    with open("file.log", "r") as f:
        print(f.read())
    with open("file2.log", "r") as f:
        print(f.read())
        text2 = text2.split
        count = 0
        for word in text2:
            if word == 'hello':
                count += 1
                print(count)
                if count > 2:
                    print("error")
except:
    print("file not found")
else:
    print("duplicate words in text1")
    print("duplicate words in text2")
finally:
    print("I will run the irrespective of error")



