for x in np.arange(-2,1,0.05):
    for y in np.arange(-1,1,0.05):
        c = x + 1j*y;
        z = 0.2;
        for i in range(10):
            z = z*z + c;
        if np.abs(z) < 1:
            plt.plot(x,y,marker='o', markerfacecolor=[np.abs(z),0,0],markeredgecolor = [1,1,1])
