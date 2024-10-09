#Biquad filter calculator graph and output for pure data
#Dr. Martin Jaroszewicz PhD ©2024 Wandersound Interactive Audio

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

def calculate_response(a0, a1, a2, b1, b2, fs, num_points=1000):
    freq = np.logspace(np.log10(20), np.log10(20000), num_points)
    omega = 2 * np.pi * freq / fs
    z = np.exp(-1j * omega)
    H = (a0 + a1 * z**-1 + a2 * z**-2) / (1 + b1 * z**-1 + b2 * z**-2)
    
    # Avoid log of zero
    abs_H = np.abs(H)
    min_value = 1e-10
    safe_H = np.where(abs_H > min_value, abs_H, min_value)
    
    mag_db = 20 * np.log10(safe_H)
    phase = np.angle(H)
    return freq / 1000, mag_db, phase  # Convert Hz to kHz

def plot_response(freq, mag_db, phase):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    
    ax1.semilogx(freq, mag_db)
    ax1.set_xlabel('Frequency [kHz]')
    ax1.set_ylabel('Magnitude [dB]')
    ax1.set_title('Magnitude Response')
    ax1.grid(True)
    ax1.set_xlim(0.02, 20)
    ax1.xaxis.set_major_formatter(formatter)
    
    ax2.semilogx(freq, np.degrees(phase))
    ax2.set_xlabel('Frequency [kHz]')
    ax2.set_ylabel('Phase [degrees]')
    ax2.set_title('Phase Response')
    ax2.grid(True)
    ax2.set_xlim(0.02, 20)
    ax2.xaxis.set_major_formatter(formatter)
    
    xticks = [0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20]
    ax1.set_xticks(xticks)
    ax2.set_xticks(xticks)
    
    plt.tight_layout()
    plt.show()

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("Enter the biquad filter coefficients:")
    a0 = get_float_input("a0: ")
    a1 = get_float_input("a1: ")
    a2 = get_float_input("a2: ")
    b1 = get_float_input("b1: ")
    b2 = get_float_input("b2: ")
    
    fs = get_float_input("Enter the sampling frequency (Hz): ")

    # Output coefficients in Pure Data order (b1 b2 a0 a1 a2)
    print("\nCoefficients in Pure Data order (-b1 -b2 a0 a1 a2):")
    print(f"biquad~ {-b1:.6f} {-b2:.6f} {a0:.6f} {a1:.6f} {a2:.6f}")

    freq, mag_db, phase = calculate_response(a0, a1, a2, b1, b2, fs)
    plot_response(freq, mag_db, phase)

    