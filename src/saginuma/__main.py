import cv2
import numpy as np

def show_saginuma()-> np.ndarray:
    img = cv2.imread('sample_img.png')
    return img

if __name__ == '__main__':
    img = show_saginuma()
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
