import random

class SimuladorDeDado:
  def __init__(self):
    self.valor_minimo = 1
    self.valor_maximo = 6
    self.mensagem = "Quer jogar o dado? (sim ou não):  "

  def Iniciar(self):
    resposta = input(self.mensagem)
    if resposta == 'sim':
      self.GerarValorDoDado()
    else:
      print('blz fera')

  def GerarValorDoDado(self):
    print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()