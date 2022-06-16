def control():
    conf()
    l,r=0,0
    x=-(int(line[0]))
    y=-(int(line[1]))
    left=(int(line[2]))
    right=(int(line[3]))
    print(line)
    if left==0 and right==1:
        print("Next")
    if right==0 and left==1:
        print("Prev")
    if right==1 and left==1:
        conf()
        leftT=(int(line[2]))
        rightT=(int(line[3]))
        x=-(int(line[0]))
        delay(30000)
        if right==1 and left==1 and x>3:
            c=False
        else:
            c=True
        if c==True:
            if play==True:
                play=False
                print("Pause")
            if play==False:
                play=True
                print("Play")