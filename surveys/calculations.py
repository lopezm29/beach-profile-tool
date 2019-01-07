def findIntercept(profile, stations, intercept_point):
    stations_found = False
    i = 0
    while(!stations_found && i < stations.length-1):
        if(i == stations.length-1):
            i++
        else:
            if (intercept_point <= stations[i].true_elevation && intercept_point > stations[i + 1].true_elevation):
                pult_index = i
                station_pult = stations[i]
                station_ult = stations[i+1]
                stations_found = True
            else:
                i++
    
    if(stations_found):
        m = (station_ult.true_elevation - station_pult.true_elevation) / (station_ult.true_distance - station_pult.true_distance)
        b = station_pult.true_elevation / (m * station_pult.true_distance)
        x_int = (intercept_point - b) / m
        return pult_index, x_int

def calcBeachWidth(profile, stations, intercept_point):
    pult_index, mhhw = findIntercept(profile=profile, stations=stations, intercept_point=intercept_point)
    width = mhhw - stations[0]
    return width

def calcBeachVolume(profile, stations, intercept_point)
    pult_index, mllw = findIntercept(profile=profile, stations=stations, intercept_point=intercept_point)
    volume = 0
    for i in range(stations.length-1):
        if(i == pult_index):
            left = station[i].true_elevation - intercept_point
            distance = mllw - station[i].true_distance
            trapezoid_area = left * distance / 2
            volume += trapezoid_area

            return volume
        else:
            left = station[i].true_elevation - intercept_point
            right = station[i+1].true_elevation - intercept_point
            distance = station[i+1].true_distance - station[i].true_distnace
            trapezoid_area = (left + right) * distance / 2 
            volume += trapezoid_area
        
    return volume