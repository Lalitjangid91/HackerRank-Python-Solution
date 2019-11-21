def capitalize(string):
    string=" ".join((s.capitalize() for s in string.strip().split(" ")))
    return string
