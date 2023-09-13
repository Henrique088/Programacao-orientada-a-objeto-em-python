class data:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        if (self.dia <=9 and self.mes<=9):
             print("0{}/0{}/{}".format(self.dia,self.mes,self.ano))
        elif(self.dia <=9 and self.mes>9):
            print("0{}/{}/{}".format(self.dia, self.mes, self.ano))
        elif(self.dia>9 and self.mes<=9):
            print("{}/0{}/{}".format(self.dia, self.mes, self.ano))
        else:
            print("{}/{}/{}".format(self.dia, self.mes, self.ano))
