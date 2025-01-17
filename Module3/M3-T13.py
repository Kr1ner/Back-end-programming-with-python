while True:
    import pyfiglet
    import datetime
    import time
    import os
    from datetime import date
    today = date.today()
    now = datetime.datetime.now()
    print("Today:", today)
    print("Year:", today.year)
    print("Month:", today.month)
    print("Day:", today.day)
    print(f"CURRENT TIME".center(50))
    print(pyfiglet.figlet_format(f"{now.hour}:{now.minute}:{now.second}",font="5x7").center(50))
    time.sleep(1)
    os.system('cls')
    os.system('clear')
