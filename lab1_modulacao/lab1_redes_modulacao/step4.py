from functions import decode_manchester, capturar_do_microfone
from configs import SAMPLE_RATE, BIT_DURATION
import soundfile as sf


duracao = 5 * BIT_DURATION + 1  # margem extra
audio_capturado = capturar_do_microfone(duracao)

sf.write('audios/audio_microfone.wav', audio_capturado, SAMPLE_RATE)

print("\nDecodificando...")
decoded = decode_manchester(audio_capturado, 5)

print(f"Original: 10110") 
print(f"Capturado: {decoded}") #Não consegui executar por falta de equipamento adequado

