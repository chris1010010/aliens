import time
import math

class Stats:

    def __init__(self):
        self.final_status = ""
        self.start_time = time.time()

    def __str__(self):
        ret = ""
        ret += "Game Stats:\n"
        ret += "  Final status: " + self.final_status + "\n"
        ret += f"  Time played: {math.floor(time.time() - self.start_time)} seconds\n"

        return ret