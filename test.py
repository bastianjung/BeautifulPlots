import beautiful_plots  # noqa
import matplotlib.pyplot as plt
import numpy as np

# plt.style.use("white_x")
# Create figure with four subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

# 1. Line Chart - Parallel curved lines
x_line = np.linspace(0, 10, 200)
base_curve = np.sin(x_line) * 2
# Create parallel curves with vertical offsets
offsets = np.array([-3, -1.5, 0, 1.5, 3])
for i, offset in enumerate(offsets):
    y = base_curve + offset
    axes[0].plot(x_line, y, label=f"Curve {i + 1} (offset={offset})", linewidth=2)
axes[0].set_title("Parallel Curved Lines", fontsize=14, fontweight="bold")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 2. Scatter Plot - Multiple groups with different colors
np.random.seed(42)
n_points = 50

# Group 1: Positive correlation
x1 = np.random.randn(n_points)
y1 = 2 * x1 + np.random.randn(n_points) * 0.5
sizes1 = 100 * np.random.rand(n_points)

# Group 2: Negative correlation
x2 = np.random.randn(n_points) + 2
y2 = -1.5 * (x2 - 2) + np.random.randn(n_points) * 0.5
sizes2 = 100 * np.random.rand(n_points)

# Group 3: Weak correlation
x3 = np.random.randn(n_points) - 2
y3 = 0.5 * (x3 + 2) + np.random.randn(n_points) * 1.0
sizes3 = 100 * np.random.rand(n_points)

# Group 4: No correlation (random)
x4 = np.random.randn(n_points)
y4 = np.random.randn(n_points)
sizes4 = 100 * np.random.rand(n_points)

axes[1].scatter(
    x1,
    y1,
    s=sizes1,
    alpha=0.6,
    label="Group 1 (positive)",
)
axes[1].scatter(
    x2,
    y2,
    s=sizes2,
    alpha=0.6,
    label="Group 2 (negative)",
)
axes[1].scatter(
    x3,
    y3,
    s=sizes3,
    alpha=0.6,
    label="Group 3 (weak)",
)
axes[1].scatter(
    x4,
    y4,
    s=sizes4,
    alpha=0.6,
    label="Group 4 (random)",
)
axes[1].set_title("Multiple Scatter Groups", fontsize=14, fontweight="bold")
axes[1].set_xlabel("X values")
axes[1].set_ylabel("Y values")
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# 3. Bar Chart - Monthly data with interesting pattern
categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
values = [23, 45, 56, 78, 65, 89, 94, 76]
cmap = plt.get_cmap("dark_beauty_reverse")
colors = [cmap(v / max(values)) for v in values]
axes[2].bar(categories, values, color=colors, linewidth=1.5)
axes[2].set_title("Monthly Performance", fontsize=14, fontweight="bold")
axes[2].set_xlabel("Month")
axes[2].set_ylabel("Value")
axes[2].grid(True, alpha=0.3, axis="y")

# 4. Heatmap - Random gradient field with dark_beauty colormap
heatmap_data = np.random.randn(20, 20)
# Apply a gradient by adding a smooth underlying pattern
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)
heatmap_data += 0.5 * (X + Y)  # Add smooth gradient component

im = axes[3].imshow(heatmap_data, cmap="dark_beauty", interpolation="bilinear")
axes[3].set_title("Random Gradient Field", fontsize=14, fontweight="bold")
axes[3].set_xlabel("X")
axes[3].set_ylabel("Y")
cbar = plt.colorbar(im, ax=axes[3])
cbar.set_label("Magnitude")

plt.tight_layout()
plt.savefig("demo.png", dpi=100)
plt.show()
