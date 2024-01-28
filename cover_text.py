def cover_text():
    #Opening cover text file
    file_path = "cover_text.txt"
    with open(file_path, 'r') as file:
        file_content = file.read()
        
    dic = {}
    count = 0
    arr = []
    #getting index of alphabet and space
    for j in "abcdefghijklmnopqrstuvwxyz ":
        dic[j] = count
        count += 1
        arr.append([])
    
    for i in range(0,len(file_content)):
        arr[dic.get(file_content[i])].append(i)
        
    return arr, dic, file_content
    