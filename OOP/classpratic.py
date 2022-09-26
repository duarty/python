from datetime import datetime

class Person:

    actual_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name;
        self.age = age;
        self.eating = eating;
        self.speaking = speaking;
        

    def eat(self, fruit):

        if self.speaking:
            print(f'{self.name} não pode comer pois está falando!');
            return

        if self.eating:
            return print(f'{self.name} já está comendo');

        self.eating = True;
        print(f'{self.name} está comendo {fruit}!');


    def stop_eat(self):

        if not self.eating:
            return print(f'{self.name} não está comendo!');
        
        self.eating = False;
        print(f'{self.name} parou de comer!');


    def speak(self, subject):

        if self.eating:
            print(f'{self.name} não pode falar pois está comendo!');
            return

        if self.speaking:
            print(f'{self.name} já está falando');
            return
        
        self.speaking = True;
        print(f'Olá sou {self.name}, e vou falar sobrem {subject}');

    
    def stop_speak(self):

        if not self.speaking:
            print(f'{self.name} não está falando!');

        print(f'{self.name} não está mais falando');
        self.speaking =  False

    def get_bithday_year(self):
        print(self.actual_year - self.age)
        return 
    

        


 
