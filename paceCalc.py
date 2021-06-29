def calc1(time, distance):
    if distance == 'marathon':
        distance = 26.2188
    elif(distance == 'half-marathon'):
        distance = 13.1094
    elif(distance == '10k'):
        distance = 6.21371
    elif(distance == '5k'):
        distance = 3.10686

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
calc1(1500, '5k')