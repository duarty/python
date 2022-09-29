class Movie:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.exibitions = 0
    

    def __str__(self):
        return f'Movie: {self.name}'

    
    def __call__(self):
        self.exibitions += 1
        return self.exibitions


    def __len__(self):
        return self.duration


