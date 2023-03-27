import matplotlib.pyplot as plt

# Print the last item from year and pop

print(year[-1])
print(pop[-1])
# Import matplotlib.pyplot as plt


# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

# Display the plot with plt.show()
plt.show()


# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis

plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()



# Change the line plot below to a scatter plot
plt.plot(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale

plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
# Show plot
plt.show()