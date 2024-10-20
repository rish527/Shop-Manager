from math import radians, cos, sin, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    lon2=float(lon2)
    lat2=float(lat2)
    R=6371.0
    dlat=radians(lat2-lat1)
    dlon=radians(lon2-lon1)

    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance=R*c
    return distance
                                          