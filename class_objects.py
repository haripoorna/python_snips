class LotteryPlayer:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        self.list = [1, 1, 1, 2, 4, 5]

    def total(self):
        return sum(self.list)


player = LotteryPlayer('hari', 'kalahasti')

print(player.total())