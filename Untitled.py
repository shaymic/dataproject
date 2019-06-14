#!/usr/bin/env python
# coding: utf-8

# In[145]:



q = [
     [[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43], [51, 52, 63]],
     [[74, 75], [84, 85], [94, 95], [104, 105], [114, 115]],
     [[126, 127, 128, 129, 1210], [136, 137, 138, 139, 1310], [146, 147, 148, 149, 1410], [156, 157, 158, 159, 1510], [166, 167, 168, 169, 1610]],
     [[1711], [1811], [1911], [2011], [2111]]
    ]
originalq = q
print("original q:")
print(originalq)
print(" ")

oneone=len(q[0][0])
onetwo=len(q[1][0])
onethree=len(q[2][0])
onefour=len(q[3][0])

q = [[q[j][i] for j in range(len(q))] for i in range(len(q[0]))]
print("output 1 q:")
print(q)
print(" ")
for i, x in enumerate(q): q[i] = [a for b in x for a in b]
print("output 2 q:")
print(q)


# In[73]:


n_vocab=[oneone, onetwo, onethree, onefour]
print (n_vocab)


# In[163]:


def spliter(arr, size):
    arrs = []
    for i in range (len(size)):
        pice = arr[:size[i]]
        arrs.append(pice)
        arr = arr[size[i]:]
    return arrs

n=[3,2,5,1,2]
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(spliter(x, n))


# In[146]:


#print(list(q))
r = []
for i in range(len(q)): r.append(spliter(q[i], n_vocab))

print(list(r))


# In[147]:


r = [[r[j][i] for j in range(len(r))] for i in range(len(r[0]))]
print(r)

