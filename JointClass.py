
# creating a class: to create a user defined programme.
# method are codes or functions inside class
# setting up the instructor method

class joint ():
    def __init__(self,x,y):
        self.xcoord = x
        self.ycoord = y
class member ():
    def __init__(self, startJoint, endJoint):
        self.startJoint = startJoint
        self.endJoint = endJoint


class load ():
    def __init__(self,Joint, Magnitude, direction):
        self.Joint= Joint
        self.Magnitude = Magnitude
        self.direction = direction

class support():
    def __init__(self, joint, supportType):
        self.joint = joint
        self.supportType = supportType
#A =joint(0,0)
#B = joint(3,0)
#C = joint(2,4)'

"""A = joint(0,0)
B = joint(4,0)
C = joint(4,4)
D = joint(0,4)

member1 = member(A,B)
member2 = member(D,C)
member3 = member(A,D)
member4 = member(B,C)
member5 = member(B,D)
member6 = member(A,C)

load1 = load(C, 50,"vertical")
load2 = load(D, 30, "Horizontal")

Support1 = support(A, "pin")
Support2 = support(B, "roller")

listOfJoints = [A,B,C,D]
listOfMemebers = [member1,member2,member3,member4,member5,member6]

for i in range(len(listOfJoints)):
    joint =listOfJoints[i]
    xj = joint.xcoord
    member = []
    for j in listOfMemebers:
        xs = j.startJoint.xcoord
        xe = j.endJoint.xcoord
        
        if xs == xj or xe == xj:
            member.append(j)"""


from numpy import sqrt 

class solver ():
    def __init__(self, joint1 , joint2):
        self.joint1 = joint1
        self.joint2 = joint2
    
    def length (self, ):
        x1 = self.joint1.xcoord
        x2 = self.joint2.xcoord
        
        y1 = self.joint1.ycoord
        y2 = self.joint2.ycoord
        
        self.L = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        L = self.L   
        self.L= L
        
        return L
   
    def direction_cosine (self, ):
        x1 = self.joint1.xcoord
        x2 = self.joint2.xcoord
        
        y1 = self.joint1.ycoord
        y2 = self.joint2.ycoord
        
        
        L = sqrt((x2 - x1)**2 + (y2 - y1)**2)
                 
        cose= ((x2 - x1)/L)
        sine = ((y2 - y1)/L)
        
        self.cose = cose
        self.sine = sine
        
        return cose, sine
#solve_truss = solver( , )
# =============================================================================
# 
# 
# =============================================================================
