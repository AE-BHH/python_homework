# Task 1

try:
    with open('diary.txt', 'a') as file:
        file.write('What happened today?\n')
        for i in range(5):
            file.write('What else?\n')

            file.write('done for now\n')

except Exception as e:
    print('An exception occurred:', e)
    