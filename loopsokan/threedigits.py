while True:
    mynumber = input('Bir sayi giriniz:')
    if ',' in mynumber:
        if len(mynumber) == 4:
            isvalid = True
            for ch in mynumber:
                if ch != ',' and not ch.isnumeric():
                    print('invalid floating point number')
                    isvalid = False
                    break
            if isvalid:
                print('3 bas sayi:' + mynumber)
                break
    elif len(mynumber) == 3 and mynumber.isnumeric():
        print('3 bas sayi girdiniz:' + str(mynumber))
        break
    else:
        print(str(len(mynumber)) + ' bas sayi girdiniz.')