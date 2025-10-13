import sys
import os
def update_file_config(file_path,key,value):
    with open(file_path,"r") as file:
        lines = file.readlines()
    #print(lines)

    with open(file_path,"w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value+"\n")
            else:
                file.write(line)
    
def update_large_file_config(file_path,key,value):
    # to handle large file update 
    temp_file = file_path+".tmp"
    try:
        with open(file_path, "r") as read_file,open(temp_file,"w") as write_file:
            for line in read_file:
                if key in line:
                    write_file.write(key + "=" + value+"\n")
                else:
                    write_file.write(line)
        
        os.replace(temp_file,file_path)
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        raise e

file_path = sys.argv[1]
key = sys.argv[2]
value = sys.argv[3]

update_large_file_config(file_path,key,value)