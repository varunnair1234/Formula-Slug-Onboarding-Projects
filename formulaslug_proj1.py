import matplotlib.pyplot as plt # type: ignore
import matplotlib.animation as animation # type: ignore
from dataclasses import dataclass
import numpy as np # type: ignore

@dataclass
class State:
    xpos: float
    ypos: float
    xvel: float
    yvel: float

delT = 0.1
bounceCoeff = 0.9
radius = 0.1 

def step(state: State) -> State:
    new_xpos = state.xpos + state.xvel * delT
    new_ypos = state.ypos + state.yvel * delT
    new_yvel = state.yvel - 9.81 * delT
    new_xvel = state.xvel

    if new_ypos < 0:
        new_yvel = new_yvel * -1 * bounceCoeff
        new_ypos = 0

    if new_ypos > 1000:
        new_yvel = new_yvel * bounceCoeff
        new_ypos = 1000
    
    if new_xpos < -4:
        new_xvel = new_xvel * -1 * bounceCoeff
        new_xpos = -4

    if new_xpos > 4:
        new_xvel = new_xvel * -1 * bounceCoeff
        new_xpos = 4

    sNew = State(
        xpos = new_xpos,
        ypos = new_ypos,
        xvel = new_xvel,
        yvel = new_yvel
    )
    return sNew

def animate (i):
    global s0, s1
    s0 = step (s0)
    s1 = step (s1)
    ax.clear()
    ax.scatter([s0.xpos], [s0.ypos], s = 200, c='blue', label='Ball 1')
    ax.scatter([s1.xpos], [s1.ypos], s = 200, c='red', label='Ball 2')
    ax.set_xlim(-4,4)
    ax.set_ylim(0, 10.5)
    return ax,

s0 = State(
    xpos = -1,
    ypos = 10,
    xvel = 0.1,
    yvel = 0
)

s1 = State(
    xpos = 1,
    ypos = 10,
    xvel = 0.2,
    yvel = 0
)


fig = plt.figure(figsize=(3,3), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(-4,4)
ax.set_ylim(0, 10.5)
plt.pause(5)
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show() 