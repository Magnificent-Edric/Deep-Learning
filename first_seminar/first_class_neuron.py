class Neuron:
    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f
        self.x = None
    def forward(self, x):
        self.x = x
        self.suma = 0
        for i in range(len(self.w)):
            self.suma += self.x[i] * self.w[i]
        return self.f(self.suma)
    def backlog(self):
        return self.x