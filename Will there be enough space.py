def enough(cap, on, wait):
    left_space=cap-on
    if left_space>wait:
        return 0
    else:
        return wait-left_space