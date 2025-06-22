import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load your trained model (save it after training and load here)
model = tf.keras.models.load_model('mnist_model.h5')

# Function to generate and display images (reuse from training script)
def generate_digit_images(model, digit, num_images=5):
    images = []
    for _ in range(num_images):
        noise = np.random.normal(0, 0.1, (1, 28, 28, 1))
        target = tf.one_hot([digit], 10)
        for _ in range(50):
            with tf.GradientTape() as tape:
                tape.watch(noise)
                preds = model(noise, training=False)
                loss = -tf.reduce_sum(target * tf.math.log(preds + 1e-10))
            grads = tape.gradient(loss, noise)
            noise += 0.1 * grads
            noise = tf.clip_by_value(noise, 0, 1)
        images.append(noise.numpy().squeeze())
    return images

# Streamlit app
st.title("Handwritten Digit Generator")
digit = st.slider("Select a digit (0-9)", 0, 9, 5)

if st.button("Generate Images"):
    images = generate_digit_images(model, digit)
    cols = st.columns(5)
    for i, img in enumerate(images):
        cols[i].image(img, caption=f"Image {i+1}", width=100, clamp=True)

