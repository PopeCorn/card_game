from Characters import David, Mojmir, Honza, Kvítek, Mark, Máta, Milan, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s

# Nic zatím nedělat

s.count = 0
if __name__ == "__main__":
    david = David.David()
    mata = Máta.Matyas()
    while True:
        s.count += 1
        if s.mata_poison is True:
            mata.poison(s.mata_poison_target)
            s.mata_poison = False
        exit()
        
        