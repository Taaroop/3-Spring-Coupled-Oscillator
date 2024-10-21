# interesting coupled oscillator on rails
import math as m
import matplotlib.pyplot as plt

A_0 = 5
k_1 = 2
k_2 = 1
k_3 = 0.5
m_1 = 2
m_2 = 0.3
h = 1

time = 0
sim_time = 10
dt = 0.001 # tends to zero; the less, the smoother the sim

state = [A_0, A_0, 0, 0, None, None] # x_1, x_2, v_1, v_2, a_1, a_2

li_time = [0]
li_pos_1 = [A_0]
li_pos_2 = [A_0]

def new(state):
    l = m.sqrt(h**2 + (state[1] - state[0])**2)
    
    # acceleration
    state[4] = 1/m_1 * ((k_3 * (state[1] - state[0]) * (1 - h/l)) - k_1*state[0])
    state[5] = 1/m_2 * ((k_3 * (state[0] - state[1]) * (1 - h/l)) - k_2*state[1])
    
    # velocity (dv = a*dt)
    state[2] += state[4]*dt
    state[3] += state[5]*dt
    
    # position (dx = v*dt)
    state[0] += state[2]*dt
    state[1] += state[3]*dt
    
    return state
    
while time < sim_time:
    time += dt
    li_time.append(time)
    state = new(state)
    li_pos_1.append(state[0])
    li_pos_2.append(state[1])
    
plt.plot(li_time, li_pos_1)
plt.plot(li_time, li_pos_2)