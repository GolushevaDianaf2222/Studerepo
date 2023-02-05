class fruits:

    def __init__(self, taste):
        self.taste = taste
        self.in_move = False

    def drive(self):
        self.in_move = True

    def stop(self):
        self.in_move = False

    def get_info(self):
        return self.taste

class allergy(fruits):

    def __init__(self, taste, term):
        super().__init__(taste=taste)
        self.term = term

    def get_info(self):
        return f'taste: {self.taste}, term: {self.term}'

class sweet (fruits):

    def __init__(self, taste='-'):
        super().__init__(taste=taste)

    def lock_fruit(self):
        self.is_locked = True

    def unlock_fruit(self):
        self.is_locked = False

if __name__ == '__main__':
     fruit1 = fruits('orange')
     fruit2 = allergy('citrus',11)
     fruit3 = sweet()

     fruit = [fruit1, fruit2, fruit3]

     for fruit in fruit:
        print(fruit.taste)

     print(fruit1.get_info())
     print(fruit2.get_info())
     fruit3.lock_fruit()
     print(fruit3.is_locked)


