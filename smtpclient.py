import smtplib
from tkinter import *
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email():
    sender = sender_entry.get()
    password = password_entry.get()
    receiver = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", END)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)

        msg = MIMEMultipart("mixed")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        text_part = MIMEText(message, "plain")
        msg.attach(text_part)

        image_file = "imagen.png"
        with open(image_file, "rb") as f:
            image_part = MIMEImage(f.read(), name="image.jpg")
            msg.attach(image_part)

        server.sendmail(sender, receiver, msg.as_string())

        server.quit()

        messagebox.showinfo("Éxito", "Correo electrónico enviado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar el correo electrónico: {str(e)}")

window = Tk()
window.title("Cliente SMTP")
window.geometry("400x660")

sender_label = Label(window, text="Remitente:")
sender_label.pack()
sender_entry = Entry(window)
sender_entry.pack()

password_label = Label(window, text="Contraseña:")
password_label.pack()
password_entry = Entry(window, show="*")
password_entry.pack()

receiver_label = Label(window, text="Destinatario:")
receiver_label.pack()
receiver_entry = Entry(window)
receiver_entry.pack()

subject_label = Label(window, text="Asunto:")
subject_label.pack()
subject_entry = Entry(window)
subject_entry.pack()

message_label = Label(window, text="Mensaje:")
message_label.pack()
message_text = Text(window)
message_text.pack()

send_button = Button(window, text="Enviar", command=send_email)
send_button.pack()

window.mainloop()
