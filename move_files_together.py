# 9/24/2021 11:41 PM
import os
import shutil
# 目标文件夹，此处为相对路径
# determination = r''
# if not os.path.exists(determination):
#     os.makedirs(determination)

# 源文件夹路径
path = r''
folders = os.listdir(path)
dirname = 'a' + folders[0].split(' ')[0]
determination = f'D:\downloads\{dirname}'
if not os.path.exists(determination):
    os.makedirs(determination)
for folder in folders:
    dir = path + '\\' + str(folder)
    files = os.listdir(dir)
    for file in files:
        source = dir + '\\' + str(file)
        deter = determination + '\\' + str(file)
        shutil.copyfile(source, deter)
print('movement done!')
