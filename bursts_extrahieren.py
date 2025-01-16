import numpy as np
from scipy import fftpack
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import Lab3Functions as lf3

def extrakt_bursts(mvc_filtered, weights_filtered, fatigue_filtered):
    plt.ion
    mvc_s, mvc_e, weights_s, weights_e, fatigue_s, fatigue_e = lf3.get_bursts(mvc_filtered, weights_filtered, fatigue_filtered)
    plt.ioff()
    return mvc_s, mvc_e, weights_s, weights_e, fatigue_s, fatigue_e


