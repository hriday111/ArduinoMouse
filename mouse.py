def ms():
    conf()
    l,r=0,0
    x=-(int(line[0]))*10
    y=-(int(line[1]))*10
    left=(int(line[2]))
    right=(int(line[3]))
    print(line)
    if left==0 and right==1:
        mouse.press(Button.left)
        while l==0:
            conf()
            lTemp=(int(line[2]))
            print(lTemp)
            if lTemp==0:
                mouse.release(Button.left)
                l=1
    if right==0 and left==1:
        mouse.press(Button.right)
        while r==0:
            conf()
            rTemp=(int(line[3]))
            if rTemp==0:
                mouse.release(Button.right)
                r=1
    if right==1 and left==1:
        conf()
        leftT=(int(line[2]))
        rightT=(int(line[3]))
        x=-(int(line[0]))
        delay(30000)
        if right==1 and left==1 and x>3:
            c=True
        else:
            c=False
        if c==False:

            if y>0:
                mouse.scroll(0, 1)
            if y<0:
                mouse.scroll(0, -1)
            x,y=0,0
    mouse.move(x, y)