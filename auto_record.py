import winsound
import time
import pyautogui

def timer(t: float):
    # Timer de t segundos
    for i in range(int(t)):
        print(f"Tiempo restante: {t - i} segundos")
        time.sleep(1)
        # Sonido de alerta antes de los ultimos 3 segundos cada segundo
        if i >= t - 3:
            winsound.Beep(1000, 1000)
            time.sleep(1)

# Tiempo de espera antes de empezar a grabar
timer(10)

# Toma la posición del mouse
x, y = pyautogui.position()
print(x, y)

# Da click en la posición del mouse
pyautogui.click(x, y)

# Tiempo de espera antes de iniciar las pruebas
timer(10)

# Inicia las pruebas
timer(20)

# Tiempo de descanso entre pruebas
timer(10)

# Inicia las pruebas
timer(20)

# Click en la posición del mouse
pyautogui.click(x, y)
