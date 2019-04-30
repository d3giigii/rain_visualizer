class RainDrop:
    
    def __init__(self, x, y, fs, g, l):
        self.x_pos = x
        self.y_pos = y
        self.fall_speed = fs
        self.gravity = g
        self.length = l
        pass
    
    def show():
        stroke(255)
        line(self.x_pos, self.y_pos, self.x_pos, self.y_pos+self.length)
        pass
    
    def fall():
        self.y_pos += self.y_speed
        self.y_speed += self.gravity
        pass
    
    pass
    
