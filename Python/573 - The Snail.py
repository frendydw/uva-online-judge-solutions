while True:
    try:
        heigh, climb, slide, fatigue = map(int, input().split())
        if heigh == 0:
            break
        day = 1
        distance = 0
        heighClimbed = 0
        heighAfterSlide = 0
        flag = True
        climbFatigue = climb
        while True:
            initHeight = heighAfterSlide
            if day > 1:
                climbFatigue = climbFatigue - (climb * fatigue/100)
            if climbFatigue > 0:
                distance = climbFatigue + initHeight
                heighClimbed = distance
                heighAfterSlide = heighClimbed - slide
            else:
                heighAfterSlide -= slide
            
            if heighAfterSlide < 0:
                flag = False
                break
            elif heighClimbed > heigh:
                break
            day += 1
        
        if flag:
            print("success on day {}".format(day))
        else:
            print("failure on day {}".format(day))

            
    except EOFError:
        break