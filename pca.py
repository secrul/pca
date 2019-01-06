import numpy as np

s = input()
l1 = s.split(' ')
m = int(l1[0])
n = int(l1[1])
k = int(l1[2])
arr = []
for i in range(m):
    s = input()
    li = s.split(',')
    lt = [float(x) for x in li]
    arr.append(lt)
mat = np.mat(arr)
mean = np.mean(mat,axis=0)
mat = mat - mean
c_mat = np.cov(mat.T)

t_v, t_arr = np.linalg.eig(c_mat)
sort_arr = np.argsort(t_v)
mat_t = np.mat(t_arr)
mat_p = np.mat(np.ones((n,k)))
length = len(t_v) - 1
ans_val = []
for i in range(k):
    mat_p[:,i] = mat_t[:,sort_arr[length - i]]
    ans_val.append(t_v[sort_arr[length-i]])
mat_ans = mat*mat_p
for i in range(k - 1):
    print(ans_val[i], end=' ')
print(ans_val[k-1])
for i in range(n):
    for j in range(k - 1):
        print(mat_p[i,j],end=' ')
    print(mat_p[i,k - 1])
for i in range(m):
    for j in range(k - 1):
        print(mat_ans[i,j],end=' ')
    print(mat_ans[i,k - 1])