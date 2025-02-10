import os

path = os.path.split(os.path.realpath(__file__))[0] #D:\Program Files\happy-blog\source\gallery\harbin-tourism\
abspath_images = path + '\\images' #图片绝对路径
xdpath_images = 'images' # 图片相对路径 images

os.chdir(abspath_images) #harbin-tourism\images
ls_file = []
for file in os.scandir():
    if file.is_file():
        ls_file.append(file.name)

md_text = "\n{% gallery %}\n"

for image in ls_file:
    md_path = "![" + os.path.splitext(image)[0] + "](" + str(xdpath_images)+ "\\" + image+ ")"
    md_text += md_path.replace("\\", "/")+"\n"

md_text += "{% endgallery %}"

os.chdir(path)

with open('index.md', 'a', encoding='utf-8') as f:
    f.write(md_text)