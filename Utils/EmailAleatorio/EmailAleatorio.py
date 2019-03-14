from random import *

class Email_Aleatorio:

    def Radom(self):

        random.seed()
        random.randrange('abc', 'efg', 'hij')
        random.choice('abcdefghij')
        items = ['abc','def','ghi','jkl','mno','pqr','stu','vxz']
        random.shuffle(items)