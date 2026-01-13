import numpy as np
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def process_signal(data):
    # Simulated Real-time filtering
    b, a = butter_bandpass(8, 30, 256)
    y = lfilter(b, a, data)
    return y

if __name__ == "__main__":
    print("Starting EEG Real-time Pipeline...")
    # Dummy execution
    dummy_data = np.random.random(1000)
    print("Processed signal shape:", process_signal(dummy_data).shape)
