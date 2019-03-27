text1 = 'Hello how are you Hello'
text2 = 'Hello how are you hello hello'
try:
    if 's' not in text1:
        raise Exception('s is not in text')
    if 'hello' in text2:
        raise Exception('hello is in text 2')

except Exception as e:
    print('error message', e)
else: