import numpy as np
from scipy import fftpack
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import Lab3Functions as lf3
import funktionen_M as fm
import json

#Importiern der Daten von Matti: Weights, MVC und Fatigue
weights_01, mvc_01, fatigue_01 = lf3.import_data(';')
#Extrahieren der Zeit
time_weights_01 = weights_01['time']
time_mvc_01 = mvc_01['time'] / 1000 #Umwandlung in Sekunden
time_fatigue_01 = fatigue_01['time']
#Extrahieren der EMG Daten
weights_01 = weights_01['emg']
mvc_01 = mvc_01['emg'] 
fatigue_01 = fatigue_01['emg']


#Importierung der Daten von Markus: MVC
mvc_02 = lf3.import_mvc('Markus', ';')
#Extrahierung der Zeit
time_mvc_02 = mvc_02['time'] / 1000 #Umwandlung in Sekunden
#Extrahierung der EMG Daten
mvc_02 = mvc_02['emg']

#Importierung der Daten von Jannis: MVC
mvc_03 = lf3.import_mvc('Jannis', ';')
#Extrahierung der Zeit
time_mvc_03 = mvc_03['time'] / 1000 #Umwandlung in Sekunden
#Extrahierung der EMG Daten
mvc_03 = mvc_03['emg']

#Entgernen des Offsets bei den MVC-Daten
mvc_01 = lf3.offset_correction(mvc_01)
mvc_02 = lf3.offset_correction(mvc_02)
mvc_03 = lf3.offset_correction(mvc_03)
weights_01 = lf3.offset_correction(weights_01)
fatigue_01 = lf3.offset_correction(fatigue_01)

#Plotten der MVC-Daten mit dem Korrigierten Offset
# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 20))
# #Plotten MVC-Daten von Matti
# ax1.plot(time_mvc_01, mvc_01, label='Matti')
# ax1.set_title('MVC-Daten Matti')
# ax1.set(xlabel='Time [s]', ylabel='ECG [mV]')
# #Plotten MVC-Daten von Markus
# ax2.plot(time_mvc_02, mvc_02, label='Markus')
# ax2.set_title('MVC-Daten Markus')
# ax2.set(xlabel='Time [s]', ylabel='ECG [mV]')
# #Plotten MVC-Daten von Jannis
# ax3.plot(time_mvc_03, mvc_03, label='Jannis')
# ax3.set_title('MVC-Daten Jannis')
# ax3.set(xlabel='Time [s]', ylabel='ECG [mV]')

mvc_01_filtered = fm.butter_bandpass_filter(mvc_01, 20, 450, 1000, 5)
mvc_02_filtered = fm.butter_bandpass_filter(mvc_02, 20, 450, 1000, 5)
mvc_03_filtered = fm.butter_bandpass_filter(mvc_03, 20, 450, 1000, 5)
weights_01_filtered = fm.butter_bandpass_filter(weights_01, 20, 450, 1000, 5)
fatigue_01_filtered = fm.butter_bandpass_filter(fatigue_01, 20, 450, 1000, 5)

#Plotten der gefilterten MVC-Daten
# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 20))
# #Plotten MVC-Daten von Matti
# ax1.plot(time_mvc_01, mvc_01_filtered, label='Matti')
# ax1.set_title('MVC-Daten Matti')
# ax1.set(xlabel='Time [s]', ylabel='ECG [mV]')
# #Plotten MVC-Daten von Markus
# ax2.plot(time_mvc_02, mvc_02_filtered, label='Markus')
# ax2.set_title('MVC-Daten Markus')
# ax2.set(xlabel='Time [s]', ylabel='ECG [mV]')
# #Plotten MVC-Daten von Jannis
# ax3.plot(time_mvc_03, mvc_03_filtered, label='Jannis')
# ax3.set_title('MVC-Daten Jannis')
# ax3.set(xlabel='Time [s]', ylabel='ECG [mV]')

mvc_01_rectified = np.abs(mvc_01_filtered)
mvc_02_rectified = np.abs(mvc_02_filtered)
mvc_03_rectified = np.abs(mvc_03_filtered)
weights_01_rectified = np.abs(weights_01_filtered)
fatigue_01_rectified = np.abs(fatigue_01_filtered)

#Plotten der gleichgerichteten MVC-Daten
# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 20))
# #Plotten MVC-Daten von Matti
# ax1.plot(time_mvc_01, mvc_01_rectified, label='Matti')
# ax1.set_title('MVC-Daten Matti')
# ax1.set(xlabel='Time [s]', ylabel='ECG [mV]')
# #Plotten MVC-Daten von Markus
# ax2.plot(time_mvc_02, mvc_02_rectified, label='Markus')
# ax2.set_title('MVC-Daten Markus')
# ax2.set(xlabel='Time [s]', ylabel='ECG [mV]')
# #Plotten MVC-Daten von Jannis
# ax3.plot(time_mvc_03, mvc_03_rectified, label='Jannis')
# ax3.set_title('MVC-Daten Jannis')
# ax3.set(xlabel='Time [s]', ylabel='ECG [mV]')

