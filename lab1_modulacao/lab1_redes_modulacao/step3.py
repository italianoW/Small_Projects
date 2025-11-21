from functions import encode_nrz, decode_nrz, adicionar_ruido, encode_manchester, decode_manchester
import numpy as np
import matplotlib.pyplot as plt

original_bits = "00111000"
snr = -3

clean_signal = encode_nrz(original_bits)
noisy_signal = adicionar_ruido(clean_signal, snr)
decoded = decode_nrz(noisy_signal, len(original_bits))

print(f"  Original: {original_bits}")
print(f"  Decodificado: {decoded}")
print(f"  Correto: {original_bits == decoded}\n")

mensagem_bits = "0011000101001001111"
num_bits = len(mensagem_bits)

modulacoes = {
    "NRZ": (encode_nrz, decode_nrz),
    "Manchester": (encode_manchester, decode_manchester)
}

SNR_values = np.arange(20, -201, -1)
resultados = {}

print("\n==== MODULAÇÃO NRZ ====")

# Parte 1: preparação
sinal_limpo_nrz = encode_nrz(mensagem_bits)
num_erros_nrz = []
primeiros_nrz = None
todos_nrz = None
bits_comprometidos_nrz = np.zeros(num_bits, dtype=bool)

# Parte 2: simulação
for snr_val in SNR_values:

    sinal_ruidoso = adicionar_ruido(sinal_limpo_nrz, snr_val)
    mensagem_decodificada = decode_nrz(sinal_ruidoso, num_bits)

    erros = 0
    for i in range(num_bits):
        if mensagem_decodificada[i] != mensagem_bits[i]:
            erros += 1
            bits_comprometidos_nrz[i] = True

    num_erros_nrz.append(erros)

    if primeiros_nrz is None and erros > 0:
        primeiros_nrz = snr_val

    if todos_nrz is None and np.all(bits_comprometidos_nrz):
        todos_nrz = snr_val

print(f"  a) Primeiros erros em: {primeiros_nrz} dB")
print(f"  b) Todos os bits comprometidos em: {todos_nrz} dB")

print("\n==== MODULAÇÃO MANCHESTER ====")

# Parte 1: preparação
sinal_limpo_man = encode_manchester(mensagem_bits)
num_erros_man = []
primeiros_man = None
todos_man = None
bits_comprometidos_man = np.zeros(num_bits, dtype=bool)

# Parte 2: simulação
for snr_val in SNR_values:

    sinal_ruidoso = adicionar_ruido(sinal_limpo_man, snr_val)
    mensagem_decodificada = decode_manchester(sinal_ruidoso, num_bits)

    erros = 0
    for i in range(num_bits):
        if mensagem_decodificada[i] != mensagem_bits[i]:
            erros += 1
            bits_comprometidos_man[i] = True

    num_erros_man.append(erros)

    if primeiros_man is None and erros > 0:
        primeiros_man = snr_val

    if todos_man is None and np.all(bits_comprometidos_man):
        todos_man = snr_val

print(f"  a) Primeiros erros em: {primeiros_man} dB")
print(f"  b) Todos os bits comprometidos em: {todos_man} dB")

# Gráficos
plt.figure(figsize=(10, 5))
plt.plot(SNR_values, num_erros_nrz, label="NRZ")
plt.xlabel("SNR (dB)")
plt.ylabel("Número de erros")
plt.title("NRZ — Erros x SNR")
plt.grid(True)
plt.gca().invert_xaxis()
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(SNR_values, num_erros_man, label="Manchester")
plt.xlabel("SNR (dB)")
plt.ylabel("Número de erros")
plt.title("Manchester — Erros x SNR")
plt.grid(True)
plt.gca().invert_xaxis()
plt.legend()
plt.show()
