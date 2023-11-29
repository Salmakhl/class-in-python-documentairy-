class documentaire():
    _counter = 0
    def __init__(self , titre = "titre" , date = 0):
        documentaire._counter += 1
        self.__titre = titre 
        self.__date = date
    

    #the getters
    
    
    def gettitre(self):
        return self.__titre
    
    def getdate(self):
        return self.__date
    
    def getcounter(self):
        return self._counter
    

    

    # the setters
    def setcode(self,code):
        self.__code = code

    def setcode(self,titre):
        self.__titre = titre

    def setcode(self,date):
        self.__date = date


    # methodes
    def TOSTRING(self):
        print(f" the code ={self.getcounter()}")
        print(f" the title ={self.gettitre()}")
        print(f" the date ={self.getdate()}")

    def equals(self,doc2): #the comparison between two vectors.
        #the first doc.
        
        titre1 = self.gettitre()
        date1 = self.getdate()
        #the second doc.
        
        titre2 = doc2.gettitre()
        date2 = doc2.getdate()
        if (titre1 == titre2) and ( date1 == date2) :
            return True
        else:
            return False
        


#the child class
class exemplaire(documentaire):
    def __init__(self,titre,date,num,datea):
        super().__init__(titre , date)
        documentaire._counter +=1
        self.__num = num
        self.__datea = datea

#THE GETTER
    def getnum(self):
        return self.__num

    
    def getdatea(self):
        return self.__datea
    
 # methodes
    def TOSTRING(self):
        print(f" the code ={self.getcounter()}")
        print(f" the title ={self.gettitre()}")
        print(f" the date ={self.getdate()}")
        print(f" the numero ={self.getnum()}")
        print(f" the date of purchase ={self.getdatea()}")

    def equals(self,doc2): #the comparison between two vectors.
        #the first doc.
        
        titre1 = self.gettitre()
        date1 = self.getdate()
        num1 = self.getnum()
        datea1 = self.getdatea()
        #the second doc.
        
        titre2 = doc2.gettitre()
        date2 = doc2.getdate()
        num2 = doc2.getnum()
        datea2 = doc2.getdatea()
        if (titre1 == titre2) and ( date1 == date2) and ( num1 == num2) and ( datea1 == datea2):
            return True
        else:
            return False
        


d1 = documentaire()
d2 = documentaire("ertyu",2345)
d1.TOSTRING()
d2.TOSTRING()
if d1.equals(d2) == True:
    print("is equals.")
else:
    print("is not equals.")
ex1 = exemplaire("tyui",3457,234,345)
ex2 = exemplaire("tyui",3457,234,345)
ex1.TOSTRING()
ex2.TOSTRING()
if ex1.equals(ex2)== True:
    print("is equal.")
else:
    print("isnot equals.")
    


