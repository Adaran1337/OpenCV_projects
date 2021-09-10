import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Считываю картинку, и сохраняю в директорию зелёный канал в качестве изображения
    image = cv.imread('python_image.jpg')
    green_channel = cv.split(image)[1]
    cv.imwrite('green_channel.jpg', green_channel)

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
    cv.compare(green_channel, clone1, cv.CMP_GE, clone2)

    # Итоговое изображение
    image_mask = cv.subtract(green_channel, thresh/2, clone2)

    # Картинка без зелёного цвета
    # image_mask = cv.subtract(image, thresh/2, clone2)

    fig, ax = plt.subplots()
    ax.imshow(image_mask, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
