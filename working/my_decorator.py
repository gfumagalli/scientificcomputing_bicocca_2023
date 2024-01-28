import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
from matplotlib import rc

def my_decorator(func):
    def wrapper(*args, **kwargs):
        #print("Hi! This is before")
        plt.rcParams.update({"text.usetex": True})
        plt.rcParams['xtick.labelsize'] = 17
        plt.rcParams['ytick.labelsize'] = 17
        plt.rcParams['ytick.left'] = True
        plt.rcParams['ytick.right'] = True
        plt.rcParams['xtick.top'] = True
        plt.rcParams['xtick.bottom'] = True
        plt.rcParams['ytick.labelleft'] = True
        plt.rcParams['ytick.labelright'] = False
        plt.rcParams['xtick.labeltop'] = False
        plt.rcParams['xtick.labelbottom'] = True
        font = {'size' : 17}
        rc('font', **font)
        rc('text',usetex=True)
        f = func(*args, **kwargs)
        #print("Hi again! This is after")     
        ax = plt.gca() 
        plt.minorticks_on()

        return f

    return wrapper

