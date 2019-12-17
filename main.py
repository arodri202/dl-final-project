
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import Model
import numpy as np
from imageio import imwrite
import os
import random




#FASTER RCNN (ON ONE IMAGE)

# Apply image detector on a single image.
# detector = hub.Module("https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1")
# detector_output = detector(image_tensor, as_dict=True)
# class_names = detector_output["detection_class_names"]

#ResNet50 (built into Keras -- returns a model instance)
#tf.keras.applications.ResNet50

#VGG16 (built into Keras -- returns a model instance)
#keras.applications.vgg16.VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)



class Model(tf.keras.Model):
	def __init__(self):
		"""
    	This model class will contain the architecture for your CNN that 
		classifies images. Do not modify the constructor, as doing so 
		will break the autograder. We have left in variables in the constructor
		for you to fill out, but you are welcome to change them if you'd like.
		"""
		super(Model, self).__init__()

	def call(self, inputs, is_testing=False):


# Train the model for one epoch.
def train(model, batch):

    return

# Test the model by generating some samples.
def test(model, batch):


	return


def main():
  

if __name__ == '__main__':
   main()