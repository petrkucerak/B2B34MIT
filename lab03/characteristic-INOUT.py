import matplotlib.pyplot as plt

# make data
x = [6, 7, 8, 9, 10, 12, 14, 16, 20]
y = [3.71, 3.77, 3.80, 3.82, 3.84, 3.86, 3.89, 3.91, 3.93]

# plot
fig, ax = plt.subplots()


ax.plot(x, y, linewidth=2.0)

plt.xlabel("$U_{IN}$ [V]")
plt.ylabel("$U_{OUT}$ [V]")
plt.grid(True)
plt.xscale('linear')
plt.yscale('linear')
plt.title("Převodní charakteristiku $U_{OUT}$ = f($U_{IN}$)")
plt.show()
