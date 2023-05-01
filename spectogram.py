import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as plt

# Load the WAV file
sample_rate, audio_data = wav.read('audios/cc1.wav')

# Convert the audio data to mono if it's in stereo
if audio_data.ndim > 1:
    audio_data = audio_data.mean(axis=1)

# Calculate the spectrogram
nfft = 1024  # Number of points for each block of the FFT
hop_length = 512  # Number of samples to shift the window
frequencies, times, spec = signal.spectrogram(audio_data, fs=sample_rate, nperseg=nfft, noverlap=hop_length)

# Define the frequency types and their ranges
frequency_types = [
    {
        'name': 'Bassline',
        'min_freq': 50,
        'max_freq': 200,
    },
    {
        'name': 'Treble',
        'min_freq': 2000,
        'max_freq': 8000,
    },
    {
        'name': 'Vocal',
        'min_freq': 80,
        'max_freq': 1000,
    },
    {
        'name': 'Percussion',
        'min_freq': 200,
        'max_freq': 5000,
    },
    {
        'name': 'Melody',
        'min_freq': 1000,
        'max_freq': 4000,
    },
    {
        'name': 'Harmonics',
        'min_freq': 500,
        'max_freq': 10000,
    },
    {
        'name': 'High Frequencies',
        'min_freq': 8000,
        'max_freq': 20000,
    },
    # Add more frequency types as needed
]

# Plot the occurrence of frequencies with time
for freq_type in frequency_types:
    min_freq = freq_type['min_freq']
    max_freq = freq_type['max_freq']

    # Find the indices corresponding to the desired frequency range
    freq_indices = np.where((frequencies >= min_freq) & (frequencies <= max_freq))[0]

    # Extract the frequencies and magnitudes for the frequency range
    freq_frequencies = frequencies[freq_indices]
    freq_magnitudes = np.mean(spec[freq_indices, :], axis=0)

    # Plot the frequency occurrence
    plt.plot(times, freq_magnitudes, label=freq_type['name'])

# Configure the plot
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.title('Frequency Occurrence')
plt.legend()

# Show the plot
plt.show()
