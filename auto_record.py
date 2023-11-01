import time
import pyautogui

def timer(t: float):
    # Timer de t segundos
    for i in range(int(t)):
        print(f"Tiempo restante: {t - i} segundos")
        time.sleep(1)

# Tiempo de espera antes de empezar a grabar
print("Acomoda el mouse en la posición deseada")
timer(10)

# Toma la posición del mouse
x, y = pyautogui.position()
print(f"Posicion grabada {x}, {y}")

# Da click en la posición del mouse
pyautogui.click(x, y)

# Tiempo de espera antes de iniciar las pruebas
print("Inicia las pruebas en 10 segundos")
timer(10)

# Inicia las pruebas
print("Inicia las pruebas")
timer(20)

# Tiempo de descanso entre pruebas
print("Descansa 20 segundos")
timer(20)

# Inicia las pruebas
print("Inicia las pruebas")
timer(20)

# Tiempo de espera antes de empezar a grabar
print("Acomoda el mouse en la posición deseada para detener la grabacion")
timer(10)

# Toma la posición del mouse
x, y = pyautogui.position()
print(f"Posicion grabada {x}, {y}")

# Click en la posición del mouse
print("Fin de la grabación")
pyautogui.click(x, y)
