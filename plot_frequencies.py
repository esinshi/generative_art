import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Load the WAV file
sample_rate, audio_data = wav.read('audios/cc1.wav')

# Convert the audio data to mono if it's in stereo
if audio_data.ndim > 1:
    audio_data = audio_data.mean(axis=1)

# Perform the Fourier Transform on the audio data
frequencies = np.fft.fft(audio_data)
frequencies = np.abs(frequencies)

# Generate the frequency axis
frequency_axis = np.fft.fftfreq(len(frequencies), 1.0 / sample_rate)

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

# Plot the frequency spectra for each frequency type
for freq_type in frequency_types:
    min_freq = freq_type['min_freq']
    max_freq = freq_type['max_freq']

    # Find the indices corresponding to the desired frequency range
    freq_indices = np.where(
        (frequency_axis >= min_freq) & (frequency_axis <= max_freq)
    )

    # Extract the frequencies and magnitudes for the frequency range
    freq_frequencies = frequency_axis[freq_indices]
    freq_magnitudes = frequencies[freq_indices]

    # Plot the frequency spectrum
    plt.plot(freq_frequencies, freq_magnitudes, label=freq_type['name'])

# Configure the plot
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')
plt.legend()

# Show the plot
plt.show()
