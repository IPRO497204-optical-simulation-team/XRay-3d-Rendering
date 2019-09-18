import pi3d
DISPLAY = pi3d.Display.create()
ball = pi3d.Sphere(z=5.0)
while DISPLAY.loop_running():
  ball.draw()

