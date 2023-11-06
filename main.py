import numpy as np
from PIL import Image

def add_gaussian_noise(image, mean=0, std=10):
    ''' Adds Gaussian noise to an image.
        Parameters:
        - image: PIL.Image - Input image
        - mean: float - Mean of the Gaussian noise
        - std: float - Standard deviation of the Gaussian noise
    '''
    # Convert image to numpy array
    img_array = np.array(image)

    # Generate Gaussian noise
    gaussian = np.random.normal(mean, std, img_array.shape).reshape(img_array.shape)

    # Add the Gaussian noise to the image
    noisy_img_array = img_array + gaussian

    # Clip the values to be in the allowable range of [0, 255]
    noisy_img_array = np.clip(noisy_img_array, 0, 255)

    # Convert back to PIL image
    noisy_image = Image.fromarray(np.uint8(noisy_img_array))
    return noisy_image

# Load the image
image_path = 'sheep.png'  # Replace with your image path
original_image = Image.open(image_path)

# Incremental steps
increments = 200  # Define the number of increments
std_increment = 25  # Define the standard deviation increment

for i in range(1, increments + 1):
    # Increase standard deviation with each step
    current_std = std_increment * i
    noisy_image = add_gaussian_noise(original_image, mean=0, std=current_std)
    noisy_image.save(f'noisy_image_{i}.png')  # Save each increment step as a new image

print("Gaussian noise addition complete.")
