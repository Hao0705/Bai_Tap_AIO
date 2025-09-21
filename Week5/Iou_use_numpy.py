import numpy as np

def non_maxima_suppression(boxes, scores, threshold):

    x_min = boxes[:, 0]
    y_min = boxes[:, 1]
    x_max = boxes[:, 2]
    y_max = boxes[:, 3]

    areas = (x_max - x_min + 1) * (y_max - y_min + 1)
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)

        xx1 = np.maximum(x_min[i], x_min[order[1:]])
        yy1 = np.maximum(y_min[i], y_min[order[1:]])

        xx2 = np.minimum(x_max[i], x_max[order[1:]])
        yy2 = np.minimum(y_max[i], y_max[order[1:]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        intersection = w * h
        iou = intersection / (areas[i] + areas[order[1:]] - intersection)

        inds = np.where(iou <= threshold)[0]
        order = order[inds + 1]

    return keep


boxes = np.array([
    [1, 2, 14, 15],
    [3, 4, 10, 11],
    [3, 5, 7, 8, ],
    [10, 19, 20, 30],
    [3, 1, 6, 9]
])
