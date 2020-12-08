class Joints:
    def __init__(self):
        self.pairs=None
        self.parts=None
        self.angle_limits=None
        self.suggestions=None

    def get_parts(self):
        return self.parts

    def get_pairs(self):
        return self.pairs

    def get_limit(self,joint):
        return self.angle_limits[joint]
    
    def get_suggestions(self):
        return self.suggestions

class Bicep(Joints):
    def __init__(self):
        super().__init__()
        self.parts=(2, 3, 4, 5, 6, 7)
        self.pairs=((2, 3), (3, 4), (5, 6), (6, 7))
        self.angle_limits={3:(50,170),
                            6:(50,170)}
        
        self.suggestions=["Fix your elbows","Squeeze at the top","Too heavy weight is good for nothing"]


class Shoulder(Joints):
    def __init__(self):
        super().__init__()
        self.parts=(1, 2, 3, 4, 5, 6, 7)
        self.pairs=((2,1),(1,5),(2,3),(3, 4),(5, 6),(6, 7))
        self.angle_limits={3:(60,180),
                            6:(60,180),
                            1:(0,360)}
        self.suggestions=["Dont't lean back","Don't use momentum instead try a lighter weight","Keep it slow"]


class Tricep(Joints):
    def __init__(self):
        super().__init__()
        self.parts=(1,5,6,7,11,12)
        self.pairs=((5,6), (6, 7), (1, 11), (11,12)) 
        self.angle_limits={6:(70,180),11:(120,180)}
        self.suggestions=["Keep your back straight","Proper extension is necessary","Fix your shoulders for better results"]
