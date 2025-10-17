#Here is my project for Formula Slug Simulations
#I used matplotlib for plotting and animation, and dataclasses for state management
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass

@dataclass
class State:
    xpos: float
    vel: float
    time: float

delT = 0.05
acceleration_phase = 10.0
acceleration = 2.0
braking = -4.0
area_cd = 1.1
air_density = 1.225
mass = 1000.0


def step (state:State) -> State:
    drag = 0.5 * area_cd * air_density * state.vel**2 #calculates the drag force
    drag_accel = -drag / mass
    if state.time < acceleration_phase:
        a = acceleration + drag_accel   #this causes acceleration
    else:
        a = braking + drag_accel  #this causes braking

    new_vel = state.vel + a * delT
    if new_vel < 0:
        new_vel = 0 #this should stop the car when the velocity goes negative
    new_xpos = state.xpos + new_vel * delT
    new_time = state.time + delT

    return State(new_xpos, new_vel, new_time)

#animation function
def animate (i):
    global s0
    s0 = step(s0)
    ax.clear()
    ax.scatter(s0.xpos, 0, s=50, c='blue', label = 'Car')
    ax.set_xlim(0, 300)
    ax.set_ylim(-1, 1)
    ax.set_label(f"Time: {s0.time:.1f}s ; Velocity: {s0.vel:.2f}m/s")
    ax.legend()
    return ax

s0 = State(
    xpos = 0.0,
    vel = 0.0,
    time = 0.0
)

fig = plt.figure(figsize=(5,2), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(0, 300)
ax.set_ylim(-1, 1)

ani = animation.FuncAnimation(fig, animate, interval=0)
plt.show()