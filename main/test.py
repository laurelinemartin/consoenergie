import matplotlib.pyplot as plt
SEMAINE = ['Lu', 'Ma', 'Me', 'Je', 'Ve']

v = [5, 10, 15, 20, 25]
w = [15, 20, 30, 16, 13]
SEMAINE = np.arrange

plt.bar(SEMAINE -0.2, v, width=0.5, label='v', color='red')
plt.bar(SEMAINE +0.2, w, width=0.5, label='w', color='blue')
plt.legend()
plt.show()