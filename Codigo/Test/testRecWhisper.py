import subprocess
import whisper

modelo = whisper.load_model("small")

duracion = 3  # segundos
archivo_salida = "grabacion.wav"

while True:

    conf = input("Presione una tecla para grabar y transcribir audio")

    subprocess.run(["arecord", "-D", "plughw:2,0", "-f", "S16_LE", "-r", "48000", "-c", "2","-d", str(duracion),archivo_salida])

    subprocess.run(["aplay", "-D", "hw:2,0", archivo_salida])

    resultado = modelo.transcribe(archivo_salida, language = 'es')

    print(f"Texto: {resultado['text']}")