def elementwise_greater_than(list_, thresh):
    list_one = []
    for i in list_:
        if i > thresh:
            list_one.append(True)
        else:
            list_one.append(False)
    return list_one
