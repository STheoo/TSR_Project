# Traffic Sign Detection Machine
The scope of this project is create a real-time Traffic Sign Detection Program that inside video offline or a live camera source it detects Traffic Signs. There are several repositories on Traffic Sign Image Classification, but they are all out-dated using old technologies and libraries. I have done research in different algorithms and have come across a newly updated library YOLOv9 which uses a state-of-the-art You Only Look Once object detection algorithm which has very high accuracy and performance. The objective is to prepare the German Traffic Sign Benchmark Dataset, by doing annotations, cleaning and augmentation to then train an object detection model using YOLOv9 and use it on a video source to detect the Traffic Signs and show their class label.

## Exploratory Data Analysis
Checking for class imbalances was quite important, since using the free Roboflow plan I could only upload 10000 images and wanted all class to be sampled evenly.

Before:

![asdjapsoj](https://github.com/STheoo/TSR_Project/assets/46623018/b11a1c03-dfe7-4845-b96d-bb8e097e7e0d)

After:

![asdasc](https://github.com/STheoo/TSR_Project/assets/46623018/50abbf59-cdbe-4a58-a408-8162039050fc)

## Model Training
Preparing the dataset was a tedious process as it had to be annotated on the Roboflow platform and then exported with the annotations. Using that dataset I have imported the YoloV9 library and started training on Google Colab to get the best weights file. With that file Traffic Sign Detection would be complete.

![results](https://github.com/STheoo/TSR_Project/assets/46623018/87888116-9671-4b83-a0a5-15348a816ca0)

## Model Performance
Here we can evaluate the performance of each class and their predicted percentage. On the diagonal we want all to be very dark blue. The darker the square the bigger the percentage of signs were predicted correct on the diagonal. Therefore looking at the matrix we can tell 80km Speed Limit, 100km Speed limit were predicted wrong quite a few times. Also there is an interesting pattern were keep right/keep left and go straight or left/go straight or right signs are lighter and boxes around it have light coloring which shows us that they are being confused with each other.

![confusion_matrix](https://github.com/STheoo/TSR_Project/assets/46623018/e93206a7-984f-494e-a0ff-b24942026271)

## Model Inference

The image below is an output file from the YoloV9 training results. It is a batch of validation images with their class predictions, which we can see are accurate.

![val_batch0_pred](https://github.com/STheoo/TSR_Project/assets/46623018/71687d83-9948-4166-847c-798df4c07fad)

Below is a detection result using a picture I have taken of a couple traffic signs around my University.

![1](https://github.com/STheoo/TSR_Project/assets/46623018/51aaf542-d52b-4fbf-9625-e96a6ebc07ff)
