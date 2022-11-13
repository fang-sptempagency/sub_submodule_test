import cv2
import numpy as np

def show_saginuma(img:np.ndarray)-> np.ndarray:
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return img

if __name__ == '__main__':
    img = show_saginuma()
