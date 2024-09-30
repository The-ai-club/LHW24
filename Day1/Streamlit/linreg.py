import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to generate data points
def generate_data(n_points=100):
    np.random.seed(42)
    X = np.linspace(0, 10, n_points)
    noise = np.random.randn(n_points) * 2
    y_true = 2 * X + 5 + noise  # True line: y = 2X + 5 with some noise
    return X, y_true

# Streamlit sidebar sliders
st.sidebar.title("Linear Regression Parameters")
weight = st.sidebar.slider("Weight (Slope)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
bias = st.sidebar.slider("Bias (Intercept)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# Generate synthetic data
X, y_true = generate_data()

# Predicted line
y_pred = weight * X + bias

# Streamlit app layout
st.title("Linear Regression Visualization")
st.write("Use the sliders in the sidebar to adjust the weight (slope) and bias (intercept) of the regression line.")

# Plot the data points and regression line
plt.figure(figsize=(8, 6))
plt.scatter(X, y_true, label="Data Points", color="blue", alpha=0.7)
plt.plot(X, y_pred, label=f"Predicted Line: y = {weight:.2f}x + {bias:.2f}", color="red", linewidth=2)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)

# Display plot in Streamlit
st.pyplot(plt)

# Display metrics for visual clarity
st.write(f"**Equation of the line**: y = {weight:.2f}x + {bias:.2f}")
