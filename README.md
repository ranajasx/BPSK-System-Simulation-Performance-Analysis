# BPSK-System-Simulation-Performance-Analysis-Python

## Project Overview
This project demonstrates a fundamental digital communication system: Binary Phase Shift Keying (BPSK) modulation over an Additive White Gaussian Noise (AWGN) channel. The core simulation logic for calculating Bit Error Rate (BER) versus Signal-to-Noise Ratio (SNR) has been implemented **independently in Python **.

Highlights:
-   **Versatility in engineering simulation tools:** Proficiency in modern scripting Python.
-   **Deep understanding of communication fundamentals:** Implementing concepts like modulation, channel modeling, detection, and performance analysis from first principles.
-   **Problem-solving and adaptability:** Successfully executing simulations under environmental constraints.
-   **Verification and validation:** Confirming simulation results against theoretical models across different platforms.

## Communication Concepts Demonstrated
-   **Binary Data Generation:** Generating random bit streams.
-   **BPSK Modulation:** Mapping binary bits (0s/1s) to antipodal symbols (-1/+1).
-   **AWGN Channel:** Modeling the additive white Gaussian noise effect on signals.
-   **Coherent Detection:** Recovering transmitted bits using a simple threshold detector.
-   **Bit Error Rate (BER) Calculation:** Quantifying system performance based on bit errors.
-   **Theoretical BER Comparison:** Validating simulated results against the known theoretical BER for BPSK over AWGN.

## Project Files
-   `bpsk_awgn_ber_python.py`: The Python implementation of the BPSK simulation.

**Output:** The simulation progress will print to the console, and a plot showing simulated and theoretical BER curves will appear.


## Expected Results
Both simulations are expected to produce a graph with two curves:
-   A **simulated BER curve** (typically blue circles) which is derived from counting bit errors.
-   A **theoretical BER curve** (typically red dashed line) which is calculated using the complementary error function (erfc/Q-function).

The simulated curve should closely follow the theoretical curve, especially at higher SNR values (lower BERs), confirming the correctness of the implementation.
