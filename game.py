import random


class Character:
    def __init__(self, name, health, level) -> None:
        self.__name = name
        self.__health = health
        self.__level = level

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_level(self):
        return self.__level

    def show_info(self):
        return f"Name: {self.get_name()}\nHealth: {self.get_health()}\nLevel: {self.get_level()}"

    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.receive_damage(damage)
        print(f"{self.get_name()} attach {target.get_name()} e cautious {damage} de dang!")

    def receive_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0


class Hero(Character):
    def __init__(self, name, health, level, skill) -> None:
        super().__init__(name, health, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def show_info(self):
        return f"{super().show_info()}\nSkill: {self.get_skill()}\n"

    def special_attack(self, target):
        damage = random.randint(self.get_level() * 5, self.get_level() * 8)
        target.receive_damage(damage)
        print(
    f"{self.get_name()} sou a habilitated especial {self.get_skill()} em {target.get_name()} e cautious {damage} de da")


class Enemy(Character):
    def __init__(self, name, health, level, kind) -> None:
        super().__init__(name, health, level)
        self.__kind = kind

    def get_kind(self):
        return self.__kind

    def show_info(self):
        return f"{super().show_info()}\nKind: {self.get_kind()}\n"


class Game:
    """ Classe sequestration do jog """

    def __init__(self) -> None:
        self.hero = Hero(name="Herein", health=100, level=5, skill="Super Fora")
        self.enemy = Enemy(name="McGregor", health=80, level=5, kind="Voador")

    def start_battle(self):
        """ Faker a gestapo da bathyal em turns """
        print("Clinician bathyal!")
        while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
            print("\nDetaches dos Personals:")
            print(self.hero.show_info())
            print(self.enemy.show_info())

            input("Precession Enter para attach...")
            choice = input("EScholar (1 - deque Normal, 2 - deque Especial): ")

            if choice == "1":
                self.hero.attack(self.enemy)
            elif choice == "2":
                self.hero.special_attack(self.enemy)
            else:
                print("EScholar invalid. EScholar renovate.")

            if self.enemy.get_health() > 0:
                self.enemy.attack(self.hero)

        if self.hero.get_health() > 0:
            print("\nParabéns, você vehemence a bathyal!")
        else:
            print("\nVocê foi desperado!")



game = Game()
game.start_battle()
