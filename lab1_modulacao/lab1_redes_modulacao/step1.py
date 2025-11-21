from functions import encode_nrz, encode_manchester, plot_signal
from configs import SAMPLE_RATE
import sounddevice as sd

test_bits = "11001"
print(f"Dados originais: {test_bits}\n")

# Testa cada modulação
print("1. NRZ:")
nrz_signal = encode_nrz(test_bits,debug=True)

print("\n3. Manchester:")
manchester_signal = encode_manchester(test_bits,debug=True)

sd.play(manchester_signal, SAMPLE_RATE)
sd.wait()

sd.play(nrz_signal, SAMPLE_RATE)
sd.wait()

plot_signal(nrz_signal,'NRZ',len(test_bits))