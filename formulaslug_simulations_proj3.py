import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass

@dataclass
class State:
    rpm: float
    torque: float
    time: float

delT = 0.05
max_rpm = 6000
torque_0 = 200
load = 5
acceleration_rate = 200
inertia = 10

def step (state:State) -> State:
    torque = torque_0 * (1 - state.rpm/max_rpm)
    if torque < 0:
        torque = 0
    
    net_torque = torque - load
    rpm_change = (net_torque / inertia) * delT * 100
    new_rpm = state.rpm + rpm_change
    if new_rpm > max_rpm:
        new_rpm = max_rpm
    
    new_time = state.time + delT
    new_torque = torque
    return State

def animate (i):
    global s0
    s0 = step(s0)

    power = s0.torque * s0.rpm / 9000

    ax.clear()
    ax.scatter([s0.rpm], [s0.torque], s = 200, c = 'orange', label = "motor")
    ax.set_xlim(0, max_rpm)
    ax.set_ylim(0, torque_0 * 1.1)
    ax.set_xlabel("RPM")
    ax.set_ylabel("Torque")
    ax.set_title(f"t = {s0.time:.1f}s ; Power = {power:.2f} W")
    ax.legend()
    return ax

s0 = State(rpm = 0, torque = torque_0, time = 0)

fig = plt.figure(figsize=(3,3), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(0, max_rpm)
ax.set_ylim(0, torque_0 * 1.1)

ani = animation.FuncAnimation(fig, animate, interval=0)
plt.show()