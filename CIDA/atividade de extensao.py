## importando a biblioteca ##
from tkinter import *
import tkinter as tk
import serial
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import struct

## Variaveis ##
layout = Tk()
pasta = os.path.dirname(__file__)


## classe ##
class sistema():
    ## MAIN ##
    def __init__(self):
        self.janela = layout
        self.estrutura_menu()
        self.dados_menu()
        layout.mainloop()

    # Menu #
    def estrutura_menu(self):
        self.janela.title("Sistema")
        self.janela.geometry('350x300')
        self.janela.resizable(False, False)
        self.janela.iconbitmap("raio.ico")
        self.janela.configure()

    def dados_menu(self):
        # Titulo_do_menu #
        self.texto0 = Label(self.janela, text='', font=('Verdana', '5', 'bold'))
        self.texto0.pack()
        self.texto1 = Label(self.janela, text='Identificação e Controle', font=('Verdana', '12', 'bold'))
        self.texto1.pack()
        self.texto4 = Label(self.janela, text='', font=('Verdana', '5', 'bold'))
        self.texto4.pack()

        # Botao_do_menu #
        self.botao1 = Button(text='Identificação e Modelagem de Sistemas', font=("verdana", 10, "bold",),
                             command=self.identificacao)
        self.botao1.place(relx=0.06, rely=0.26)
        # self.botao2 = Button(text='Experimento com Malha Fechada', font=("verdana", 10, "bold",), command=self.experimento)
        # self.botao2.place(relx=0.12, rely=0.40)
        self.botao3 = Button(text='About', font=("verdana", 10, "bold",), command=self.about)
        self.botao3.place(relx=0.41, rely=0.55)
        self.botao4 = Button(text='Exit', font=("verdana", 10, "bold",), command=self.janela.destroy)
        self.botao4.place(relx=0.43, rely=0.70)

    # About #
    def about(self):
        # Estrutura_do_about #
        self.about = Toplevel()
        self.about.title("About")
        self.about.geometry('250x200')
        self.about.resizable(False, False)
        self.about.iconbitmap("raio.ico")
        self.about.configure()
        self.about.focus_force()
        self.about.grab_set()

        # Bot?o_do_about #
        self.botao_about = Button(self.about, text='Exit', font=("verdana", 10, "bold",), command=self.about.destroy)
        self.botao_about.place(relx=0.40, rely=0.70)

        # Texto_do_about#
        self.texto_about = Label(self.about, text='Interface e Controle 1.0 (64 e 32 bit)')
        self.texto_about.place(relx=0.05, rely=0.01)
        self.texto_about1 = Label(self.about, text='Publicado por Yuri Henrique Rezende')
        self.texto_about1.place(relx=0.05, rely=0.11)
        self.texto_about2 = Label(self.about, text='Professor Orientador: Hugo Sakai Idagawa')
        self.texto_about2.place(relx=0.05, rely=0.21)
        self.texto_about3 = Label(self.about, text='Apoio: Faculdade Senai "Roberto Mange" ')
        self.texto_about3.place(relx=0.05, rely=0.31)

    # Malha Fechada #
    ''''
   # Experimento_Com_Malha_Fechada #
    def experimento(self):
        # estrutura #
        self.janela_ex = Toplevel()
        self.janela_ex.title("Experimento Com Malha Fechada")
        self.janela_ex.geometry('650x700')
        self.janela_ex.resizable(False, False)
        self.janela_ex.configure()
        self.janela_ex.focus_force()
        self.janela_ex.grab_set()


        # Limpar Entradas #
        self.validacao_numeros = self.janela_ex.register(self.validar_numeros)

        # Colunas e Espa?amentos #
        self.colunas1 = Label(self.janela_ex, background='gray')
        self.colunas1.place(relx=0, rely=0.35, relwidth=1, relheight=0.005)

        self.colunas2 = Label(self.janela_ex, background='gray')
        self.colunas2.place(relx=0.5, rely=0.1, relwidth=0.01, relheight=0.25)

        self.colunas3 = Label(self.janela_ex, background='gray')
        self.colunas3.place(relx=0, rely=0.10, relwidth=1, relheight=0.005)

        self.texto4 = Label(self.janela_ex, text='', font=('Verdana', '5', 'bold'))
        self.texto4.pack()

        self.colunas5 = Label(self.janela_ex, background='gray')
        self.colunas5.place(relx=0, rely=0.60, relwidth=1, relheight=0.005)

        self.colunas5 = Label(self.janela_ex, background='gray')
        self.colunas5.place(relx=0, rely=0.75, relwidth=1, relheight=0.005)

        # Textos e Titulos #
        self.texto5 = Label(self.janela_ex, text='Experimento Com Malha Fechada', font=('Verdana', '13', 'bold'))
        self.texto5.pack()

        self.texto6 = Label(self.janela_ex, text='Passo 1: Conex?o', font=('Verdana', '9', 'bold'))
        self.texto6.place(relx=0.08, rely=0.09)

        self.texto7 = Label(self.janela_ex, text='SISTEMA OPERACIONAL', font=('Verdana', '8', 'bold'))
        self.texto7.place(relx=0.15, rely=0.12)

        self.texto8 = Label(self.janela_ex, text='CONFIGURA??O DO ARDUINO', font=('Verdana', '8', 'bold'))
        self.texto8.place(relx=0.62, rely=0.12)

        self.texto9 = Label(self.janela_ex, text='DIGITE A ENTRADA DO ARDUINO:', font=('Verdana', '7'))
        self.texto9.place(relx=0.51, rely=0.17)

        self.texto10 = Label(self.janela_ex, text='DIGITE A VELOCIDADE DE COMUNICA??O:', font=('Verdana', '7'))
        self.texto10.place(relx=0.51, rely=0.20)

        self.texto11 = Label(self.janela_ex, text='Passo 2: Ajuste dos ganhos do controlador', font=('Verdana', '9', 'bold'))
        self.texto11.place(relx=0.06, rely=0.37)

        self.texto12 = Label(self.janela_ex, text='Ganhos do Controlador:', font=('Arial', '10'))
        self.texto12.place(relx=0.06, rely=0.40)

        self.texto13 = Label(self.janela_ex, text='Kp:', font=('Arial', '12'))
        self.texto13.place(relx=0.06, rely=0.45)

        self.texto14 = Label(self.janela_ex, text='Ki:', font=('Arial', '12'))
        self.texto14.place(relx=0.06, rely=0.49)

        self.texto15 = Label(self.janela_ex, text='Kd:', font=('Arial', '12'))
        self.texto15.place(relx=0.06, rely=0.53)

        self.texto16 = Label(self.janela_ex, text='Passo 3: Entrada de referencia (Vin)', font=('Verdana', '9', 'bold'))
        self.texto16.place(relx=0.06, rely=0.62)

        self.degrau_simples = Label(self.janela_ex, text='Dura??o do Degrau (em s.): ', font=('Arial', '9'))
        self.degrau_simples.place(relx=0.06, rely=0.66)

        self.degrau_simples1 = Label(self.janela_ex, text='Tens?o 1 (0V a 3.0V): ', font=('Arial', '9'))
        self.degrau_simples1.place(relx=0.06, rely=0.70)

        # Entradas e Bot?es #
        self.caixa1 = IntVar()
        self.caixa1 = Entry(self.janela_ex)
        self.caixa1.place(relx=0.81, rely=0.17, relwidth=0.06, relheight=0.03)

        self.caixa2 = IntVar()
        self.caixa2 = Entry(self.janela_ex, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa2.place(relx=0.89, rely=0.20, relwidth=0.06, relheight=0.03)

        self.botao1 = Button(self.janela_ex,text='conectar', font=("verdana", 10, "bold",), command=self.conectar1)
        self.botao1.place(relx=0.60, rely=0.26, relwidth=0.12, relheight=0.05)

        self.botao2 = Button(self.janela_ex,text='desconectar', font=("verdana", 10, "bold"), command=self.desconectar1)
        self.botao2.place(relx=0.75, rely=0.26, relwidth=0.16, relheight=0.05)

        self.botao3 = Button(self.janela_ex,text='fechar programa', font=("verdana", 10, "bold"), command=self.janela_ex.destroy)
        self.botao3.place(relx=0.13, rely=0.25, relwidth=0.25, relheight=0.05)

        self.sistem = IntVar()
        self.botaoE = Radiobutton(self.janela_ex,text="Windows", variable=self.sistem, value=1).place(x=60, y=140)
        self.botaoE = Radiobutton(self.janela_ex,text="Linux", variable=self.sistem, value=2).place(x=180, y=140)

        self.botao4 = Button(self.janela_ex,text='Realizar Aquisi??o', font=("verdana", 10, "bold"),command=self.experimento_malha_fechada)
        self.botao4.place(relx=0.37, rely=0.85, relwidth=0.25, relheight=0.05)

        self.caixa3 = IntVar()
        self.caixa3 = Entry(self.janela_ex, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa3.place(relx=0.11, rely=0.45, relwidth=0.06, relheight=0.04)

        self.caixa4 = IntVar()
        self.caixa4 = Entry(self.janela_ex, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa4.place(relx=0.11, rely=0.49, relwidth=0.06, relheight=0.04)

        self.caixa5 = IntVar()
        self.caixa5 = Entry(self.janela_ex, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa5.place(relx=0.11, rely=0.53, relwidth=0.06, relheight=0.04)

        self.caixa6 = IntVar()
        self.caixa6 = Entry(self.janela_ex, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa6.place(relx=0.31, rely=0.66, relwidth=0.05, relheight=0.04)

        self.caixa7 = IntVar()
        self.caixa7 = Entry(self.janela_ex, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa7.place(relx=0.25, rely=0.69, relwidth=0.05, relheight=0.04)
    def conectar1(self):
        serialPort = self.caixa1.get()
        velocidade = self.caixa2.get()
        sistema = self.sistem.get()
        try:
            if sistema == 2:
                try:
                    self.serial_objeto = serial.Serial('/dev/tty' + str(serialPort), velocidade)
                    self.texto8 = Label(self.janela_ex, text='CONECTADO                 ', font=('Verdana', '7'),
                                        foreground="green")
                    self.texto8.place(relx=0.64, rely=0.32)
                except:
                    self.texto9 = Label(self.janela_ex, text='FALHA                     ', font=('Verdana', '7'),
                                        foreground="red")
                    self.texto9.place(relx=0.64, rely=0.32)
            elif sistema == 1:
                self.serial_objeto = serial.Serial('COM' + str(serialPort), velocidade)
                self.texto8 = Label(self.janela_ex, text='CONECTADO                     ', font=('Verdana', '7'),
                                    foreground="green")
                self.texto8.place(relx=0.64, rely=0.32)
        except:
            self.texto9 = Label(self.janela_ex, text='FALHA                         ', font=('Verdana', '7'),
                                foreground="red")
            self.texto9.place(relx=0.64, rely=0.32)
    def desconectar1(self):
        try:
            self.serial_objeto.close()
            self.texto9 = Label(self.janela_ex, text='DESCONECTADO                      ', font=('Verdana', '7'),
                                foreground="red")
            self.texto9.place(relx=0.64, rely=0.32)
        except:
            self.texto9 = Label(self.janela_ex, text='DESCONECTADO                      ', font=('Verdana', '7'),
                                foreground="red")
            self.texto9.place(relx=0.64, rely=0.32)
    def experimento_malha_fechada(self):
        # passo 2 entradas:
        try:
            kp = float(self.caixa3.get())
            ki = float(self.caixa4.get())
            kd = float(self.caixa5.get())
            degrau = float(self.caixa6.get())
            tensao = float(self.caixa7.get())
        except:
            pass
    '''''

    # Identifica??o_e_Modelagem_de_Sistemas #
    def identificacao(self):
        # Estrutura #
        self.janela_id = Toplevel()
        self.janela_id.title("Identificação e Modelagem de Sistemas")
        self.janela_id.geometry('650x800')
        self.janela_id.resizable(False, False)
        self.janela_id.iconbitmap("raio.ico")
        self.janela_id.configure()
        self.janela_id.focus_force()
        self.janela_id.grab_set()

        # Limpar Entradas #
        self.validacao_numeros = self.janela_id.register(self.validar_numeros)

        # Colunas e Espa?amentos #
        self.colunas1 = Label(self.janela_id, background='gray')
        self.colunas1.place(relx=0, rely=0.35, relwidth=1, relheight=0.005)

        self.colunas2 = Label(self.janela_id, background='gray')
        self.colunas2.place(relx=0.5, rely=0.1, relwidth=0.01, relheight=0.70)

        self.colunas3 = Label(self.janela_id, background='gray')
        self.colunas3.place(relx=0, rely=0.10, relwidth=1, relheight=0.005)

        self.colunas4 = Label(self.janela_id, background='gray')
        self.colunas4.place(relx=0, rely=0.80, relwidth=1, relheight=0.005)

        self.texto4 = Label(self.janela_id, text='', font=('Verdana', '5', 'bold'))
        self.texto4.pack()

        # Textos e Titulos #
        self.texto5 = Label(self.janela_id, text='Identificação e Modelagem de Sistemas',
                            font=('Verdana', '13', 'bold'))
        self.texto5.pack()

        self.texto6 = Label(self.janela_id, text='Passo 1: Conexão', font=('Verdana', '9', 'bold'))
        self.texto6.place(relx=0.08, rely=0.09)

        self.texto7 = Label(self.janela_id, text='SISTEMA OPERACIONAL', font=('Verdana', '8', 'bold'))
        self.texto7.place(relx=0.15, rely=0.12)

        self.texto8 = Label(self.janela_id, text='CONFIGURAÇÃO DO ARDUINO', font=('Verdana', '8', 'bold'))
        self.texto8.place(relx=0.62, rely=0.12)

        self.texto9 = Label(self.janela_id, text='DIGITE A ENTRADA DO ARDUINO:', font=('Verdana', '7'))
        self.texto9.place(relx=0.51, rely=0.17)

        # self.texto10 = Label(self.janela_id, text='DIGITE A VELOCIDADE DE COMUNICA??O:', font=('Verdana', '7'))
        # self.texto10.place(relx=0.51, rely=0.20)

        self.texto11 = Label(self.janela_id, text='Passo 2: Ajuste do modelo da planta', font=('Verdana', '9', 'bold'))
        self.texto11.place(relx=0.05, rely=0.37)

        # Formula.png #
        self.imagem = PhotoImage(file=pasta + "\\calc.png")
        self.l_lago = Label(self.janela_id, image=self.imagem)
        self.l_lago.place(relx=0.01, rely=0.43, relwidth=0.45, relheight=0.10)

        self.texto12 = Label(self.janela_id, text='Coeficientes do Modelo:')
        self.texto12.place(relx=0.07, rely=0.53)

        self.texto13 = Label(self.janela_id, text='Função de tranferencia da planta:', font=('Arial', '9'))
        self.texto13.place(relx=0.07, rely=0.40)

        self.texto14 = Label(self.janela_id, text='G1', font=('Arial', '10'))
        self.texto14.place(relx=0.10, rely=0.56)

        self.texto15 = Label(self.janela_id, text='G2', font=('Arial', '10'))
        self.texto15.place(relx=0.10, rely=0.59)

        self.texto17 = Label(self.janela_id, text='A=', font=('Arial', '10'))
        self.texto17.place(relx=0.10, rely=0.62)

        self.texto18 = Label(self.janela_id, text='B=', font=('Arial', '10'))
        self.texto18.place(relx=0.10, rely=0.65)

        self.texto19 = Label(self.janela_id, text='C=', font=('Arial', '10'))
        self.texto19.place(relx=0.10, rely=0.68)

        self.texto21 = Label(self.janela_id, text='Passo 3: Entrada de Referencia(Vin)', font=('Verdana', '9', 'bold'))
        self.texto21.place(relx=0.56, rely=0.37)

        self.texto13 = Label(self.janela_id, text='Sinal de entrada: ', font=('Arial', '9'))
        self.texto13.place(relx=0.58, rely=0.40)

        # Entradas e Bot?es #
        self.caixa1 = IntVar()
        self.caixa1 = Entry(self.janela_id)
        self.caixa1.place(relx=0.81, rely=0.17, relwidth=0.06, relheight=0.03)

        # self.caixa2 = IntVar()
        # self.caixa2 = Entry(self.janela_id, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        # self.caixa2.place(relx=0.89, rely=0.20, relwidth=0.06, relheight=0.03)

        self.caixa3 = IntVar()
        self.caixa3 = Entry(self.janela_id, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa3.place(relx=0.15, rely=0.56, relwidth=0.20, relheight=0.03)

        self.caixa4 = IntVar()
        self.caixa4 = Entry(self.janela_id, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa4.place(relx=0.15, rely=0.59, relwidth=0.20, relheight=0.03)

        self.caixa5 = IntVar()
        self.caixa5 = Entry(self.janela_id, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa5.place(relx=0.15, rely=0.62, relwidth=0.20, relheight=0.03)

        self.caixa6 = IntVar()
        self.caixa6 = Entry(self.janela_id, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa6.place(relx=0.15, rely=0.65, relwidth=0.20, relheight=0.03)

        self.caixa7 = IntVar()
        self.caixa7 = Entry(self.janela_id, validate='key', validatecommand=(self.validacao_numeros, '%S'))
        self.caixa7.place(relx=0.15, rely=0.68, relwidth=0.20, relheight=0.03)

        self.botao1 = Button(self.janela_id, text='conectar', font=("verdana", 10, "bold",), command=self.conectar)
        self.botao1.place(relx=0.60, rely=0.26, relwidth=0.12, relheight=0.05)

        self.botao2 = Button(self.janela_id, text='desconectar', font=("verdana", 10, "bold"), command=self.desconectar)
        self.botao2.place(relx=0.75, rely=0.26, relwidth=0.16, relheight=0.05)

        self.botao3 = Button(self.janela_id, text='fechar programa', font=("verdana", 10, "bold"), command=self.fechar)
        self.botao3.place(relx=0.13, rely=0.25, relwidth=0.25, relheight=0.05)

        self.sistem = IntVar()
        self.botaoE = Radiobutton(self.janela_id, text="Windows", variable=self.sistem, value=1).place(x=60, y=140)
        self.botaoE = Radiobutton(self.janela_id, text="Linux", variable=self.sistem, value=2).place(x=180, y=140)

        self.botaoD = Button(self.janela_id, text="Degrau Simples", font=("verdana", 10, "bold"),
                             command=lambda: degrau_simples(self))
        self.botaoD.place(x=350, y=350)
        self.botaoD = Button(self.janela_id, text="Degrau Duplo", font=("verdana", 10, "bold"),
                             command=lambda: degrau_duplo(self))
        self.botaoD.place(x=500, y=350)

        self.botao5 = Button(self.janela_id, text='Plotar P(s)', font=("verdana", 10, "bold"),
                             command=self.plotar_tranferencia_planta)
        self.botao5.place(relx=0.09, rely=0.86, relwidth=0.25, relheight=0.05)

        self.botao7 = Button(self.janela_id, text='Comparar Curvas', font=("verdana", 10, "bold"),
                             command=self.comparar_curvas)
        self.botao7.place(relx=0.67, rely=0.86, relwidth=0.25, relheight=0.05)

    def fechar(self):
        try:
            self.janela_id.destroy()
            self.serial_objeto.close()
            self.janela_id.destroy
        except:
            pass

    def plotar_tranferencia_planta(self):
        global time
        global voltagem
        # Entrada de dados e conversao #
        try:
            G1 = float(self.caixa3.get())
            G2 = float(self.caixa4.get())
            A = float(self.caixa5.get())
            B = float(self.caixa6.get())
            C = float(self.caixa7.get())
        except:
            pass

        # preparando para plotar o grafico 3
        try:
            num = (G1, G2)
            den = (A, B, C)
            sys = signal.TransferFunction(num, den)
            time, voltagem = signal.step(sys)

            # plotar
            plt.plot(time, voltagem, label="Simulation")
            plt.show()
        except:
            pass

    def conectar(self):
        serialPort = self.caixa1.get()
        velocidade = 115200
        sistema = self.sistem.get()
        try:
            if sistema == 2:
                try:
                    self.serial_objeto = serial.Serial('/dev/tty' + str(serialPort), velocidade, timeout=2)
                    self.texto8 = Label(self.janela_id, text='CONECTADO                 ', font=('Verdana', '7'),
                                        foreground="green")
                    self.texto8.place(relx=0.64, rely=0.32)
                except:
                    self.texto9 = Label(self.janela_id, text='FALHA                     ', font=('Verdana', '7'),
                                        foreground="red")
                    self.texto9.place(relx=0.64, rely=0.32)
                    self.desativado()
            elif sistema == 1:
                self.serial_objeto = serial.Serial('COM' + str(serialPort), velocidade, timeout=2)
                self.texto8 = Label(self.janela_id, text='CONECTADO                     ', font=('Verdana', '7'),
                                    foreground="green")
                self.texto8.place(relx=0.64, rely=0.32)
                try:
                    self.realizar()
                except:
                    self.desativado()
        except:
            self.desativado()
            self.texto9 = Label(self.janela_id, text='FALHA                         ', font=('Verdana', '7'),
                                foreground="red")
            self.texto9.place(relx=0.64, rely=0.32)

    def desconectar(self):
        try:
            self.serial_objeto.close()
            self.texto9 = Label(self.janela_id, text='DESCONECTADO                      ', font=('Verdana', '7'),
                                foreground="red")
            self.texto9.place(relx=0.64, rely=0.32)
            self.desativado()
        except:
            self.texto9 = Label(self.janela_id, text='DESCONECTADO                      ', font=('Verdana', '7'),
                                foreground="red")
            self.texto9.place(relx=0.64, rely=0.32)
            self.desativado()

    def plotar_vin_simples(self):
        try:
            self.valor_degrau = self.caixa_degrau_simples.get()
            valor_degrau = float(self.valor_degrau)

            self.valor_s = self.caixa_degrau_simples1.get()
            valor_tensao = float(self.valor_s)
        except:
            pass
        # preparando para plotar o grafico
        try:
            x = np.linspace(0, valor_degrau, 1000)
            y = np.linspace(valor_tensao, valor_tensao, 1000)

            # plotar o grafico
            plt.plot(x, y)
            plt.show()
        except:
            pass

    def plotar_vin_duplo(self):
        # Entrada de valores e conversao
        try:
            self.valor = self.caixa_degrau_duplo1.get()
            valor_degrau = float(self.valor)

            self.valor_1 = self.caixa_degrau_duplo2.get()
            tensao_1 = float(self.valor_1)

            self.valor_2 = self.caixa_degrau_duplo3.get()
            tensao2 = float(self.valor_2)
        except:
            pass

        # Preparando para plotar o grafico
        try:
            x = [0, valor_degrau, valor_degrau, 2 * valor_degrau]
            y = [tensao_1, tensao_1, tensao2, tensao2]

            # Plotar o grafico
            plt.plot(x, y)
            plt.show()
        except:
            pass

    def simples(self):
        global tempo_certo
        global tensoes
        try:
            self.serial_objeto.write(str.encode('1\\n'))
            self.serial_objeto.write(str.encode(self.caixa_degrau_simples1.get() + '\\n'))
            self.serial_objeto.write(str.encode('0.00\\n'))  # degrau simples
            self.serial_objeto.write(str.encode(self.caixa_degrau_simples.get() + '\\n'))

            self.serial_objeto.write(str.encode('2\\n'))  # dizer se e degrau simples ou duplo 2 ou 3

            valor = int.from_bytes(self.serial_objeto.read(2), "little", signed=True)
            tempo = []
            tensoes = [0.0]

            while (valor != -1):
                tempo.append(valor)
                data = struct.unpack("f", self.serial_objeto.read(4))
                tensoes.append(data[0])
                valor = int.from_bytes(self.serial_objeto.read(2), "little", signed=True)

            contador = range(len(tempo))
            tempo_certo = [0.0]

            for i in contador:
                novo = tempo_certo[i] + tempo[i]
                tempo_certo.append(novo)

            plt.plot(tempo_certo, tensoes)
            plt.show()
        except:
            self.serial_objeto.close()
            self.serial_objeto.open()

    def duplo(self):
        global tempo_certo
        global tensoes
        try:
            self.serial_objeto.write(str.encode('1\\n'))
            self.serial_objeto.write(str.encode(self.caixa_degrau_duplo2.get() + '\\n'))
            self.serial_objeto.write(str.encode(self.caixa_degrau_duplo3.get() + '\\n'))  # degrau simples
            self.serial_objeto.write(str.encode(self.caixa_degrau_duplo1.get() + '\\n'))

            self.serial_objeto.write(str.encode('3\\n'))  # dizer se e degrau simples ou duplo 2 ou 3

            valor = int.from_bytes(self.serial_objeto.read(2), "little", signed=True)
            tempo = []
            tensoes = [0.0]

            while (valor != -1):
                tempo.append(valor)
                data = struct.unpack("f", self.serial_objeto.read(4))
                tensoes.append(data[0])
                valor = int.from_bytes(self.serial_objeto.read(2), "little", signed=True)

            contador = range(len(tempo))
            tempo_certo = [0.0]

            for i in contador:
                novo = tempo_certo[i] + tempo[i]
                tempo_certo.append(novo)

            plt.plot(tempo_certo, tensoes)
            plt.show()
        except:
            self.serial_objeto.close()
            self.serial_objeto.open()

    def comparar_curvas(self):
        try:
            # plot 1:
            plt.subplot(1, 2, 1)
            plt.plot(time, voltagem, color='blue')
            plt.legend(['Teorico'], fontsize=14)
            plt.xlabel('Tempo(s)', fontsize=15)
            plt.ylabel('Tensao(v)', fontsize=15)

            # plot 2:
            plt.subplot(1, 2, 2)
            plt.plot(tempo_certo, tensoes, color='red')
            plt.legend(['Pratico'], fontsize=14)
            plt.xlabel('Tempo(s)', fontsize=15)
            plt.ylabel('Tensao(v)', fontsize=15)

            plt.suptitle("Comparar Curvas")
            plt.show()
        except:
            pass

    # Botao e entradas do passo 3 #
    def realizar(self):
        try:
            self.botao6.config(state=NORMAL)
            return
        except:
            pass

    def desativado(self):
        try:
            self.botao6.config(state=DISABLED)
            return
        except:
            pass

    # Valida??o_numeros e Coree??o #
    def validar_numeros(self, e):
        if e.isdigit() or e == ".":
            return True
        elif e == "":
            return True
        else:
            return False

    def valor_corrigido_simples(self, *args):
        # CORRE??O DEGRAU SIMPLES E TENSAO #
        try:
            entrada = float(self.caixa_degrau_simples.get())
            if entrada > 5:
                self.valor_corrigido = 5
                self.caixa_degrau_simples.delete(0, tk.END)
                self.caixa_degrau_simples.insert(0, "{:.3f}".format(self.valor_corrigido))
            elif entrada < 0:
                self.caixa_degrau_simples.delete(0, tk.END)
        except ValueError:
            self.caixa_degrau_simples.delete(0, tk.END)

        try:
            entrada = float(self.caixa_degrau_simples1.get())
            if entrada > 3:
                self.valor_corrigido = 3
                self.caixa_degrau_simples1.delete(0, tk.END)
                self.caixa_degrau_simples1.insert(0, "{:.3f}".format(self.valor_corrigido))
            elif entrada < 0:
                self.caixa_degrau_simples1.delete(0, tk.END)
        except ValueError:
            self.caixa_degrau_simples1.delete(0, tk.END)

    def valor_corrigido_duplo(self, *args):
        try:
            entrada = float(self.caixa_degrau_duplo1.get())
            if entrada > 5:
                self.valor_corrigido = 5
                self.caixa_degrau_duplo1.delete(0, tk.END)
                self.caixa_degrau_duplo1.insert(0, "{:.3f}".format(self.valor_corrigido))
            elif entrada < 0:
                self.caixa_degrau_duplo1.delete(0, tk.END)
        except ValueError:
            self.caixa_degrau_duplo1.delete(0, tk.END)

        try:
            entrada = float(self.caixa_degrau_duplo2.get())
            if entrada > 3:
                self.valor_corrigido = 3
                self.caixa_degrau_duplo2.delete(0, tk.END)
                self.caixa_degrau_duplo2.insert(0, "{:.3f}".format(self.valor_corrigido))
            elif entrada < 0:
                self.caixa_degrau_duplo2.delete(0, tk.END)
        except ValueError:
            self.caixa_degrau_duplo2.delete(0, tk.END)

        try:
            entrada = float(self.caixa_degrau_duplo3.get())
            if entrada > 3:
                self.valor_corrigido = 3
                self.caixa_degrau_duplo3.delete(0, tk.END)
                self.caixa_degrau_duplo3.insert(0, "{:.3f}".format(self.valor_corrigido))
            elif entrada < 0:
                self.caixa_degrau_duplo3.delete(0, tk.END)
        except ValueError:
            self.caixa_degrau_duplo3.delete(0, tk.END)


def degrau_simples(self):
    self.degrau_simples = Label(self.janela_id, text='Duração do Degrau (em s.): ', font=('Arial', '9'))
    self.degrau_simples.place(x=340, y=400)

    self.degrau_simples1 = Label(self.janela_id, text='Tensão 1 (0V a 3.0V): ', font=('Arial', '9'))
    self.degrau_simples1.place(x=340, y=430)

    self.caixa_degrau_simples = Entry(self.janela_id, validate='key',
                                      validatecommand=(self.validacao_numeros, '%S'))
    self.caixa_degrau_simples.place(relx=0.77, rely=0.50, relwidth=0.10, relheight=0.03)
    self.caixa_degrau_simples.bind("<KeyRelease>", self.valor_corrigido_simples)

    self.caixa_degrau_simples1 = Entry(self.janela_id, validate='key',
                                       validatecommand=(self.validacao_numeros, '%S'))
    self.caixa_degrau_simples1.place(relx=0.72, rely=0.54, relwidth=0.10, relheight=0.03)
    self.caixa_degrau_simples1.bind("<KeyRelease>", self.valor_corrigido_simples)

    self.bloco = Label(self.janela_id)
    self.bloco.place(relx=0.72, rely=0.57, relwidth=0.10, relheight=0.10)

    self.bloco = Label(self.janela_id)
    self.bloco.place(relx=0.52, rely=0.57, relwidth=0.20, relheight=0.10)

    self.botaoD = Button(self.janela_id, text='Plotar Vin', font=("verdana", 10, "bold"),
                         command=self.plotar_vin_simples)
    self.botaoD.place(relx=0.65, rely=0.64, relwidth=0.15, relheight=0.05)

    self.botao6 = Button(self.janela_id, text='Realizar Aquisição', font=("verdana", 10, "bold"), command=self.simples,
                         state=DISABLED)
    self.botao6.place(relx=0.38, rely=0.86, relwidth=0.25, relheight=0.05)

    try:
        self.serial_objeto.flush()
        self.realizar()
    except:
        self.desativado()


def degrau_duplo(self):
    self.degrau_duplo = Label(self.janela_id, text='Duração do Degrau (em s.): ', font=('Arial', '9'))
    self.degrau_duplo.place(x=340, y=400)

    self.degrau_duplo = Label(self.janela_id, text='Tensão 1 (0V a 3.0V): ', font=('Arial', '9'))
    self.degrau_duplo.place(x=340, y=430)

    self.degrau_duplo = Label(self.janela_id, text='Tensão 2 (0V a 3.0V): ', font=('Arial', '9'))
    self.degrau_duplo.place(x=340, y=456)

    self.caixa_degrau_duplo1 = Entry(self.janela_id, validate='key', validatecommand=(self.validacao_numeros, '%S'))
    self.caixa_degrau_duplo1.place(relx=0.77, rely=0.50, relwidth=0.10, relheight=0.03)
    self.caixa_degrau_duplo1.bind("<KeyRelease>", self.valor_corrigido_duplo)

    self.caixa_degrau_duplo2 = Entry(self.janela_id, validate='key', validatecommand=(self.validacao_numeros, '%S'))
    self.caixa_degrau_duplo2.place(relx=0.72, rely=0.54, relwidth=0.10, relheight=0.03)
    self.caixa_degrau_duplo2.bind("<KeyRelease>", self.valor_corrigido_duplo)

    self.caixa_degrau_duplo3 = Entry(self.janela_id, validate='key', validatecommand=(self.validacao_numeros, '%S'))
    self.caixa_degrau_duplo3.place(relx=0.72, rely=0.57, relwidth=0.10, relheight=0.03)
    self.caixa_degrau_duplo3.bind("<KeyRelease>", self.valor_corrigido_duplo)

    self.botaoDD = Button(self.janela_id, text='Plotar Vin', font=("verdana", 10, "bold"),
                          command=self.plotar_vin_duplo)
    self.botaoDD.place(relx=0.65, rely=0.64, relwidth=0.15, relheight=0.05)

    self.botao6 = Button(self.janela_id, text='Realizar Aquisição', font=("verdana", 10, "bold"), command=self.duplo,
                         state=DISABLED)
    self.botao6.place(relx=0.38, rely=0.86, relwidth=0.25, relheight=0.05)
    try:
        self.serial_objeto.flush()
        self.realizar()
    except:
        self.desativado()


sistema()
