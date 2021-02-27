import numpy as np
import matplotlib.pyplot as plt

def SquareWave(n):
    xmin=0;
    xmax=10;

    ymin=-2;
    ymax=2;

    Nx=1000;
    offset=1;

    x=np.linspace(xmin, xmax, Nx);
    y=np.sign(x+n)*offset;

    y[(x<n)]=0;
    y[(x>n+1)]=0;

    plt.plot(x, y);
    plt.axis([xmin, xmax, ymin, ymax]);
    plt.grid()
    plt.show()
    