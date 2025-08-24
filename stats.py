import time
import math

class Stats:

    def __init__(self):
        self.final_status = ""
        self.start_time = time.time()
        self.civilians_spawned = 0
        self.marines_spawned = 0
        self.humans_infected = 0
        self.humans_consumed_by_player = 0
        self.attacked_by_marine = 0
        self.aliens_added_to_pack = 0

    def __str__(self):
        ret = ""
        ret += "Game Stats:\n"
        ret += f"  Final status: {self.final_status}\n"
        ret += f"  Time played: {math.floor(time.time() - self.start_time)} seconds\n"
        ret += f"  Civilians spawned: {self.civilians_spawned}\n"
        ret += f"  Colonial marines spawned: {self.marines_spawned}\n"
        ret += f"  Humans infected by face huggers: {self.humans_infected}\n"
        ret += f"  Humans consumed by you: {self.humans_consumed_by_player}\n"
        ret += f"  Attacks on you by marines: {self.attacked_by_marine}\n"
        ret += f"  Xenomorphs added to your pack: {self.aliens_added_to_pack}\n"

        return ret