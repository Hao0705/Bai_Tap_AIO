import numpy as np
from Week4.ComputeIoU import computeIoU


def non_max_supperession(boxes, score, iou_threshould):

    keep = np.array([])

    while len(boxes) > 0:
        idx = np.argmax(score)
        score = np.delete(score, idx, axis=0)
        keep = np.vstack([keep, boxes[idx]]) if keep.size else boxes[idx].reshape(1, -1)
        boxes = np.delete(boxes, idx, axis=0)
        max_box = keep[-1]
        idx_delete = []
        for i in range(len(score)):
            if computeIoU(max_box, boxes[i]) > iou_threshould:
                idx_delete.append(i)
        if len(idx_delete):
            boxes = np.delete(boxes, idx_delete, axis=0)
            score = np.delete(score, idx_delete, axis=0)

    return keep

boxes = np.array([
    [12, 84, 140, 212],
    [24, 84, 152, 212],
    [36, 84, 164, 212],
    [12, 96, 140, 224],
    [24, 96, 152, 224],
    [24, 108, 152, 236]
])

score = np.array([0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
iou_threshould = 0.8
keep = non_max_supperession(boxes, score, iou_threshould)

print(keep)
