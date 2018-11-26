"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Derrick Swart.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
jack = rg.SimpleTurtle('turtle')
john = rg.SimpleTurtle('square')
bob = rg.SimpleTurtle('arrow')
jack.pen = rg.Pen('red' , 1)
john.pen = rg.Pen('midnight blue',1)
bob.pen = rg.Pen('black' , 1)
jack.speed = 10
john.speed = 10
bob.speed = 10
window.tracer(2)
for k in range(200):
    jack.draw_regular_polygon(3, k)
    jack.forward(50)
    jack.left(60)
john.go_to(rg.Point(0, 0))
for k in range (100):

    john.forward(100)
    john.draw_circle(k)
    john.left(90)
for k in range (400):
    bob.forward(k)
    bob.right(95)



window.close_on_mouse_click()
