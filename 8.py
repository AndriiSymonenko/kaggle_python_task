def menu_is_boring(meals):
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False
