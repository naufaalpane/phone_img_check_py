import os

# Folder Path
path_image = "./comparing_assets/image"
path_waImg = "./comparing_assets/Whatsapp Images"
list_image = []
list_waImg = []

for file in os.listdir(path_image):
    list_image.append(file)

for file in os.listdir(path_waImg):
    list_waImg.append(file)

list_found = []
list_notFound = []
isTrue = False

for image in list_image:
    isTrue = False

    for waImg in list_waImg:
        if image == waImg:
            list_found.append(image)
        elif image != waImg and isTrue == False:
            list_notFound.append(image)
            isTrue = True

with open('./found.txt', 'w') as f:
    f.write(str(list_found))

with open('./not_found.txt', 'w') as f:
    f.write(str(list_notFound))