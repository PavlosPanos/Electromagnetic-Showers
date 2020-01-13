import numpy as np
import matplotlib.pyplot as plt 
def random(a,b):
    return (np.random.uniform(low=a, high=b))
x=np.linspace(0,1,10000)
y=[]
for i in range(10000):
    y.append(random(0,1))
plt.plot(x,y)
def N(t):
    return(np.exp(t*np.log(2)))
def E(t,E0):
    return(E0/(2**t))
def tmax(E0,Ec):
    return(np.log(E0/Ec)/np.log(2))
Ec=10**5
E=[]
t=1
N1=[]
tmatrix=[]
Ntotal=np.zeros(1000)
for i in range(100):
    E0=random(10**4,10**8)
    while(t<tmax(E0,Ec)):
        N1.append(N(t))
        t+=1
        E.append(E0/(2**t))
        tmatrix.append(t)
    t=1
    while(t<tmax(E0,Ec)):
        Ntotal[i]+=N1[i]
        t+=1
plt.subplot(2, 1, 1)
plt.plot(tmatrix, N1)
plt.title('Electromagnetic Shower')
plt.ylabel('Ntotal(t)')

plt.subplot(2, 1, 2)
plt.plot(tmatrix, E)
plt.xlabel('time (s)')
plt.ylabel('E(t)')
plt.show()


