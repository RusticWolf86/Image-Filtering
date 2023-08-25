# Image Filtering and Processing Project

This project explores the concepts of image filtering and processing using basic convolution techniques. The goal is to understand how different filters can enhance, modify, or extract specific features from images.

## Project Overview

In this project, we apply various filters to an image using manual convolution, without relying on built-in functions. We examine the effects of each filter on the original image and gain insights into the theory behind these filters.

## Filters Explored

1. **Identity Filter (1e):** No change to the image.
2. **Shift Filters (1f, 1d, 1g, 1c):** Induce shifts in different directions.
3. **Sobel Edge Detection Filters (2a, 2b):** Detect horizontal and vertical edges.
4. **Average Filter (3a):** Apply blurring for noise reduction.
5. **Gaussian Filter (3b):** Apply soft blur for smoothing.

## Implementation Approach

We use Python and the NumPy library to manually perform convolution. Images are converted into matrices, and filters are applied using nested loops. The results are saved as separate images for each filter.

## Files in the Repository

- `mk3.py`: Contains the Python code for applying filters and saving filtered images.
- `Einstein.jpg`: Sample input image (replace with your image).
- `filtered_images`: Directory containing the saved filtered images.

## How to Run

1. Replace `Einstein.jpg` with your input image.
2. Run `mk3.py` to apply filters and save filtered images.
3. Filtered images will be saved in the `filtered_images` directory.

## Conclusion

This project provides a hands-on understanding of image filtering, convolution, and their practical applications. By exploring the effects of various filters, we gain insights into how images can be enhanced and manipulated. Feel free to experiment with different filters and images to further explore the world of image processing.

For questions or feedback, please contact porus.vaid@gmail.com

