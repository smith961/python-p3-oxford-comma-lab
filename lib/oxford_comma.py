def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    elif len(items) > 2:
        return ", ".join(items[:-1]) + ", and " + items[-1]
    else:
        return None