import os
screen = dict()
cratio = 3.5
empty,symb,Food = " ","@","0"
speed = 3
cx,cy = 0,0 #скорость
am = False
Finded = False
FoodX,FoodY = 0,0
cmdX,cmdY = os.get_terminal_size()[0],os.get_terminal_size()[1] #Разрешение cmd
centerX,centerY = round(cmdX/2),round(cmdY/2)       #Центр
ratioCMD = cmdX/cmdY
D = min(cmdY,int(cmdX/ratioCMD))//5 #Диаметр круглика
r = round(D/2)
rc = r//5
ratio = round(cmdX/cmdY*0.5)
horiz, vertic = True, False #Направление мяча. Horiz True - право, Vertic True - вверх
for frames in range(0,1000000):
    for fory in range(0,cmdY):
        for forx in range(0,cmdX):
            x, y = forx, (cmdY-fory)
            i = cmdX*(y-1)+x      # i - Символ по счёту. График перевёрнутый по y(по вертикали)
            screen[i] = empty #Заполнение ячеек пустотой
            cyrcleX, cyrcleY = centerX + cx , centerY + cy # Середина круга
            maxFoX, minFoX = round(cmdX-D),D-1       #-1 Потому что счёт идёт с 0
            maxFoY, minFoY = round(cmdY-(round(r)))-1,round(r)
            #Ограничение для пакмена по краям окна
            if centerY+cy+r>=cmdY:vertic = False
            elif centerY+cy-r+1<=0:vertic = True    #+1 потому что последняя строка не заполняется
            if cyrcleX>=cmdX-D+1:horiz = False
            elif cyrcleX<=D-2:horiz = True
            #Направление пакмена
            if vertic is True: cy += 0.00002*speed
            else: cy -= 0.00002*speed
            if horiz is True: cx += 0.00002*speed
            else: cx -= 0.00002*speed
            # Круг через формулы
            if (x-cyrcleX)** 2 + (y-cyrcleY)**2*cratio <= D ** 2: screen[i] = symb
            #ПРАВО ВВЕРХ
            if vertic == True and horiz == True:
                if round(cyrcleX) - round(r/2) == x and round(cyrcleY) + round(r*3/4) == y: screen[i] = empty
                if am == False:
                    if x>cyrcleX and y>cyrcleY :screen[i] = empty
                
                if Finded is False:
                    if (cmdX-cyrcleX)>(cmdY-cyrcleY):       #Еда по X(Низ|вверх)
                        FoodX,FoodY = round(cyrcleX+round(cmdY-cyrcleY)),maxFoY+round(r/2)
                        Finded = True
                    else:
                        FoodX,FoodY = maxFoX+r,round(cyrcleY+(cmdX-cyrcleX)-r)
                        Finded = True

                elif am == False and round((FoodX - x) ** 2 / ratio + (FoodY - y) ** 2) <= round(rc):
                    screen[i] = Food
            #ПРАВО ВНИЗ
            if vertic == False and horiz == True:
                if round(cyrcleX)+round(r) == x and round(cyrcleY)+round(r*1/7) == y:screen[i] = empty
                if am == False:
                    if x>cyrcleX and y<cyrcleY:screen[i]=empty

                if Finded is False:
                    if (cmdX-cyrcleX)>cyrcleY:
                        FoodX,FoodY = round(cyrcleX+cyrcleY),minFoY-round(r/2)
                        Finded = True
                    else:
                        FoodX,FoodY = maxFoX+r,round(cyrcleY-(cmdX-cyrcleX))+r+1
                        Finded = True
                elif am == False and round((FoodX - x) ** 2 / ratio + (FoodY - y) ** 2) <= round(rc):
                    screen[i] = Food
            #ВЛЕВО ВВЕРХ
            if vertic == True and horiz == False:
                if round(cyrcleX)+round(r/2) == x and round(cyrcleY)+round(r*3/4) == y:screen[i] = empty
                if am == False:
                    if x<cyrcleX and y>cyrcleY :screen[i]=empty

                    if Finded is False:
                        if cyrcleX > cmdY-cyrcleY:
                            Finded = True
                            FoodX, FoodY = round(cyrcleX - (cmdY-cyrcleY)), maxFoY + round(r / 2)
                        else:
                            Finded = True
                            FoodX, FoodY = minFoX - round(r / 2), round(cyrcleY + cyrcleX-r)
                    elif am == False and round((FoodX - x) ** 2 / ratio + (FoodY - y) ** 2) <= round(rc):
                        screen[i] = Food
            #ВЛЕВО ВНИЗ
            if vertic == False and horiz == False:
                if round(cyrcleX)-round(r) == x and round(cyrcleY)+round(r/2/2) == y:screen[i] = empty
                if am == False:
                    if x<cyrcleX and y<cyrcleY :screen[i]=empty

                if Finded is False:
                    if cyrcleX > cyrcleY:
                        Finded = True
                        FoodX, FoodY = round(cyrcleX - cyrcleY), minFoY - round(r / 2)

                    elif cyrcleX <= cyrcleY :
                        Finded = True
                        FoodX, FoodY = minFoX - round(r/2 * ratio), round(cyrcleY - cyrcleX)
                elif am is False and round((FoodX - x) ** 2 / ratio + (FoodY - y) ** 2) <= round(rc):screen[i] = Food
    #Вывод на экран
    if cyrcleY >= maxFoY or cyrcleY <= minFoY or cyrcleX >= maxFoX or cyrcleX <= minFoX:am,Finded = True, False
    else:am = False
    fullscreen = ""
    for value in screen.values():fullscreen += str(value)
    else:print(fullscreen,end="")
    #print(D)
