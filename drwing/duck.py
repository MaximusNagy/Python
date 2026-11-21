import os
import time
from colorama import init, Fore

init(autoreset=True)

duck1 = Fore.YELLOW + r"""
   __
<(o )___
 ( ._> /
  `---'
"""

duck2 = Fore.CYAN + r"""
   __
<( ^ )___
 ( ._> /
  `---'
"""

colors = [Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.GREEN, Fore.RED]

while True:
    for color in colors:
        os.system('cls')
        print(color + duck1)
        time.sleep(0.25)

        os.system('cls')
        print(color + duck2)
        time.sleep(0.25)