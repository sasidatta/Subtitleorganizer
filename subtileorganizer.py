import zipfile
import glob, os
import os
import re
import shutil
import rarfile
import unrar

list= []
def remove_junk_zip(file, del_dir_zip, del_dir_srt):
    try:
            zf = zipfile.ZipFile(file, 'r')
            file_list = zf.namelist()
            zf.close()
            for i in file_list:
                if i.endswith(".srt"):
                        list.append(file)
                        print "Moving file ", file
                        shutil.move(file,os.path.join(del_dir_zip, i))
            dir=file[:-4]
            remove_junk_dir(file, dir, del_dir_zip, del_dir_srt)
    except:
             pass

def remove_junk_rar(file, del_dir_zip, del_dir_srt):
    try:
            rf = rarfile.RarFile(file, 'r')
            file_list = rf.namelist()
            rf.close()
            for i in file_list:
                if i.endswith(".srt"):
                    list.append(file)
                    print "Moving file ", file
                    shutil.move(file,os.path.join(del_dir_zip, i))
            dir = file[:-4]
            remove_junk_dir(file, dir, del_dir_zip, del_dir_srt)
    except:
             pass


def remove_junk_dir(file, dir_path,  del_dir_zip, del_dir_srt):
    try:
            if len(os.listdir(dir_path)) == 1:
                shutil.move(file, del_dir_srt)
            elif len(os.listdir(dir_path)) == 2:
                for i in os.listdir(dir_path):
                    if i.endswith(".nfo"):
                        shutil.move(file,os.path.join(del_dir_zip, i))
                        shutil.move(dir_path, del_dir_zip)
                    elif i.endswith(".srt"):
                        shutil.move(file, os.path.join(del_dir_zip, i))
                        shutil.move(dir_path, del_dir_zip)
                    elif i.endswith(".txt"):
                        shutil.move(file, os.path.join(del_dir_zip, i))
                        shutil.move(dir_path, del_dir_zip)
                    elif i.endswith(".html"):
                        shutil.move(file, os.path.join(del_dir_zip, i))
                        shutil.move(dir_path, del_dir_zip)
            elif len(os.listdir(dir_path)) == 3:
                list=os.listdir(dir_path)
                for i in list:
                    if i.endswith(".nfo"):
                        shutil.move(file,os.path.join(del_dir_zip, i))
                        shutil.move(dir_path, del_dir_zip)
                    elif i.endswith(".srt"):
                        shutil.move(file, os.path.join(del_dir_zip, i))
                        shutil.move(dir_path, del_dir_zip)
                    elif i.endswith(".txt"):
                        shutil.move(file, os.path.join(del_dir_zip, i))
                        shutil.move(dir_path, del_dir_zip)
                    elif i.endswith(".html"):
                        shutil.move(file, os.path.join(del_dir_zip, i))
                        shutil.move(dir_path, del_dir_zip)
                    else:
                         break
            elif len(os.listdir(dir_path)) > 3:
                shutil.move(file, del_dir_srt)
    except:
        pass


def list_dir(paths, del_dir_zip, del_dir_srt):
    rx = re.compile(r'\.(zip|rar|gz|srt)')
    for path in paths:
        for dirpath, dirs, files in os.walk(path):
            for filename in files:
                if rx.search(filename):
                    fullpath = os.path.join(dirpath, filename)
                    if filename.endswith(".zip"):
                        remove_junk_zip(fullpath,del_dir_zip,del_dir_srt)
                    elif filename.endswith(".gz"):
                        remove_junk_zip(fullpath, del_dir_zip,del_dir_srt)
                    elif filename.endswith(".rar"):
                        remove_junk_rar(fullpath, del_dir_zip,del_dir_srt)
                    elif filename.endswith(".srt"):
                        remove_junk_dir(fullpath, dirpath, del_dir_zip,del_dir_srt)
paths = ["C:\\", "D:\\"]
del_dir_zip="D:\\Dump\\zip"
del_dir_srt="D:\\Dump\\srt"
list_dir(paths, del_dir_zip,del_dir_srt)
if len(list) >  0:
    print "Moved ",len(list) ,"files to ", del_dir_zip
else:
    print "No files found"