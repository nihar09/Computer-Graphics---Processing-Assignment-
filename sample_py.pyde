def setup():
    global viewport;
    size(500,400,P3D);
    
def draw():
    rect(30,20,55,55,7)
    ellipse(46,36,11,11);
    ellipse(66,36,11,11);
    line(46,56,66,56);
    ellipse(58,112,77,77);
    triangle(58,112,26,136,26,145)
    ellipse(180,60,55,55);
    line(180,85,180,160);
    line(180,100,145,110);
    line(180,100,250,90);
    stroke(50);
