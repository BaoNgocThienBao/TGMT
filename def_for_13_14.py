import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def histogram_equalization(image, nbr_bins=256):
    # Đảm bảo hình ảnh đầu vào là ảnh xám
    if image.mode != 'L':
        image = image.convert('L')
    
    # Chuyển đổi hình ảnh thành mảng NumPy
    image_array = np.array(image)

    # Tính toán histogram của ảnh
    histogram, bins = np.histogram(image_array, bins=nbr_bins, range=(0, 256), density=True)

    # Tính toán hàm phân phối tích luỹ (CDF - Cumulative Distribution Function)
    cdf = histogram.cumsum()
    cdf = 255 * cdf / cdf[-1]

    # Lấy giá trị mới cho từng pixel dựa trên CDF
    image_equalized = np.interp(image_array, bins[:-1], cdf)

    # Chuyển đổi mảng kết quả thành hình ảnh
    equalized_image = Image.fromarray(image_equalized.astype('uint8'))

    return equalized_image

def average_images(image_list):
    total_array = np.array(Image.open(image_list[0]), 'f')
    count=1

    for image_path in image_list[1:]:
        try:
            image_array = np.array(Image.open(image_path), 'f')
            total_array += image_array
            count=count+1
        except:
            print("Skip ", image_path);

    # Tính trung bình
    average_array = total_array / count

    # Chuyển đổi kết quả trung bình thành hình ảnh
    average_image = Image.fromarray(average_array.astype('uint8'))

    return average_image