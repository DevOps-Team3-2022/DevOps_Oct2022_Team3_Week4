def hello_world(name):
    if len(name) == 0:
        return "Input string is empty!"        
    elif len(name) > 10:
        return "Input string too long!"
    return f"Hello {name}! Welcome to Hello World File!"
