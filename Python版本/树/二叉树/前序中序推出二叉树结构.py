
def cT2(po, io, l):
    if len(io) <= 1 or len(po) <= 1:
        l.append(po[0])
        return

    r = po[0]
    l.append(r)

    for j in range(len(io)):
        if io[j] == r:
            break

    i = 0
    while(po[i] in io[:j+1]):
        i += 1

    cT2(po[1:i], io[:j], l)
    cT2(po[i:], io[j+1:], l)


if __name__ == "__main__":
    l = []
    cT2(['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['C', 'B', 'E', 'D', 'F', 'A', 'G'], l)
    print(l)