mvc_01_envelope = fm.butter_lowpass_filter(mvc_01_rectified, 3, 1000, 5)
mvc_02_envelope = fm.butter_lowpass_filter(mvc_02_rectified, 3, 1000, 5)
mvc_03_envelope = fm.butter_lowpass_filter(mvc_03_rectified, 3, 1000, 5)
weights_01_envelope = fm.butter_lowpass_filter(weights_01_rectified, 3, 1000, 5)
fatigue_01_envelope = fm.butter_lowpass_filter(fatigue_01_rectified, 3, 1000, 5)

# #Plotten der Einhüllenden der MVC-Daten
# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 20))
# #Plotten MVC-Daten von Matti
# ax1.plot(time_mvc_01, mvc_01_envelope, label='Matti')
# ax1.set_title('MVC-Daten Matti')
# ax1.set(xlabel='Time [s]', ylabel='EMG [mV]')
# #Plotten MVC-Daten von Markus
# ax2.plot(time_mvc_02, mvc_02_envelope, label='Markus')
# ax2.set_title('MVC-Daten Markus')
# ax2.set(xlabel='Time [s]', ylabel='EMG [mV]')
# #Plotten MVC-Daten von Jannis
# ax3.plot(time_mvc_03, mvc_03_envelope, label='Jannis')
# ax3.set_title('MVC-Daten Jannis')
# ax3.set(xlabel='Time [s]', ylabel='EMG [mV]')

# #Plotten der MVC- Daten eines Gruppenmitglieds
# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20, 20))
# #Plotten der gefilterten MVC-Daten
# ax1.plot(time_mvc_02, mvc_02_filtered)
# ax1.set_title('Gefilterte MVC-Daten')
# ax1.set(xlabel='Time [s]', ylabel='EMG [mV]')
# #Plotten gleichgerichteten MVC-Daten
# ax2.plot(time_mvc_02, mvc_02_rectified)
# ax2.set_title('Gleichgerichtete MVC-Daten')
# ax2.set(xlabel='Time [s]', ylabel='EMG [mV]')
# #Plotten der Einhüllenden der MVC-Daten
# ax3.plot(time_mvc_02, mvc_02_envelope)
# ax3.set_title('Einhüllende der MVC-Daten')
# ax3.set(xlabel='Time [s]', ylabel='EMG [mV]')

# Aktivitätsphasen von Matti
# plt.ion()
# mvc_01_s, mvc_01_e, weights_01_s, weights_01_e, fatigue_01_s, fatigue_01_e = lf3.get_bursts(mvc_01_filtered, weights_01_filtered, fatigue_01_filtered)
# plt.ioff()

# # Aktivitätsphasen von Markus
# plt.ion()
# mvc_02_s, mvc_02_e, _, _, _, _ = lf3.get_bursts(mvc_02_filtered, weights_01_filtered, fatigue_01_filtered)
# plt.ioff()

# # Aktivitätsphasen von Jannis
# plt.ion()
# mvc_03_s, mvc_03_e, _, _, _, _ = lf3.get_bursts(mvc_03_filtered, weights_01_filtered, fatigue_01_filtered)
# plt.ioff()

# Daten in ein Dictionary speichern
# bursts_data = {
#     "Matti": {
#         "mvc_start": mvc_01_s.tolist(),
#         "mvc_end": mvc_01_e.tolist(),
#         "weights_start": weights_01_s.tolist(),
#         "weights_end": weights_01_e.tolist(),
#         "fatigue_start": fatigue_01_s.tolist(),
#         "fatigue_end": fatigue_01_e.tolist()
#     },
#     "Markus": {
#         "mvc_start": mvc_02_s.tolist(),
#         "mvc_end": mvc_02_e.tolist()
#     },
#     "Jannis": {
#         "mvc_start": mvc_03_s.tolist(),
#         "mvc_end": mvc_03_e.tolist()
#     }
# }


#Aufgabe 9
# Daten in eine JSON-Datei schreiben
fatigue_start_time = [37, 5730, 12450]
fatigue_end_time = [5550, 12100, 18450]
fatigue_start_time = np.array(fatigue_start_time)
fatigue_end_time = np.array(fatigue_end_time)

# Define the segment length
segment_length = 500  # 500 milliseconds

# Initialize a figure for plotting
fig, axs = plt.subplots(3, 3, figsize=(8, 8))
fig.suptitle('Spektrale Leistungsdichte der Fatigue-Daten', y=1.02)

