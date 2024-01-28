import cover_text as ct

def decripting_data(stego_key,auto_key):
    arr,dic,fc = ct.cover_text()
    num = dic.get(auto_key)
    text = str(auto_key)
    
    # DECRIPTING TEXT
    for i in range(0,len(stego_key)):
        text += fc[stego_key[i] - num]
        num = dic.get(fc[stego_key[i] - num])
    
    return text
        