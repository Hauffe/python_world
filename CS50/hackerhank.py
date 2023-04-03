queries = [["ADD_FILE","/file1.txt","4"], 
 ["ADD_FILE","/file2.mp4","38"], 
 ["ADD_FILE","/dir1/file3","17"], 
 ["ADD_FILE","/dir1/file4.txt","6"], 
 ["ADD_FILE","/dir1/deep_dir/file5.mkv","40"], 
 ["ADD_FILE","/dir2/file6.mov","15"], 
 ["GET_N_LARGEST","/","3"]]

def solution(queries):
    files = {}
    returns = []
    for touple in queries:
        cmd = touple[0]
        if cmd == "ADD_FILE":
            file = touple[1]
            size = int(touple[2])
            if file in files:
                files[file] = size
                returns.append("overwritten")
            else:
                files[file] = size
                returns.append("created")
        if cmd == "GET_FILE_SIZE":
            file = touple[1]
            if file in files:
                returns.append(str(files[file]))
            else:
                returns.append("")
        if cmd == "MOVE_FILE":
            file1 = touple[1]
            file2 = touple[2]
            if file2 not in files and file1 in files:
                files[file2] = files[file1]
                del  files[file1]
                returns.append("true")
            else:
                returns.append("false")
        if cmd == "GET_N_LARGEST":
            file_name = touple[1]
            num = int(touple[2])
            temp_files = sorted(files.items(), key = lambda item: (item[1], item[0]), reverse=True)
            count = num
            string = ""
            for key, _ in temp_files:
                if file_name in key and files[key] > num and count > 0:
                    count -= 1
                    string += key+"("+str(files[key])+")"
                    if count > 0:
                        string+=", "
            returns.append(string)
    return(returns)



import itertools
a = [i for i in filter(lambda x: x%5, itertools.islice(itertools.count(5), 10))]
print(a)        