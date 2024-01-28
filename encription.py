import random
import cover_text as ct

def encripting_data():
    arr,dic,fc = ct.cover_text()
    secret = input("ENTER SECRET TEXT: ")
    code = []
    
    # ENCRIPTING TEXT USING RANDOM INDEX OF COVER TEXT
    for i in range(0, len(secret)):
        lst = arr[dic.get(secret[i])]
        random_index = random.choice(lst)
        #ind = (i*random_number+len(secret))%len(lst)
        code.append(random_index)
    
    # ENCRIPTING WITH THE ADDITION OF PREVIOUS INDEX
    enc = []
    for i in range(1,len(code)):
        cc = code[i] + dic.get(secret[i-1])
        enc.append(cc)

    return enc,secret[0]

    
