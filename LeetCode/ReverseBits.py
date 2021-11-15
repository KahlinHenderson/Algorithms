# Given a 32 bit unsigned integer reverse its bits.
def reverseBits(n):
    times = 32
    rev = []
    while times > 0:
        t = n & 1
        rev.append(t)
        n = n >> 1
        times -= 1
    res = 0
    for i in range(len(rev)):
        res = res << 1
        res = res | rev.pop(i)
    return res
