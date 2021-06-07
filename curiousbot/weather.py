def simpleweather(request, loc):
    masterurl = "https://wttr.in/"  # website used to get our info
    if request == "simple":
        newurl = masterurl + loc + "?format=3"  # builds url
        print(newurl)
        return newurl
    elif request == "sexy":
        modify = list(loc)
        for idx, val in enumerate(modify):  # handles spaces in strings
            if val == " ":
                modify[idx] = "+"
                loc = "".join(modify)
                newurl = masterurl + loc + ".png"
        return newurl
