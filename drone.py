class Cdrone:
    
    def __init__(self,type,sn):
        self.type=type
        self.sn=sn  
    def getType(self):
        return self.type 
    def getSN(self):
        return self.sn
    def getOrientation(self):
        return self.orientation
    def getStatus(self):
        return self.status
    def setOrientation(self,orientation:int):
        orin=[1, 2, 3, 4]
        while orientation not in orin:
            orientation=int(input("get orientation:"))
        self.orientation=orientation
    def setEtat(self,status):
        stat=["en service","en reparation","hors service"]
        while status not in stat:
            status=input("get etat:")
        self.status=status
    def rtn_orientation(self):
        orient={1:'nord',2:'est',3:'sud',4:'ouest'}
        orin=self.orientation
        return orient[orin]
        
                
    def tourner(self):
        ori=self.orientation
        if ori==1:
            ori=4
        else:
            ori-=1
        self.orientation=ori
    def afficher(self):
        print("l'etat {},l'orientation {}:{},numero serie {},type {}".format(self.status,self.orientation,self.rtn_orientation(),self.sn,self.type))
        
''' partie B'''
class CdroneMobile(Cdrone):
    def __init__(self,type,sn,abs,ord):
        super().__init__(type,sn)
        self.abs=abs
        self.ord=ord
    
    def avancer(self,x):
        ori=self.orientation
        if ori == 2:
            self.abs += x
        if ori == 1:
            self.ord += x    
        if ori == 4:
            self.abs -= x
        if ori == 3:
            self.ord -= x
          
    def affichePosition(self):
        print("l'abscisse est {} ,l'ordonnee est {}".format(self.abs,self.ord))
    def afficher(self):
        super().afficher()
        self.affichePosition()
        
drone=CdroneMobile('helicopter',123,30,245)
drone.setOrientation(6)
drone.setEtat('en service')
drone.afficher()
drone.tourner()
drone.afficher()
drone.avancer(5)
drone.afficher()

