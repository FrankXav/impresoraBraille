# transcriptor.py  (lanzar una vez y permanecer vivo)
import multiprocessing as mp
import whisper, signal, os

# ---------- 1. inicializador ----------
def init_model():
    global model
    model = whisper.load_model("base")   # Carga única

# ---------- 2. función de transcripción ----------
def _transcribe(path):
    return model.transcribe(
        path, language='es',
        initial_prompt='Objetos en la oficina'
    )['text']

# ---------- 3. worker principal ----------
def loop_reconocimiento(entrada, salida, timeout=20):
    pool = mp.get_context("spawn").Pool(
        processes=1, initializer=init_model
    )

    while True:
        tarea = entrada.get()
        if tarea == "salir":
            pool.close()
            pool.join()
            break

        uid, archivo = tarea["uid"], tarea["archivo"]
        async_result = pool.apply_async(_transcribe, (archivo,))

        try:
            texto = async_result.get(timeout=timeout)
        except mp.TimeoutError:
            # Cancela futura respuesta y reinicia el pool
            async_result.cancel()
            pool.terminate()      # mata al hijo atascado
            pool.join()
            pool = mp.get_context("spawn").Pool(
                processes=1, initializer=init_model
            )
            texto = "ERROR: tiempo de reconocimiento agotado"

        salida.put({"uid": uid, "texto": texto})
