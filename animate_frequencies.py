import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the WAV file
sample_rate, audio_data = wav.read('audios/Claudia-678607932.wav')

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

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Initialize empty lines for each frequency type
lines = []
for _ in range(len(frequency_types)):
    line, = ax.plot([], [])
    lines.append(line)

# Configure the plot
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Magnitude')
ax.set_title('Real-time Frequency Spectrum')


# Define the update function for the animation
def update(frame):
    # Clear the axis
    ax.clear()

    # Plot the frequency spectra for each frequency type
    for i, freq_type in enumerate(frequency_types):
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
        lines[i].set_data(freq_frequencies, freq_magnitudes)

    # Set the x-axis limits based on the frequency range of interest
    ax.set_xlim(min_freq, max_freq)


# Create the animation
ani = FuncAnimation(fig, update, frames=len(audio_data), interval=10)

# Save the animation as a video
ani.save('frequency_spectrum.mp4')

# Show the final plot
plt.show()
