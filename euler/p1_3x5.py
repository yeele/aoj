def foo(N):
    ans = 0
    for i in range(1, ((N-1)//3)+1):
        ans += (i*3)
        print("i:%s, i*3:%s" % (i, i*3))

    for i in range(1, ((N-1)//5)+1):
        ans += (i*5)
        print("i:%s, i*5:%s" % (i, i*5))
    for i in range(1, ((N-1)//15)+1):
        ans -= (i*15)
        print("i:%s, i*15:%s" % (i, i*15))
    return ans

print(foo(10))
print(foo(1000))