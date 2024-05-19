from ultralytics import YOLO

model = YOLO("C:\\Users\\savva\\Documents\\VS-Projects\\TSR_Project\\best.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam

results = model.predict(source=0, save=True)
