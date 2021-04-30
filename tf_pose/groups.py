from tf_pose.utils import get_angle
from numpy.lib.function_base import select


class Joints:
    def __init__(self):
        self.pairs=None
        self.parts=None
        self.angle_limits=None
        self.suggestions=None
        self.status_message=""

    def get_parts(self):
        return self.parts

    def get_pairs(self):
        return self.pairs

    def get_limit(self,joint):
        return self.angle_limits[joint]
    
    def get_suggestions(self):
        return self.suggestions

    def check_form(self,centers):
        pass

class Bicep(Joints):
    def __init__(self):
        super().__init__()
        self.parts=(2, 3, 4, 5, 6, 7)
        self.pairs=((2, 3), (3, 4), (5, 6), (6, 7))
        self.angle_limits={3:(30,160),
                            6:(30,160)}
        
        self.suggestions=["Fix your elbows","Squeeze at the top","Too heavy weight is good for nothing"]

    def check_form(self, centers):
        #check if shoulder is above elbow
        status=1
        try:
            if(centers[2] and centers[3]):
                if(not(centers[2][0]<centers[3][0])):
                    self.status_message ="Not performing the right exercise"
                    status=-1

            if(centers[5] and centers[6]):
                if(not(centers[5][0]<centers[6][0])):
                    self.status_message ="Not performing the right exercise"
                    status=-1
        except:
            print("working")
        return self.status_message,status

class Shoulder(Joints):
    def __init__(self):
        super().__init__()
        self.parts=(1, 2, 3, 4, 5, 6, 7)
        self.pairs=((2,1),(1,5),(2,3),(3, 4),(5, 6),(6, 7))
        self.angle_limits={3:(60,180),
                            6:(60,180),
                            1:(0,360)}
        self.suggestions=["Dont't lean back","Don't use momentum instead try a lighter weight","Keep it slow"]

    def check_form(self, centers):
        status=1
        try:
            if(centers[2] and centers[3] and centers[4]):
                ang=get_angle(centers[2],centers[3],centers[4])
                if((centers[2][0]<=centers[3][0]) and ang>90):
                    self.status_message ="Too much expansion of the arms."
                    status=-1
                    
            if(centers[5] and centers[6] and centers[7]):
                ang=get_angle(centers[5],centers[6],centers[7])
                if((centers[5][0]<=centers[6][0]) and ang>90):
                    self.status_message ="Too much expansion of the arms."
                    status=-1
        except:
            print("working")

        return self.status_message,status

class Tricep(Joints):
    def __init__(self):
        super().__init__()
        self.parts=(1,5,6,7,11,12)
        self.pairs=((5,6), (6, 7), (1, 11), (11,12)) 
        self.angle_limits={6:(70,180),11:(120,180)}
        self.suggestions=["Keep your back straight","Proper extension is necessary","Fix your shoulders for better results"]

    def check_form(self,centers):
        status=1
        return self.status_message,status
