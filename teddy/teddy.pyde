def setup():
    global viewport;
    size(600,500,P3D);
    
def draw():
    rect(250,60,87,87,40);
    fill(0,0,0);
    rect(305,85,10,10,10);
    fill(0,0,0);
    rect(275,85,10,10,10);
    fill(0,0,0);
    rect(292,105,7,7,5);
    fill(0,0,0);
    rect(280,125,30,5,10);
    fill(102,51,0);
    rect(230,55,27,27,13);
    rect(330,55,27,27,13);
    rect(230,148,130,180,80);
    rotate(PI/3);
    rect(252, -110, 35, 82, 90);
    rotate(PI/3);
    rect(-40, -486, 35, 82, 90);
    rotate(2*PI/3);
    rect(-400, -26, 35, 82, 90);
    rotate(PI/3);
    rect(-105, 455, 35, 82, 90);
    stroke(10);
