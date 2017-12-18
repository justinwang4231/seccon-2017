import sys
def _l(idx, s):
    return s[idx:] + s[:idx]
def main(p, k1, k2):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
    t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
    i1 = 0
    i2 = 0
    c = ""
    print t[25][25][25]
    for a in p:
        c += t[s.find(a)][s.find(k1[i1])][s.find(k2[i2])]
        i1 = (i1 + 1) % len(k1)
        i2 = (i2 + 1) % len(k2)
    return c
print main(sys.argv[1], sys.argv[2], sys.argv[2][::-1])
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
y="SECCON{"
f="POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"
fow=[]
meow=[]
for x in range(len("SECCON{")):
    fow.append(s.index(y[x])-s.index(f[x]))
for x in fow:
    meow.append(x)
for x in fow[::-1]:
    meow.append(x)
for x in range(len(f)):
    print s[(s.find(f[x])+meow[x%len(meow)])%len(s)]
