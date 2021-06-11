import os 
import shutil 
import time 


def read_all_file(path): 
    output = os.listdir(path) 
    file_list = [] 
    
    for i in output: 
        if os.path.isdir(path+"/"+i):
            file_list.extend(read_all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i):
            file_list.append(path+"/"+i)
    
    return file_list 
 
 
def copy_all_file(file_list, new_path):
    for src_path in file_list:
        file_name = src_path.split("/")[-1]
        f.seek(0)
        line = f.readline()
        while line:
            serach_file=line.split("/")
            result_text=serach_file[-1]           
            del serach_file[-1]            
            current_path='/'.join(serach_file) 
            
            if file_name in result_text:
                if not os.path.isdir(new_path+current_path+file_name):                                                           
                    os.makedirs(new_path+current_path, exist_ok=True)
                shutil.copy2(src_path, new_path+current_path+file_name)
                print("전송 완료 파일 :" + src_path)
                print("전송된 경로 : " + new_path+current_path+file_name)
            line = f.readline()
   

src_path = "C:/Users/kimjeonghwan/Desktop/asis/AttachFile/Storage" # 기존 폴더 경로
new_path = "C:/Users/kimjeonghwan/Desktop/copy/" # 옮길 폴더 경로
f = open('./input.py','r')

file_list = read_all_file(src_path)
copy_all_file(file_list, new_path)
