"""

codice contea, x, y, popolazione, rischio di cancro

"""

class Contea:

    def __init__(self, id, x, y, pop, risk):
        self.id = id
        self.x = x
        self.y = y
        self.population = pop
        self.cancer_risk = risk

    def __str__(self):
        s = "id: " + str(self.id)
        return s

    def __repr__(self):
        s = "id: " + str(self.id)
        return s

