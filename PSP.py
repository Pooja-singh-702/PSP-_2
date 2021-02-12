import itertools
from itertools import product
n=5
sample_space= list(product(['H','T'],repeat=n))
print(sample_space)
print(len(sample_space))

A = {Head for Head in sample_space  if Head[0] == 'H'}# Head on first tossing
print(A)
print(len(A))

B = { Head for Head in sample_space if Head.count('H') ==2}# two Head
print(B)
print(len(B))

def prob(x):
    return len(x)/len(sample_space)

print(prob(A))
print(prob(B))



"C:\Users\Pooja\New folder (2)\python.exe" C:/Users/Pooja/PycharmProjects/pythonProject6/main.py
[('H', 'H', 'H', 'H', 'H'), ('H', 'H', 'H', 'H', 'T'), ('H', 'H', 'H', 'T', 'H'), ('H', 'H', 'H', 'T', 'T'), ('H', 'H', 'T', 'H', 'H'), ('H', 'H', 'T', 'H', 'T'), ('H', 'H', 'T', 'T', 'H'), ('H', 'H', 'T', 'T', 'T'), ('H', 'T', 'H', 'H', 'H'), ('H', 'T', 'H', 'H', 'T'), ('H', 'T', 'H', 'T', 'H'), ('H', 'T', 'H', 'T', 'T'), ('H', 'T', 'T', 'H', 'H'), ('H', 'T', 'T', 'H', 'T'), ('H', 'T', 'T', 'T', 'H'), ('H', 'T', 'T', 'T', 'T'), ('T', 'H', 'H', 'H', 'H'), ('T', 'H', 'H', 'H', 'T'), ('T', 'H', 'H', 'T', 'H'), ('T', 'H', 'H', 'T', 'T'), ('T', 'H', 'T', 'H', 'H'), ('T', 'H', 'T', 'H', 'T'), ('T', 'H', 'T', 'T', 'H'), ('T', 'H', 'T', 'T', 'T'), ('T', 'T', 'H', 'H', 'H'), ('T', 'T', 'H', 'H', 'T'), ('T', 'T', 'H', 'T', 'H'), ('T', 'T', 'H', 'T', 'T'), ('T', 'T', 'T', 'H', 'H'), ('T', 'T', 'T', 'H', 'T'), ('T', 'T', 'T', 'T', 'H'), ('T', 'T', 'T', 'T', 'T')]
32
{('H', 'H', 'T', 'H', 'H'), ('H', 'H', 'H', 'T', 'H'), ('H', 'H', 'T', 'H', 'T'), ('H', 'H', 'H', 'H', 'T'), ('H', 'H', 'T', 'T', 'H'), ('H', 'H', 'H', 'T', 'T'), ('H', 'T', 'H', 'T', 'H'), ('H', 'T', 'H', 'T', 'T'), ('H', 'T', 'T', 'T', 'H'), ('H', 'H', 'T', 'T', 'T'), ('H', 'T', 'H', 'H', 'H'), ('H', 'T', 'T', 'H', 'H'), ('H', 'T', 'T', 'T', 'T'), ('H', 'T', 'H', 'H', 'T'), ('H', 'T', 'T', 'H', 'T'), ('H', 'H', 'H', 'H', 'H')}
16
{('T', 'T', 'T', 'H', 'H'), ('T', 'T', 'H', 'H', 'T'), ('T', 'H', 'T', 'H', 'T'), ('T', 'T', 'H', 'T', 'H'), ('T', 'H', 'T', 'T', 'H'), ('H', 'T', 'T', 'T', 'H'), ('H', 'H', 'T', 'T', 'T'), ('H', 'T', 'T', 'H', 'T'), ('H', 'T', 'H', 'T', 'T'), ('T', 'H', 'H', 'T', 'T')}
10
0.5
0.3125

Process finished with exit code 0
