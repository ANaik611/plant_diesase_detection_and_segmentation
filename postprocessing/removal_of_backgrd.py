import cv2
import numpy as np

def bluish_grey_to_black(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define HSV range for bluish-grey
    lower_blue = np.array([0, 0, 50])
    upper_blue = np.array([180, 50, 200])

    # Create a mask for bluish-grey pixels
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Change bluish-grey pixels to black in the original image
    image[mask > 0] = [0, 0, 0]

    # Save the result
    cv2.imwrite(output_path, image)

    return image

def calculate_leaf_area(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the total area of the image
    total_area = gray_image.shape[0] * gray_image.shape[1]

    # Count the number of black pixels (where pixel value is 0)
    black_area = np.sum(gray_image == 0)

    # Calculate the leaf area
    leaf_area = total_area - black_area

    return leaf_area

# Usage
processed_image = bluish_grey_to_black('/content/anu.JPG', '/content/naik.JPG')
leaf_area = calculate_leaf_area(processed_image)

print(f"Leaf area (in pixels): {leaf_area}")