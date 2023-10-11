import matplotlib.pyplot as plt

# make data
x = [0, 9.23, 38, 64, 70, 97, 101]
y = [4.52, 4.34, 3.8, 3.55, 3.5, 3.19, 2.63]

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

plt.xlabel("$I_{OUT}$ [mA]")
plt.ylabel("$U_{OUT}$ [V]")
plt.grid(True)
plt.xscale('linear')
plt.yscale('linear')
plt.title("Zatěžovací charakteristiku $U_{OUT}$ = f($I_{OUT}$)")
plt.show()
