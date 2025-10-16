import os 

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None,"folder name is not valid:"+folder_path
    #print(files)
    except PermissionError:
        return None,"no access to folder:"+folder_path

def main():
    folder_paths = input("please input list of foldername with spaces:").split()
    for folder_path in folder_paths:
        files , error_message = list_files_in_folder(folder_path)
        if files:
            for file in files:
                print(file)
        else:
            print(f"Error in listing files for folder {folder_path}:{error_message}")

if __name__ =="__main__":
    main()