class Game():
    def __init__(self, choice_1, choice_2):
        self.choice_1 = choice_1
        self.choice_2 = choice_2
    
    def game_function(self):
   
        if self.choice_1 == self.choice_2:
            return f"Nobody Wins! Both players have chosen {self.choice_1}!"
# ....
        elif self.choice_1 == "rock":
            if self.choice_2 == "scissors":
                return "You Win! Rock crushes Scissors!"
            elif self.choice_2 == "lizard":
                return "You Win! Rock crushes Lizard!"
            elif self.choice_2 == "spock":
                return "The Computer Wins! Spock vaporizes Rock!"
            else:
                return "The Computer Wins! Paper covers Rock!"
# ....
        elif self.choice_1 == "paper":
            if self.choice_2 == "rock":
                return "You Win! Paper covers Rock!"
            elif self.choice_2 == "spock":
                return "You Win! Paper disproves Spock!"
            elif self.choice_2 == "lizard":
                return "The Computer Wins! Lizard eats Paper!"
            else:
                return "The Computer Wins! Scissors cut paper!"
# ....
        elif self.choice_1 == "scissors":
            if self.choice_2 == "paper":
                return "You Win! Scissors cut paper!"
            elif self.choice_2 == "lizard":
                return "You Win! Scissors decapitate Lizard!"
            elif self.choice_2 == "spock":
                return "The Computer Wins! Spock smashes Scissors!"
            else:
                return "The Computer Wins! Rock beats scissors!"
# ....
        elif self.choice_1 == "lizard":
            if self.choice_2 == "paper":
                return "You Win! Lizard eats Paper!"
            elif self.choice_2 == "spock":
                return "You Win! Lizard poisons Spock!"
            elif self.choice_2 == "scissors":
                return "The Computer Wins! Scissors decapitate Lizard!"
            else:
                return "The Computer Wins! Rock crushes Lizard!"
# ....
        elif self.choice_1 == "spock":
            if self.choice_2 == "scissors":
                return "You Win! Spock smashes Scissors!"
            elif self.choice_2 == "rock":
                return "You Win! Spock vaporizes Rock!"
            elif self.choice_2 == "lizard":
                return "The Computer Wins! Lizard poisons Spock!"
            else:
                return "The Computer Wins! Paper disproves Spock!"
        #  ..........       
        # elif self.choice_1 == "rock":
        #     if self.choice_2 == "lizard":
        #         return "You Win! Rock crushes Lizard!"
        #     else:
        #         return "The Computer Wins! Rock crushes Lizard!"
        # elif self.choice_1 == "lizard":
        #     if self.choice_2 == "spock":
        #         return "You Win! Lizard poisons Spock!"
        #     else:
        #         return "The Computer Wins! Lizard poisons Spock!"
        # elif self.choice_1 == "spock":
        #     if self.choice_2 == "scissors":
        #         return "You Win! Spock smashes Scissors!"
        #     else:
        #         return "The Computer Wins! Spock smashes Scissors!"
        # elif self.choice_1 == "scissors":
        #     if self.choice_2 == "lizard":
        #         return "You Win! Scissors decapitate Lizard!"
        #     else:
        #         return "The Computer Wins! Scissors decapitate Lizard!"
        # elif self.choice_1 == "lizard":
        #     if self.choice_2 == "paper":
        #         return "You Win! Lizard eats Paper!"
        #     else:
        #         return "The Computer Wins! Lizard eats Paper!"
        # elif self.choice_1 == "paper":
        #     if self.choice_2 == "spock":
        #         return "You Win! Paper disproves Spock!"
        #     else:
        #         return "The Computer Wins! Paper disproves Spock!"
        # elif self.choice_1 == "spock":
        #     if self.choice_2 == "rock":
        #         return "You Win! Spock vaporizes Rock!"
        #     else:
        #         return "The Computer Wins! Spock vaporizes Rock!"
