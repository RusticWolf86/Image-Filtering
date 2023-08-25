import numpy as np
from PIL import Image

def apply_filter(image_matrix, filter_matrix):
    image_height, image_width = image_matrix.shape
    filter_size = filter_matrix.shape[0]
    padding = filter_size // 2
    filtered_image = np.zeros_like(image_matrix)
    
    for i in range(padding, image_height - padding):
        for j in range(padding, image_width - padding):
            region = image_matrix[i - padding:i + padding + 1, j - padding:j + padding + 1]
            filtered_value = np.sum(region * filter_matrix)
            filtered_image[i, j] = filtered_value
    
    return filtered_image

# Load the image using Pillow
image_path = 'Einstein.jpg'
image = Image.open(image_path)

# Convert the image to a grayscale matrix
image_matrix = np.array(image.convert("L"))

filter_matrix_1e = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

filter_matrix_1f = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 0, 0]
])

filter_matrix_1d = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 0, 0]
])

filter_matrix_1g = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [1, 0, 0]
])

filter_matrix_1c = np.array([
    [0, 0, 1],
    [0, 0, 0],
    [0, 0, 0]
])

filter_matrix_2a = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
])

filter_matrix_2b = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])

avg_filter_matrix = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]) / 9

gaussian_filter_matrix = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
] )/16


# Apply the filter
filtered_image_1e = apply_filter(image_matrix, filter_matrix_1e)
filtered_image_1f = apply_filter(image_matrix, filter_matrix_1f)
filtered_image_1d = apply_filter(image_matrix, filter_matrix_1d)
filtered_image_1g = apply_filter(image_matrix, filter_matrix_1g)
filtered_image_1c = apply_filter(image_matrix, filter_matrix_1c)
filtered_image_2a = apply_filter(image_matrix, filter_matrix_2a)
filtered_image_2b = apply_filter(image_matrix, filter_matrix_2b)
filtered_image_3a = apply_filter(image_matrix, avg_filter_matrix)
filtered_image_3b = apply_filter(image_matrix, gaussian_filter_matrix)

#convert the arry to image (after being filtered)
filtered_image_pil_1e = Image.fromarray(filtered_image_1e, 'L')
filtered_image_pil_1f = Image.fromarray(filtered_image_1f, 'L')
filtered_image_pil_1d = Image.fromarray(filtered_image_1d, 'L')
filtered_image_pil_1g = Image.fromarray(filtered_image_1g, 'L')
filtered_image_pil_1c = Image.fromarray(filtered_image_1c, 'L')
filtered_image_pil_2a = Image.fromarray(filtered_image_2a, 'L')
filtered_image_pil_2b = Image.fromarray(filtered_image_2b, 'L')
filtered_image_pil_3a = Image.fromarray(filtered_image_3a, 'L')
filtered_image_pil_3b = Image.fromarray(filtered_image_3b, 'L')

# Save the filtered image
filtered_image_path_1e = 'filtered_image_1e.jpg'
filtered_image_path_1f = 'filtered_image_1f.jpg'
filtered_image_path_1d = 'filtered_image_1d.jpg'
filtered_image_path_1g = 'filtered_image_1g.jpg'
filtered_image_path_1c = 'filtered_image_1c.jpg'
filtered_image_path_2a = 'filtered_image_2a.jpg'
filtered_image_path_2b = 'filtered_image_2b.jpg'
filtered_image_path_3a = 'filtered_image_Avg_filter.jpg'
filtered_image_path_3b = 'filtered_image_Gaussian_filter.jpg'

filtered_image_pil_1e.save(filtered_image_path_1e)
filtered_image_pil_1f.save(filtered_image_path_1f)
filtered_image_pil_1d.save(filtered_image_path_1d)
filtered_image_pil_1g.save(filtered_image_path_1g)
filtered_image_pil_1c.save(filtered_image_path_1c)
filtered_image_pil_2a.save(filtered_image_path_2a)
filtered_image_pil_2b.save(filtered_image_path_2b)
filtered_image_pil_3a.save(filtered_image_path_3a)
filtered_image_pil_3b.save(filtered_image_path_3b)


print("Filtered image saved as:", filtered_image_path_1e)
print("Filtered image saved as:", filtered_image_path_1f)
print("Filtered image saved as:", filtered_image_path_1d)
print("Filtered image saved as:", filtered_image_path_1g)
print("Filtered image saved as:", filtered_image_path_1c)
print("Filtered image saved as:", filtered_image_path_2a)
print("Filtered image saved as:", filtered_image_path_2b)
print("Filtered image saved as:", filtered_image_path_3a)
print("Filtered image saved as:", filtered_image_path_3b)
