class EqPrimG:


    def __init__(self,equacion):

        self.equacion = equacion.split()
        

    def calcula(self):
        part12 = self.equacion[0]
        part1 = int(part12[:-1])
        part2 = part12[1]
        operador = self.equacion[1]
        part3 = int(self.equacion[2])
        part4 = int(self.equacion[4])
        #print ("part1=",part1)
        #print ("part2=",part2)
        #print ("operator=",operador)
        #print ("part3=",part3)  
        #print ("part4=",part4) 


        
        if operador == "+":
            calculo = (part4 - part3) / part1
            return print ("resultado de",self.equacion," = ",calculo)

            
        elif operador == "-":
            calculo = (part4 + part3) / part1
            return print ("resultado de",self.equacion," = ",calculo)

        else: 
           return print("sintaxis erronea")
            
      


