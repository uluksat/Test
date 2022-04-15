import random

class GTA: 
    def __init __(self, carecter):
        if carecter!="Mikl" and carecter!="Trewor" and carecter!="Franklin":
            print("Netu takogo personaja")
        else:
            self.carecter=carecter
        self.health=100
        self.money=100
        self.satietly=100
        self.walk=0

    def info(self):
        return f"{self.health}, {self.money}, {self.satietly}, {self.walk}"

    def walk(self):
        self.walk+=1
        

    



        
    
