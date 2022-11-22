import random 
import PySimpleGUI as sg

class Dado:
  def __init__(self):
    self.valor_minimo = 1
    self.valor_maximo = 6
    self.layout = [
      [sg.Text('Jogar o dado?')],
      [sg.Button('Sim'), sg.Button('Não')]
    ]

  def Iniciar(self):
    self.janela = sg.Window('Dado', layout=self.layout)
    self.eventos, self.valores = self.janela.Read()

    try:
      if self.eventos == 'Sim':
        self.GerarValor()
      elif self.eventos == 'Não':
        print('Agradecemos a sua participção!')

    except:
      print('Ocorreu um erro com a resposta!')
  
  def GerarValor(self):
    numeroAleatorio = random.randint(self.valor_minimo, self.valor_maximo)
    self.janela.close()
    self.janela = sg.Window('Dado', layout=[
      [sg.Text('O lado do dado que caiu foi:')],
      [sg.Text(numeroAleatorio)]
    ])
    self.eventos, self.valores = self.janela.Read()
    print("O lado do dado que caiu foi:", numeroAleatorio)

simulador = Dado()
simulador.Iniciar()