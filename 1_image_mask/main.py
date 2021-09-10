import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Считываю картинку, и сохраняю в директорию зелёный канал в качестве изображения
    image = cv.imread('python_image.jpg')
    green_channel = cv.split(image)[1]

    fig, ax = plt.subplots()
    ax.imshow(green_channel, cmap='gray')
    plt.show()

    # Клонирую зелёный канал и нахожу минимальное и максимальное значения
    clone1, clone2 = green_channel.copy(), green_channel.copy()
    min_pixel_value = min(min(green_channel, key=lambda line: min(line)))
    max_pixel_value = max(max(green_channel, key=lambda line: max(line)))
    print(f'Минимальное значение: {min_pixel_value}, максимальное значение: {max_pixel_value}')

    # Преобразование clone1 и clone2 и создание маски
    thresh = np.ubyte((max_pixel_value - min_pixel_value) / 2)
    clone1.fill(thresh)
    clone2.fill(0)
    image_mask = cv.compare(src1=green_channel, src2=clone1, cmpop=cv.CMP_GE)

    # Итоговое изображение
    final_output = cv.subtract(src1=green_channel, src2=thresh/2, mask=image_mask)

    # Картинка без зелёного цвета
    # final_output = cv.subtract(src1=image, src2=thresh/2)

    fig, ax = plt.subplots()
    ax.imshow(final_output, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
