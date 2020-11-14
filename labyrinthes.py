import numpy as np
import igraph
import cv2

def img_to_graph(path):
    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
