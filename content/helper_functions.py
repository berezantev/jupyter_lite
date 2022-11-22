import numpy as np
import matplotlib.pyplot as plt
import piplite
await piplite.install("ipywidgets")
await piplite.install("ipympl")
import ipywidgets as widgets
%matplotlib widget
%matplotlib inline

N=0.1
x_range = np.linspace(-4, 6)

def f(x):
    return (x-1.5)**2

@widgets.interact(x=(-2, 4, N))
def create_scatter(x=-2):
    fig, ax = plt.subplots(figsize=(5,5))

    # Plot the surface.
    surf = plt.plot(x_range, [f(x) for x in x_range], zorder=1)
    
    plt.scatter(x, f(x), c="red", zorder=2)

    plt.ylim(-1, 20)
   
    
    plt.title("x=%.2f, f(x)=%.2f"%(x, f(x)))
    plt.show()