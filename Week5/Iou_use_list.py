def compute_iou(box_a, box_b):

    x_a = max(box_a[0], box_b[0])
    y_a = max(box_a[1], box_b[1])

    x_b = min(box_a[2], box_b[2])
    y_b = min(box_a[3], box_b[3])

    a_area = (box_a[2] - box_a[0] + 1) * (box_a[3] - box_a[1] + 1)
    b_area = (box_b[2] - box_b[0] + 1) * (box_b[3] - box_b[1] + 1)

    intersect_area = max(0, x_b - x_a + 1) * max(0, y_b - y_a + 1)

    return intersect_area / (a_area + b_area - intersect_area)

def multi_iou(boxes, scores, iou_threshold):

    sorted_indices = sorted(range(len(scores)), key=lambda k: scores[k], reverse=True)
    keep = []

    while sorted_indices:
        index = sorted_indices.pop(0)
        keep.append(index)

        m = []
        for i in sorted_indices:
            if compute_iou(boxes[index], boxes[i]) < iou_threshold:
                m.append(i)
        sorted_indices = m

    return keep

boxes = [
    [1, 2, 14, 15],
    [3, 4, 10, 11],
    [3, 5, 7, 8,],
    [10, 19, 20, 30],
    [3, 1, 6, 9]
]

scores = [0.3, 0.4, 0.5, 0.7, 0.8]
iou_threshold = 0.1
results = multi_iou(boxes, scores, iou_threshold)

print(results)
