import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("project132/c132Data.csv")

mass_data = data["Mass"].to_list()
radius_data = data["Radius"].to_list()
gravity_data = data["Gravity"].to_list()
distance_data = data["Distance"].to_list()

# combined_data = list(zip(mass_data,radius_data,gravity_data))
# combined_data.sort(key=lambda x:x[0])

# sorted_mass_data, sorted_radius_data, sorted_gravity_data = zip(*combined_data)

mass_data.sort()
radius_data.sort()
gravity_data.sort()



plt.plot(radius_data,mass_data)
plt.title("Radius vs Mass")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()


plt.plot(mass_data,gravity_data)
plt.title("Mass vs Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()

plt.scatter(radius_data,mass_data)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()






