def calc1(time, distance):
    #minutes = int(time / 100)
    #seconds = time - (minutes * 100)
    #print(f'Time is {minutes}:{seconds}')
    minutes = 1
    seconds = 1
    if(time  >= 100):
        minutes = int(time / 100)
        seconds = time - 100*minutes
    else:
        print('add feature later')

    td = time/distance
  
    paceMinutes = int((time / distance) / 100)
    paceSeconds = (((minutes / distance) - paceMinutes) * (paceMinutes * 60) + seconds) / distance
    print("\n")
    print('--------------------------------------------')
    print(f'{paceMinutes}:{paceSeconds:.6} pace for {distance} miles')
    print('--------------------------------------------')
    print("\n")




calc1(2625, 5)