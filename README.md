# Roadsign Detection
## Description
This project involves retraining the detectNet network to create a model that can recognize stop signs, european speed limit signs, traffic lights, and cross walk signs. Projects like this one can allow for safer and more efficient roads as well as advancements in autonomous driving.
## The Algorithm
I decided to use the detectNet network which is a pre-trained model that I could retrain to recognize certain signs on the road. I needed a dataset that was large enough to fine-tune the model. The dataset I used was found on Kaggle and it contained 876 images as well as four classes: Traffic Light, Stop, Speedlimit, Crosswalk. Every image had its own annotation that described what class it was as well as the size and file path of that image.
