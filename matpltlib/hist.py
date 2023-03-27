import matplotlib.pyplot as plt
# Build histogram with 5 bins
plt.hist(life_exp, 5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, 20)

# Show and clean up again
plt.show()
plt.clf()


# Histogram of life_exp, 15 bins

plt.hist(life_exp,15)
# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950,15)

# Show and clear plot again
plt.show()
plt.clf()