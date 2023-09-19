# import re
# import os 
# import shutil


# main_folder = r''

# def rename_file(file):



#     file_name, file_extension = os.path.splitext(file)
#     file_name_numbers = re.findall(r'\d+', file_name)
     
#     contador = 0
#     if not file_name_numbers:
#         return file 
    


#     return file_name_numbers



# def files_loop(root, dirs, files):
#     for file in files:
#         new_file_name = rename_file(file)
#         old_file_full_path = os.path.join(root, file)
#         new_file_full_path = os.path.join(root, new_file_name)
#         print(new_file_name)
#         # print(f'movendo arquivos {file} para {new_file_name}')
#         # shutil.move(old_file_full_path, new_file_full_path)


# def main_loop():
#     for root, dirs, files, in os.walk(main_folder):
#         files_loop(root, dirs, files)

# if __name__ == '__main__' :
#     main_loop()

   