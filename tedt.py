import tkinter as tk

class JanelaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x100")
        self.btn = tk.Button(self.master, text="Abrir nova janela", command=self.abrir)
        self.btn.pack(pady=10)

    def abrir(self):
        self.master.withdraw()
        self.nova_janela = tk.Toplevel(self.master)
        self.app = JanelaSecundaria(self.nova_janela)

class JanelaSecundaria:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x100")
        self.btn = tk.Button(self.master, text="Fechar", command=self.fechar)
        self.btn.pack(pady=10)

    def fechar(self):
        self.master.destroy()
        root.deiconify()

root = tk.Tk()
app = JanelaPrincipal(root)
root.mainloop()