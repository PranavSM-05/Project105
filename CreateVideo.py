import os 
import cv2  
  
path = "Images/"
  
Images = []

for file in os.listdir(path):
    ext = os.path.splitext(file)
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)
        file_name = Images.append()
count = len(Images)
frame = cv2.imread(Images[0])
height, width, layers = frame.shape   
size = (width,height)
print(size)

out = cv2.VideoWriter('Project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count-1):
    out.write(cv2.imread(os.path.join(path, file)))
print("Done")