import csv

class Player_Data:
    def __init__(self):
        self.file_name = "file/player.csv"

    def read_all_players(self):
        return_list = []
        with open(self.file_name, newline = "",encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                return_list.append(Player(line["name"], line["id_number"]))
            return return_list


    def create_player(self, player):
        with open(self.file_name, "a", newline = "", encoding = "utf-8") as csvfile:
            fieldname = ["name", "id_number"]
            writer = csv.DictWriter(csv, fieldnames=fieldnames)

            writer.writeline({"name": player.name, "id_number": player.id_number})
            
