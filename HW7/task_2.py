def count_glasnye(word):
    count = 0
    glasnye = 'аеёиоуыэюя'
    for i in word: 
        if i in glasnye:
            count += 1
    return count

ryfm_pyfm = 'чик пик пон чик'
words = ryfm_pyfm.split(" ") 
ryfm_pyfm_cout = list(map(count_glasnye, words))
if len(set(ryfm_pyfm_cout)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам') 

