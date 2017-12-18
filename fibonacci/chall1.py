import sys
sys.setrecursionlimit(99999)
def f(n):
    return n if n < 2 else f(n-2) + f(n-1)
print "SECCON{" + str(f(1))[:32] + "}"
print "SECCON{" + str(f(2))[:32] + "}"
print "SECCON{" + str(f(3))[:32] + "}"
#Fibonacci
#SECCON{65076140832331717667772761541872}
#http://php.bubble.ro/fibonacci/
