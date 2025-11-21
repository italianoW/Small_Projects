from functions import encode_nrz, encode_manchester, decode_nrz, decode_manchester
from configs import SAMPLE_RATE
import soundfile as sf
from functions import plot_signal
import sounddevice as sd

# Dados de teste
test_data = "1010100000001111110000010101010111000"

print(f"Criando arquivos de teste para: {test_data}")

# NRZ
nrz_signal = encode_nrz(test_data)
sf.write('audios/teste_nrz.wav', nrz_signal, SAMPLE_RATE)
print("\t ✓ Arquivo teste_nrz.wav criado")

# Manchester
manchester_signal = encode_manchester(test_data)
sf.write('audios/teste_manchester.wav', manchester_signal, SAMPLE_RATE)
print("\t ✓ Arquivo teste_manchester.wav criado")

original_data = '0011000101001001111'



print(f"\nDados originais: {original_data}")
print(f"Número de bits: {len(original_data)}\n")

# Testa decodificação NRZ
print("1. Decodificando NRZ:")
nrz_audio, _ = sf.read('audios/dados_123111398_44100hz.wav')
decoded_nrz = decode_nrz(nrz_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_nrz}")
print(f"Correto: {original_data == decoded_nrz}\n")

# Testa decodificação Manchester
print("3. Decodificando Manchester:")
manchester_audio, _ = sf.read('audios/dados_123111398_44100hz.wav')
decoded_manchester = decode_manchester(manchester_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_manchester}")
print(f"Correto: {original_data == decoded_manchester}")

sd.play(nrz_audio, SAMPLE_RATE)

plot_signal(nrz_audio,'Modulação Análoga',len(original_data))
## Não é nem manchester, nem NRZ, ambos dão um resultado, mas a plotagem demonstra que não há a possibilidade de ser algum deles.
## Sendo os resultados a(XOR)(("1")*N) = b. (a = manchester_decoded, b = nrz_decoded, n = tamanho)