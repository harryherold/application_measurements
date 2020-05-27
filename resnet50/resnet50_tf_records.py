#!/usr/bin/env python3

import argparse
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.applications import resnet50


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('batchsize', type=int)
    parser.add_argument('batchcount', type=int)
    args = parser.parse_args()

    ds_all, info = tfds.load('imagenet_resized/32x32',
                              with_info=True,
                              split="train",
                              as_supervised=True)

    classes = info.features["label"].num_classes
    shape = info.features['image'].shape

    model = resnet50.ResNet50(weights=None, input_shape=shape, classes=classes)

    model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  optimizer=tf.keras.optimizers.Adam(), metrics=['accuracy'])

    model.fit(ds_all.batch(args.batchsize), steps_per_epoch=args.batchcount, epochs=1, verbose=1)
