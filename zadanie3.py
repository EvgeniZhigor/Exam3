class Tomato:
    states={0:'byton',1:'cvet',2:'plod'}
    def __init__(self,index):
        self._index=index
        self._state=0


    def grow(self):
        self._change()


    def is_ripe(self):
        if self._state == 2:
            return True
        return False


    def _change(self):
        if self._state<2:
            self._state+=1
        self._vivod()


    def _vivod(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

class TomatoBush:
    def __init__(self,kol):
        self.tomatoes = [Tomato(index) for index in range(0, kol)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self,name,plant):
        self.name=name
        self._plant=plant

    def work(self):
        print('Работаем')
        self._plant.grow_all()
        print('Работа окончена')

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Все плоды созрели, урожай собран')
        else:
            print('плоды ещё не созрели, рано собирать урожай')

    @staticmethod
    def knowledge_base():
        print('''Ухаживать за помидорами, в том числе и за зелёными, может быть и легко, и хлопотно. 
        Все зависит от желаемого количества урожая. Помидор отзывчив на все агротехнические мероприятия. 
        Необходимый уход включает полив, подкормку, рыхление почвы, подвязывание, окучивание, прополку сорняков, а также защиту от вредителей и болезней.
        Помидоры любят оптимальный полив по мере высыхания почвы, не учитывая дождей. С ними - и того реже.
        Самое главное, чтобы воды хватало в момент образования завязей и до окончания налива плодов. 
        Если поливать помидоры капельным или подземным способом, в вечернее время, под корень, либо по бороздам - они никогда не заболеют вершинной гнилью плодов.
        Также помидоры редко болеют, если при поливе добавлять в воду немного золы.
        ост и плодоношение возрастут''')

Gardener.knowledge_base()
tomatobush=TomatoBush(3)
gardener=Gardener('Женя',tomatobush)
gardener.work()
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()

