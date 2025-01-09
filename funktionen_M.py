import numpy as np
import scipy.signal as sps
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#Butterworth Bandpass Filter für die Filterung
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = sps.butter(order, [low, high], btype='band')
    y = sps.filtfilt(b, a, data)
    return y  

#Butterworth Lowpass Filter für die Bildung der Einhüllenden
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = sps.butter(order, normal_cutoff, btype='low', analog=False)
    y = sps.filtfilt(b, a, data)
    return y

#Funktion zum Gleichrichten des EMG Signals
def rectify(data):
    return np.abs(data)