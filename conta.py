class Conta:
    def __init__(self,numero,titular,saldo,limite):
        print("Construindo objeto ...")
        self.numero=numero
        self.titular=titular
        self.saldo=saldo
        self.limite=limite
    
    def extrato(self):
        print("O saldo do titular {} é {}".format(self.titular,self.saldo))
    