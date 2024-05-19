from ultralytics import YOLO
from IPython.display import Image
from PIL import Image


model = YOLO("C:\\Users\\savva\\Documents\\VS-Projects\\TSR_Project\\best.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
im1 = Image.open('Train\\13\\00013_00002_00025.png')
results = model.predict(source=im1, save=True)  # save plotted images
