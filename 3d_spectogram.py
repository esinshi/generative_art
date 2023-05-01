import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the WAV file
sample_rate, audio_data = wav.read('audios/cc1.wav')

# Convert the audio data to mono if it's in stereo
if audio_data.ndim > 1:
    audio_data = audio_data.mean(axis=1)

# Calculate the spectrogram
nfft = 1024  # Number of points for each block of the FFT
hop_length = 512  # Number of samples to shift the window
frequencies, times, spec = signal.spectrogram(audio_data, fs=sample_rate, nperseg=nfft, noverlap=hop_length)

# Plot the spectrogram in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
time_mesh, freq_mesh = np.meshgrid(times, frequencies)
ax.plot_surface(time_mesh, freq_mesh, 10 * np.log10(spec), cmap='viridis')

# Set the labels and title
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frequency (Hz)')
ax.set_zlabel('Magnitude (dB)')
ax.set_title('Spectrogram')

# Show the plot
plt.show()
