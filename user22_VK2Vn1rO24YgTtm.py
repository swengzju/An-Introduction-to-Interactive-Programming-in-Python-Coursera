# template for "Stopwatch: The Game"

# define global variables
import simplegui

t = 0
x = 0
y = 0
running = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    subsec = t - int(t/10)*10
    minute = int(int(t/10)/60)
    sec = int(t/10) - minute*60
    if sec < 10:  
        return str(minute)+":0"+str(sec)+"."+str(subsec)
    else:
        return str(minute)+":"+str(sec)+"."+str(subsec)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    running = 0
    timer.start()
    
def stop():
    global x, y, running
    if running == 0 and t - int(t/10)*10 == 0:
        y += 1
        x += 1
        running = 1
    elif running == 0 and t - int(t/10)*10 != 0:
        y += 1
        running = 1
    else:
        running = 1
    timer.stop()

def reset():    
    global t, x, y
    t = 0
    x = 0
    y = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t = t + 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), (120, 180), 60, 'White')
    canvas.draw_text(str(x)+"/"+str(y), (300, 50), 40, 'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 400, 300)

# register event handlers
frame.add_button('Start', start, 150)
frame.add_button('Stop', stop, 150)
frame.add_button('Reset', reset, 150)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
# Please remember to review the grading rubric
