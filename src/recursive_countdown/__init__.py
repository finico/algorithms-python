def recursive_countdown(i):
    if i < 0:
        return
    else:
        print(i)
        recursive_countdown(i - 1)
