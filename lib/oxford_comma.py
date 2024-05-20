def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        new_list = " and ".join(items)
        return new_list
    else:
        last_element = items.pop()
        new_list = ", ".join(items) + ", and " + last_element
        return new_list
