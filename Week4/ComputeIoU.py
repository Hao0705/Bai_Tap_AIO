def computeIoU(boxA, boxB):
    x_min = max(boxA[0], boxB[0])
    y_min = max(boxA[1], boxB[1])

    x_max = min(boxA[2], boxB[2])
    y_max = min(boxA[3], boxB[3])

    S_intersection = max(0, x_max - x_min + 1) * max(0, y_max - y_min + 1)
    S_boxA = abs(boxA[2] - boxA[0] + 1) * abs(boxA[3] - boxA[1] + 1)
    S_boxB = abs(boxB[2] - boxB[0] + 1) * abs(boxB[3] - boxB[1] + 1)

    S_sum = S_boxB + S_boxA - S_intersection

    return S_intersection / S_sum

