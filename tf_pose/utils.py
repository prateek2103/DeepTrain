import math

def get_angle(center1,center2,center3):
    x1, y1 = center1
    x2, y2 = center2
    x3, y3 = center3
    ang = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))
    if ang < 0:
        ang = ang+360

    if ang > 180:
        ang = 360-ang

    return ang