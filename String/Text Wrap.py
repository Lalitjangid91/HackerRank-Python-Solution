def wrap(string, max_width):
    t=''
    while True:
        if not string:
            break
        t=t+string[:max_width]
        t=t+'\n'
        string=string[max_width:]

    return t
