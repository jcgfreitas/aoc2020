def read(path: str):
    lines = []
    f = open(path, "r")
    for line in f:
        lines.append(line)
    return lines
