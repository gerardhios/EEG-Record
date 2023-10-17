
# Grabacion de señales EGG automatizada

Repositorio para almacenar el codigo que permite grabar de forma automatizada las señales EEG


# Instalacion

## Crear entorno virtual
```bash
  python -m  venv env
```

## Activar el entorno virtual
### Windows
```bash
  . .\env\Scripts\activate
```
### Linux
```bash
  source ./env/bin/activate
```

## Instalar EEG-Record con pip

```bash
  pip install -r requirements.txt
```

# Explicacion del funcionamiento

Al ejecutar el script de python el programa sigue la sig. secuencia:

1. Espera 10 segundos para que el usuario ponga el cursor en el boton de inicio de grabacion
2. Graba la posicion del boton y da click para iniciar la grabacion
3. Toma 10 segundos de grabacion antes de empezar con la prueba
4. Toma 20 segundos de grabacion de la primera intención
5. Toma 20 segundoa de grabacion de descanso antes de pasar a la siguiente intención
6. Toma 20 segundos de grabacion de la segunda intención
7. Termina la grabacion

