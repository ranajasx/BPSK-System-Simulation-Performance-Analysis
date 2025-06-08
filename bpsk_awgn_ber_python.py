# bpsk_awgn_ber_python.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf


def bpsk_awgn_ber_simulation(num_bits_per_snr, snr_db_range):
    ber_simulated = []
    ber_theoretical = []

    print("Starting BPSK over AWGN BER simulation in Python...")

    for snr_db in snr_db_range:
        snr_linear = 10 ** (snr_db / 10)  # Convert SNR from dB to linear

        # 1. Data Generation (Binary)
        input_bits = np.random.randint(0, 2, num_bits_per_snr)  # Generate random binary bits (0s and 1s)

        # 2. BPSK Modulation (Mapping 0->-1, 1->+1)
        # Assuming unit energy per bit (Eb=1) for modulated symbols
        modulated_symbols = 2 * input_bits - 1  # Maps 0 to -1, 1 to +1

        # 3. AWGN Channel Simulation
        # Noise power calculation: Noise_Power = Eb / SNR_linear
        # Since Eb = 1, Noise_Power = 1 / SNR_linear
        noise_variance = 1 / snr_linear
        noise_std_dev = np.sqrt(noise_variance / 2)  # Standard deviation for real/imaginary parts of noise

        # Generate real Gaussian noise
        noise = noise_std_dev * np.random.randn(num_bits_per_snr)

        # Add noise to the signal
        received_signal = modulated_symbols + noise

        # 4. BPSK Demodulation (Coherent Detection)
        # Simple threshold detector (0) for -1/+1 symbols
        detected_bits = (received_signal > 0).astype(int)  # If received > 0, decide 1; else 0

        # 5. Calculate Bit Error Rate (BER)
        num_bit_errors = np.sum(input_bits != detected_bits)
        simulated_ber = num_bit_errors / num_bits_per_snr
        ber_simulated.append(simulated_ber)

        # 6. Calculate Theoretical BER for BPSK over AWGN
        # BER_theoretical = Q(sqrt(2 * Eb/No))
        # Q(x) = 0.5 * erfc(x / sqrt(2))  AND erfc(x) = 1 - erf(x)
        # So, BER_theoretical = 0.5 * (1 - erf(sqrt(Eb/No)))
        # Here, Eb/No = SNR_linear
        theoretical_ber = 0.5 * (1 - erf(np.sqrt(snr_linear)))  # Using erf from scipy.special

        ber_theoretical.append(theoretical_ber)

        print(f"SNR = {snr_db} dB, Simulated BER = {simulated_ber:.2e}, Theoretical BER = {theoretical_ber:.2e}")

    # 7. Plotting BER Curve
    plt.figure()
    plt.semilogy(snr_db_range, ber_simulated, 'bo-', label='Simulated BPSK')
    plt.semilogy(snr_db_range, ber_theoretical, 'r--', label='Theoretical BPSK')
    plt.xlabel('SNR (Eb/No in dB)')
    plt.ylabel('Bit Error Rate (BER)')
    plt.title('BPSK Modulation over AWGN Channel')
    plt.grid(True, which="both")
    plt.ylim(1e-5, 1)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    num_bits = 100000  # Number of bits to simulate
    snr_range_db = np.arange(0, 13, 2)  # SNR range from 0 to 12 dB in steps of 2

    bpsk_awgn_ber_simulation(num_bits, snr_range_db)