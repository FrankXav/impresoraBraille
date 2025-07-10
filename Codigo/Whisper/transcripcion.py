import whisper
import multiprocessing
import time

def loop_reconocimiento(entrada, salida):
    print("Se carga modelo!!!!")
    modelo = whisper.load_model("base")  

    while True:
        tarea = entrada.get()  # Espera nueva tarea
        if tarea == "salir":
            print("Cerrando proceso de transcripción.")
            break

        archivo = tarea.get("archivo")
        uid = tarea.get("uid")

        try:
            print("Comenzamos reconocimiento!!!!!")
            resultado = modelo.transcribe(archivo, language='es', initial_prompt='Objetos en la oficina')
            texto = resultado['text']
        except Exception as e:
            texto = f"ERROR: {str(e)}"

        salida.put({"uid": uid, "texto": texto})