# Loop through each burst and extract 3 segments
for i, (start, end) in enumerate(zip(fatigue_start_time, fatigue_end_time)):
    # Calculate positions for the segments
    total_length = end - start
    positions = [start, start + total_length // 2 - segment_length // 2, end - segment_length]

    # Extract the segments
    segments = [fatigue_01_rectified[pos:pos + segment_length] for pos in positions]

    # Plot the power spectral density for each segment
    for j, segment in enumerate(segments):
        sLd_power, sLd_frequency = lf3.get_power(segment, 1000)
        ax = axs[i, j]
        ax.plot(sLd_frequency, sLd_power)
        ax.set_title(f'Burst {i+1}, Segment {j+1}', fontsize=8)
        ax.set_xlabel('Frequenz (Hz)', fontsize=6)
        ax.set_ylabel('Leistungsdichte', fontsize=6)
        ax.tick_params(axis='both', which='major', labelsize=6)

# Plot Burst 2 Segment 1 in a larger plot
burst_index = 1
segment_index = 0
segment = segments[segment_index]
sLd_power, sLd_frequency = lf3.get_power(segment, 1000)

# Filter the segment with a lowpass filter at 40 Hz
filtered_segment = fm.butter_lowpass_filter(segment, 40, 1000, 5)

# Calculate the average frequency
average_frequency = np.sum(sLd_frequency * sLd_power) / np.sum(sLd_power)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(sLd_frequency, sLd_power, label='Spektrale Leistungsdichte')
ax.plot(sLd_frequency, fm.butter_lowpass_filter(sLd_power, 40, 1000, 5), 'r--', label='Gefiltertes Signal (40 Hz)')
ax.axvline(average_frequency, color='g', linestyle=':', label=f'Durchschnittliche Frequenz: {average_frequency:.2f} Hz')
ax.set_title('Burst 2, Segment 1 - Spektrale Leistungsdichte', fontsize=12)
ax.set_xlabel('Frequenz (Hz)', fontsize=10)
ax.set_ylabel('Leistungsdichte', fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)
ax.legend()

plt.tight_layout()
plt.show()



# Aufgabe 10
# Plotten der gefilterten Signale von Burst 2 übereinander mit Cutoff von 40 Hz

# Extract the segments for Burst 2
burst_2_start = fatigue_start_time[1]
burst_2_end = fatigue_end_time[1]
total_length_burst_2 = burst_2_end - burst_2_start
positions_burst_2 = [burst_2_start, burst_2_start + total_length_burst_2 // 2 - segment_length // 2, burst_2_end - segment_length]
segments_burst_2 = [fatigue_01_rectified[pos:pos + segment_length] for pos in positions_burst_2]

# Initialize a figure for plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each segment
colors = ['blue', 'green', 'red']
line_styles = ['-', '--', ':']
for j, (segment, color, line_style) in enumerate(zip(segments_burst_2, colors, line_styles)):
    sLd_power, sLd_frequency = lf3.get_power(segment, 1000)
    filtered_power = fm.butter_lowpass_filter(sLd_power, 40, 1000, 5)
    ax.plot(sLd_frequency, filtered_power, label=f'Segment {j+1}', color=color, linestyle=line_style)

    # Calculate and plot the median frequency for each segment
    cumulative_power = np.cumsum(sLd_power)
    median_frequency = sLd_frequency[np.searchsorted(cumulative_power, cumulative_power[-1] / 2)]
    ax.axvline(median_frequency, linestyle=line_style, color=color, label=f'Median Frequenz Segment {j+1}: {median_frequency:.2f} Hz')

# Set plot title and labels
ax.set_title('Burst 2 - Vergleich von gefilterter Spektrale Leistungsdichte ', fontsize=12)
ax.set_xlabel('Frequenz (Hz)', fontsize=10)
ax.set_ylabel('Leistungsdichte', fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)
ax.legend()

plt.tight_layout()
plt.show()


#Aufgabe 11
# Aufgabe 11
# Plotten der Medianfrequenz für jeden Burst und seine Segmente

# Initialize a figure for plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Define line styles for each burst
line_styles = ['-', '--', ':']
colors = ['blue', 'green', 'red']

# Loop through each burst
for i, (start, end) in enumerate(zip(fatigue_start_time, fatigue_end_time)):
    # Calculate positions for the segments
    total_length = end - start
    positions = [start, start + total_length // 2 - segment_length // 2, end - segment_length]

    # Extract the segments
    segments = [fatigue_01_rectified[pos:pos + segment_length] for pos in positions]

    # Calculate and plot the median frequency for each segment
    median_frequencies = []
    time_points = []
    for pos, segment in zip(positions, segments):
        sLd_power, sLd_frequency = lf3.get_power(segment, 1000)
        cumulative_power = np.cumsum(sLd_power)
        median_frequency = sLd_frequency[np.searchsorted(cumulative_power, cumulative_power[-1] / 2)]
        median_frequencies.append(median_frequency)
        time_points.append((pos - start) / total_length)

    # Plot the median frequencies for the burst
    ax.plot(time_points, median_frequencies, label=f'Burst {i+1}', linestyle=line_styles[i], color=colors[i], marker='o')

# Set plot title and labels
ax.set_title('Medianfrequenz der Segmente für jeden Burst', fontsize=12)
ax.set_xlabel('Messzeitpunkte (in Prozent)', fontsize=10)
ax.set_ylabel('Medianfrequenz (Hz)', fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)
ax.legend()

plt.tight_layout()
plt.show()






