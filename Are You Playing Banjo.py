def areYouPlayingBanjo(name):
    # Implement me!
    str_name=str(name)
    
    if str_name[0]=="R" or str_name[0]=="r":
        return name +" plays banjo" 
    else:
        return name + " does not play banjo"