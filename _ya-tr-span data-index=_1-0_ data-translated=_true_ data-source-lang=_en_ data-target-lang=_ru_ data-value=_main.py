from random import randint as rnd

class Voin:

    def __init__(self, name, zdorovie, injury):
        self.name = name
        self.zdorovie = zdorovie
        self.inijury = injury

    def hit(self, Unit):
        Unit.zdorovie -= self.inijury
        if Unit.zdorovie > 0:
            print(f'"{self.name}" атакует "{Unit.name}". ранен "{Unit.name}" жив {Unit.zdorovie} здоровья')
        else:
            print(f'"{self.name}" атакует "{Unit.name}". "{Unit.name}" убит')
            Unit.zdorovie = 0
        return Unit.zdorovie


Unit1 = Voin('Воин 1', 100, 20)
Unit2 = Voin('Воин 2 ', 100, 20)
Unit = [Unit1, Unit2]
while True:
    attack_index = rnd(0, 1)
    s_index = (attack_index + 1) % 2
    s_zdorovie = Unit[attack_index].hit(Unit[s_index])
    if s_zdorovie == 0:
        print(f'"{Unit[attack_index].name}" Победил!')
        break
