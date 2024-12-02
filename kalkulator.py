import json
import math

with open("karakterer\Ram.json", "r") as ram_raw:
    ram_parsed = json.load(ram_raw)

with open("karakterer/risc_scaling.json", "r") as risc_scaling_chart_raw:
    risc_scaling_chart = json.load(risc_scaling_chart_raw)

class kalkisbrur():
    def __init__(self, ram_parsed, risc_scaling_chart):
                
        # ============ Decay når man starter med visse moves ==============
        high_low_start_decay = 5  # does not count charged dust
        projectile_start_decay = 5
        high_risc_loss_start_decay = 5  # for moves with 1500 or 2000 risc loss
        six_p_start_decay = 20
        counterhit_start = -10

        # ============ R.I.S.C. variabler ==============
        self.risc = 0
        self.max_risc = 12800

        # ============ Combo variabler ==============
        self.full_combo_damage = 0
        self.beat = 0
        self.move_damage = 0
        self.valid_attack_tf = False

        # ============ Movelist Select variabler ==============
        self.movelist = {}
        self.number_of_moves = 0


        for move in ram_parsed:
            self.number_of_moves += 1
            self.movelist[move] = self.number_of_moves
        self.select_move()
        



    
    def select_move(self): 


        for move in self.movelist:
            print(move, ":", self.movelist[move])

        attack = input("select which move to do: ")

        try:
            attack = int(attack)
        except:
            print("Invalid input")

        for move in self.movelist:
            if attack == self.movelist[move]:
                self.valid_attack_tf = True
                self.move_damage = ram_parsed[move]["damage"]
                self.attack_name = move

        print(self.valid_attack_tf)


        print(f"You selected: {attack}")
        self.damage_calculation()

    def damage_calculation(self):
        if self.risc >= self.max_risc:
            self.risc = self.max_risc
        print(self.risc)

        for risc_id in risc_scaling_chart:
            if self.risc >= risc_scaling_chart[risc_id]["risc"] and self.risc < risc_scaling_chart[str(int(risc_id)+1)]["risc"]:
                if type(self.move_damage) == int:
                    factor_interpolated = risc_scaling_chart[risc_id]["factor"] + (risc_scaling_chart[str(int(risc_id)+1)]["factor"]- risc_scaling_chart[risc_id]["factor"]) * (self.risc - risc_scaling_chart[risc_id]["risc"]) / (risc_scaling_chart[str(int(risc_id)+1)]["risc"] - risc_scaling_chart[risc_id]["risc"])
                    self.move_damage_post_scaling = math.floor(self.move_damage * math.floor(factor_interpolated) / 256)
                    if self.move_damage_post_scaling <= 0:
                        self.move_damage_post_scaling =1
                    self.risc += ram_parsed[self.attack_name]["risc loss"]
                    break
                if type(self.move_damage) == list:
                    self.move_damage_post_scaling = []
                    for hit in self.move_damage:
                        factor_interpolated = risc_scaling_chart[risc_id]["factor"] + (risc_scaling_chart[str(int(risc_id)+1)]["factor"]- risc_scaling_chart[risc_id]["factor"]) * (self.risc - risc_scaling_chart[risc_id]["risc"]) / (risc_scaling_chart[str(int(risc_id)+1)]["risc"] - risc_scaling_chart[risc_id]["risc"])
                        temp_var_move_move_damage_post_scaling = math.floor(hit * math.floor(factor_interpolated) / 256)
                        if temp_var_move_move_damage_post_scaling <= 0:
                            temp_var_move_move_damage_post_scaling =1
                        self.move_damage_post_scaling.append(int(temp_var_move_move_damage_post_scaling))
                    self.risc += ram_parsed[self.attack_name]["risc loss"]
                    break

        print(self.move_damage)
        print(self.move_damage_post_scaling)
                



if __name__ == "__main__":
    kalkisbrur(ram_parsed, risc_scaling_chart)
