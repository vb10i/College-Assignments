import matplotlib.pyplot as plt
measured_temperature = [42.97, 43.46, 43.88, 43.95, 43.97]
room_temperature = [40,40,40,40,40]
plt.plot(measured_temperature, label = "Measured Temperature", marker = 'o')
plt.plot(room_temperature, label = "Room Temperature", marker = 'o')
plt.xlabel("Measured Temperature")
plt.ylabel("Temperature values")
plt.grid(True)
plt.legend()
plt.title("Observed temperature(t) - Room temperature(r)")
plt.show()
