
from pytube import YouTube
from tkinter import *
import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()

janela.title("Ytdown - Donwload Gratuito de Videos do Youtube.")
texto = Label(janela, text="Seja bem Vindo ao Ytdown!")
texto.grid(column=0, row=0, padx=10, pady=10)


def download():
    Youtube_link = link_video.get() 
    youtube = YouTube(Youtube_link)
    youtube.streams.get_highest_resolution().download()
    messagebox.showinfo("Obrigado por usar o Ytdown!", "Download Concluido!")

link_label = Label(janela, text="Digite o link do video que deseja baixar:")
link_label.grid(column=0, row=1, padx=10, pady=10)

link_video = janela.linkText = Entry(janela,width=55,)


janela.linkText.grid( row=2, padx=10, pady=10) 


botao = Button(janela, text="Baixar Video", command=download)
botao.grid(column=0, row=3, padx=10, pady=10)



janela.mainloop()

