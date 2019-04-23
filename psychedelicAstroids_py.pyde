class Astroid:
    def __init__(self, x, y, r, col):
        self.x = x-width/2
        self.y = y-height/2
        self.r = r
        self.rotation = 0
        self.col = col
        
    def display(self):
        step = PI/100
        fill(0,self.col,0)
        noStroke()
        #stroke(255, 0, 0)
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.rotation)
        beginShape()
        for i in range(200):
            x = self.r * cos(i*step)**3
            y = self.r * sin(i*step)**3
            vertex(x, y)
        endShape()
        popMatrix()


def bkg():
    fill(255)
    beginShape()
    vertex(0, -465)
    vertex(465, 0)
    vertex(0, 465)
    vertex(-465, 0)
    endShape(CLOSE)
                
        
l = []
def setup():
    global l
    size(900, 900)
    r = 50
    step = r*2
    start = width / 2
    stop = width / 2
    for y in range(r, height, r):
        if y <= height/2:
            stop += r
        else:
            stop -= r
            
        for x in range(start, stop, step):
            l.append(Astroid(x, y, r, (x+y)%255+50))
            
        if y < height/2:
            start -= r
        else:
            start += r


        
        
rot = 0
def draw():
    global rot
    background(40)
        
    pushMatrix()
    translate(450,450)
    rotate(rot)
    bkg()
    
    for i in range(len(l)):
        l[i].display()
        l[i].rotation -= PI/100
        
    popMatrix()    
    rot += PI/200
    #noLoop()
    #saveFrame('output/trip_####.png')
