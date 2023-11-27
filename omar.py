from PIL import Image as PILImage
import os
import uuid
folder_path = r"C:\Users\kh249\OneDrive\Desktop\Yaman help\D"
contents = os.listdir(folder_path)
path_ = os.path.join(folder_path, str(uuid.uuid4())) 
os.mkdir(path_)
a = 0
for item in contents:
    if not  any(item.endswith(type) for type in ['.jpg', '.jpeg', '.png', '.tiff']):
        os.rename(os.path.join(folder_path, item), os.path.join(folder_path, item)+'.png')
        item_path = os.path.join(folder_path, item)
        image_path = os.path.join(folder_path, item)+'.png'
        if os.path.isfile(image_path):
            path = os.path.join(folder_path, item)+'.png'
            image_edit = PILImage.open(path)
            image_edit.save(os.path.join(path_, f'Item_num{a}.png'), "png", quality=85, optimize=True)
        a+=1
