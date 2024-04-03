import bisect
def A(f,a):
    q=bisect.bisect_left(f,a)
    if q:
        if len(f)!=q: f[q]=a
        else: f.append(a)
a,m=[int(input())for _ in range(int(input()))],0
for i in range(len(a)):
    c,d=[a[i]],[-a[i]]
    for t in range(i+1, len(a)):
        A(c,a[t])
        A(d,-a[t])
    m=max(m,len(c)+len(d)-1)
print(m)