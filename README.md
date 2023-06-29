# Roadsign Detection
## Description
This project involves retraining the detectNet network to create a model that can recognize stop signs, european speed limit signs, traffic lights, and cross walk signs. Projects like this one can allow for safer and more efficient roads as well as advancements in autonomous driving.
## The Algorithm
I decided to use the detectNet network which is a pre-trained model that I could retrain to recognize certain signs on the road. I needed a dataset that was large enough to fine-tune the model. The dataset I used was found on Kaggle and it contained 876 images as well as four classes: Traffic Light, Stop, Speedlimit, Crosswalk. Every image had its own annotation that described what class it was as well as the size and file path of that image. I created four files: train.txt, test.txt, trainval.txt, and val.txt. Each of these included a certain amount of image names (train.txt has over 400, test.txt has a little over 200, val.txt has a little over 200, and trainval.txt had a little over 600). I wrote a python script (named script.py) that added the photo names to each of the text files. I also created another text file that contained all of the labels (classes), for when I retrained the model. The model was trained with a pre-written Python program. I chose to train the model based on 30 epochs.
## Running the Project
1. Make sure detectNet is downloaded on the Jetson
2. Make sure the jetson-inference folder is downloaded as well (located here: https://github.com/dusty-nv/jetson-inference)
3. Change directories into jetson-inference/python/training/detection/
4. Download all of the files from this GitHub to the Jetson
5. Make sure the folder road_detection_dataset contains the Annotations, ImageSets/Main, JPEGImages, and Outputs folders as well as labels.txt (there is one in the models folder, which is used for training, so this one isn't necessary). This is the folder that contains the dataset.
6. Change directories to jetson-inference
7. Run the docker container: ./docker/run.sh
8. Change directories to jetson-inference/python/training/detection/ssd
9. Run the following command: python3 train_ssd.py --dataset-type=voc --data=data/road_detection_dataset --model-dir=models/roadsign_check
10. Wait for training to finish
## Export Model
1. 
