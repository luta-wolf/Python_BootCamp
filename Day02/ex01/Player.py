# Cheater
# Detective
# Grudger
# Copycat
# Cooperator

class Player(object):
    def __init__(self, name: str = "Player", behaviour: str = None):
        self.name = name
        self.behaviour = behaviour

    def put_candy(self):
        put_count = 0 if self.behaviour == "Cheater" else 1
        return put_count

    def get_candy(self, n):
        self.change_behaviour(opponent_behaviour='Cheater' if n == 0 else "Cooperator")

    def change_behaviour(self, opponent_behaviour):
        pass


class Cheater(Player):
    def __init__(self):
        super().__init__(name="Cheater", behaviour="Cheater")


class Cooperator(Player):
    def __init__(self):
        super().__init__(name="Cooperator", behaviour="Cooperator")


class Copycat(Player):
    def __init__(self):
        super().__init__(name="Copycat", behaviour="Cooperator")

    def change_behaviour(self, opponent_behaviour):
        self.behaviour = opponent_behaviour


class Grudger(Player):
    def __init__(self):
        super().__init__(name="Grudger", behaviour="Cooperator")

    def change_behaviour(self, opponent_behaviour):
        if opponent_behaviour == "Cheater":
            self.behaviour = "Cheater"


class Detective(Player):
    def __init__(self):
        super().__init__(name="Detective", behaviour="Cooperator")
        self.history = []

    def change_behaviour(self, opponent_behaviour):
        self.history.append(opponent_behaviour)
        if len(self.history) == 1:
            self.behaviour = "Cheater"
        elif len(self.history) == 2 or len(self.history) == 3:
            self.behaviour = "Cooperator"
        elif len(self.history) >= 4 and "Cheater" in self.history[:4]:
            self.behaviour = opponent_behaviour
        elif len(self.history) >= 4 and "Cheater" not in self.history[:4]:
            self.behaviour = "Cheater"

