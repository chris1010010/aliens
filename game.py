import sys

def exit_game(stats, final_status):
    print("Game over!")
    stats.final_status = final_status
    print(stats)
    sys.exit(0)