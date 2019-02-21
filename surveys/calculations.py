def findIntercept(profile, stations, intercept_point):
    stations_found = False
    i = 0
<<<<<<< HEAD
    while not stations_found and i < len(stations)-1:
        if i == len(stations)-1 :
            i += 1
=======
    while(!stations_found && i < stations.length-1):
        if(i == stations.length-1):
            i++
>>>>>>> parent of e4738e5... Update calculations.py
        else:
            if intercept_point <= stations[i].true_elevation and intercept_point > stations[i + 1].true_elevation:
                pult_index = i
                station_pult = stations[i]
                station_ult = stations[i+1]
                stations_found = True
            else:
                i += 1
    
    if stations_found:
        m = (station_ult.true_elevation - station_pult.true_elevation) / (station_ult.true_distance - station_pult.true_distance)
        b = station_pult.true_elevation / (m * station_pult.true_distance)
        x_int = (intercept_point - b) / m
        return pult_index, x_int
        
    return False

def calcBeachWidth(profile, stations, intercept_point):
    pult_index, mhhw = findIntercept(profile=profile, stations=stations, intercept_point=intercept_point)
    width = mhhw - stations[0]
    return width

def calcBeachVolume(profile, stations, intercept_point):
    pult_index, mllw = findIntercept(profile=profile, stations=stations, intercept_point=intercept_point)
    volume = 0
<<<<<<< HEAD
    for i in range(len(stations)-1):
        if i == pult_index:
            left = stations[i].true_elevation - intercept_point
            distance = mllw - stations[i].true_distance
=======
    for i in range(stations.length-1):
        if(i == pult_index):
            left = station[i].true_elevation - intercept_point
            distance = mllw - station[i].true_distance
>>>>>>> parent of e4738e5... Update calculations.py
            trapezoid_area = left * distance / 2
            volume += trapezoid_area

            return volume
        else:
            left = stations[i].true_elevation - intercept_point
            right = stations[i+1].true_elevation - intercept_point
            distance = stations[i+1].true_distance - stations[i].true_distnace
            trapezoid_area = (left + right) * distance / 2 
            volume += trapezoid_area
        
    return volume