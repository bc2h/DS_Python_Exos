import matplotlib.pyplot as plt
import numpy as np

#  https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()
#____________________________________________________________

plt.plot([1,2,3,4], [2,4,6,8], 'ro')
plt.axis([0,6,0,10])
plt.show()
#____________________________________________________________

# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()
#____________________________________________________________

# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure()
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()
#____________________________________________________________