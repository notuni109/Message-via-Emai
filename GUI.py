from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import email_send

class Email:
    def __init__(self, master):

        master.title('Email sending')

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text='E-mail:' ).grid(row=0, column=0, padx=5, sticky='w')
        ttk.Label(self.frame_content, text='Password:').grid(row=0, column=1, padx=5, sticky='w')
        ttk.Label(self.frame_content, text='Recipient:' ).grid(row=2, column=0, padx=5, sticky='w')

        self.entry_email = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))
        self.entry_password = ttk.Entry(self.frame_content, show='*', width=24, font=('Arial', 10))
        self.entry_recipient = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))

        self.entry_email.grid(row=1, column=0, padx=5)
        self.entry_password.grid(row=1, column=1, padx=5)
        self.entry_recipient.grid(row=3, column=0, padx=5)
        
        ttk.Button(self.frame_content, text='Send', command=self.sending).grid(row=4, column=0, padx=20, sticky='e')
        ttk.Button(self.frame_content, text='Clear', command=self.clear).grid(row=4, column=1, padx=20, sticky='w')
    
    def sending(self):
        with open('sender.txt', 'w', encoding='utf-8') as f:
            f.write(str({'email': self.entry_email.get(), 'password': self.entry_password.get()}))
        with open('recipient.txt', 'w', encoding='utf-8') as f1:
            f1.write(f'{self.entry_recipient.get()}')
        email_send.main()
        messagebox.showinfo(title="Notification", message="E-mail sent!")

    def clear(self):
        self.entry_email.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.entry_recipient.delete(0, 'end')

def main():
    root = Tk()
    email = Email(root)
    root.mainloop()

if __name__=="__main__": 
    main()
    