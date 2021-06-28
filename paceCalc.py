def calc1(time, distance):

    global minutes
    global seconds
    
    if(time  >= 100):
        minutes = int(time / 100)
        seconds = time - 100*minutes
    else:
        print('add bug checking later')
  
  
    paceMinutes = int((time / distance) / 100)
    paceSeconds = (((minutes % distance) * 60) + seconds) / distance

    print("\n")
    print('--------------------------------------------')
    print(f'{paceMinutes}:{paceSeconds:.5} pace for {distance} miles')
    print('--------------------------------------------')
    print("\n")
    

#Enter Time and Distance below
calc1(2625, 5.4)