from random import *

class Email_Aleatorio:

    def Radom(self):

        random.seed()  # inicia a semente dos número pseudo randômicos
        random.randrange(8, 1500, 100)  # pares entre 0 e 9
        random.choice('abcdefghij')  # seleciona um dos elementos aleatoriamente
        items = [1, 2, 3, 4, 5, 6, 7,8,9,0]
        random.shuffle(items)  # embaralha os itens aleatoriamente