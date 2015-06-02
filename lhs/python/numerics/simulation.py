#!/usr/bin/python3


# Needed modules
# ==============
import matplotlib.pyplot as plt
import sys
import math


# Spring-mass definition
# ======================

# Spring constants
# ----------------
spring_k = 0.4  # kg s^-2
spring_b = 0.0  # kg m s^-1
spring_m = 2    # kg

# Differential equation
# ---------------------
def acc_spring_mass (a, v, x, k = spring_k, b = spring_b, m = spring_m):
    return (- k*x - b*v)/m


# Probe falling definition
# ========================

# Probe constants
# ---------------
G            = 6.673e-11    # m^3 kg^-1 s^-2
earth_mass   = 5.972e24     # kg
earth_radius = 6.371e6      # m
probe_mass   = 2.3e3        # kg
probe_area   = 2            # m^2

# Differential equation
# ---------------------
def acc_probe (a, v, h,
            m2 = probe_mass, m1 = earth_mass, r = earth_radius,
            p0 = 1.0, h0 = 7000.0, area = probe_area):
    b_atmo = area * p0 * math.exp (- h / h0)        # `b` varies with `h`
    acc_air = b_atmo * (v*v) / m2                   # Atmospheric drag
    acc_grav = - (G * m1) / ((r+h) * (r+h))         # Gravity
    return acc_grav + acc_air


# Single step integrators
# =======================

# Euler
# -----
def euler (f, a, v, x, dt):
    an = f (a, v, x)
    vn = v + a*dt
    xn = x + v*dt
    return an, vn, xn

# Symplectic Euler
# ----------------
def symplectic_euler (f, a, v, x, dt):
    an = f (a, v, x)
    vn = v + an*dt
    xn = x + vn*dt
    return an, vn, xn

# Runge-Kutta 4th Order (RK4)
# ---------------------------
def rk4 (f, a, v, x, dt):
    x1 = x
    v1 = v
    a1 = f (a, v1, x1)

    x2 = x + 0.5*v1*dt
    v2 = v + 0.5*a1*dt
    a2 = f (a, v2, x2)

    x3 = x + 0.5*v2*dt
    v3 = v + 0.5*a2*dt
    a3 = f (a, v3, x3)

    x4 = x + v3*dt
    v4 = v + a3*dt
    a4 = f (a, v4, x4)

    xn = x + (dt/6)*(v1 + 2*v2 + 2*v3 + v4)
    vn = v + (dt/6)*(a1 + 2*a2 + 2*a3 + a4)
    an = (1/6)*(a1 + 2*a2 + 2*a3 + a4)

    return an, vn, xn


# Path generators
# ===============

# Fixed time-step
# ---------------
def gen_path (f, a0, v0, x0, dt, tf, integrator):
    num = int(tf / dt)
    a = [a0] * num
    v = [v0] * num
    x = [x0] * num
    for i in range(1, num):
        a[i], v[i], x[i] = integrator (f, a[i-1], v[i-1], x[i-1], dt)
    return a, v, x

# Converge with adaptive time-step
# --------------------------------
def converge_gen_path (f, a0, v0, x0, dt, tf, integrator, x_tol):
    a1, v1, x1 = gen_path(f, a0, v0, x0, dt,   tf, integrator)
    a2, v2, x2 = gen_path(f, a0, v0, x0, dt/2, tf, integrator)

    squared_x_error = [(p1-p2)*(p1-p2) for p1,p2 in zip(x1, x2[::2])]
    avg_rms_x_error = math.sqrt (sum (squared_x_error) / len(x1))
    if avg_rms_x_error > x_tol:
        return converge_gen_path (f, a0, v0, x0, dt/4, tf, integrator, x_tol)

    return a1, v1, x1, dt   # This data is 'good enough', and half the size!


# Outputs
# =======

# Write out data for gnuplot
# --------------------------
# format: time acceleration velocity position
def write_data (name, dt, a, v, x):
    f_name = "dat/" + name + ".dat"
    with open(f_name, "w") as fo:
        fo.write ("# time \t\tacc   \t\tvel   \t\tpos\n")
        # One timestep per line (tab separated for gnuplot)
        for i,(ai,vi,xi) in enumerate(zip(a, v, x)):
            fo.write ("{0:.5f}\t\t".format(i*dt))
            fo.write ("{0:.5f}\t\t".format(ai))
            fo.write ("{0:.5f}\t\t".format(vi))
            fo.write ("{0:.5f}\n".format(xi))
        print ("-   data: {}".format(f_name))

# Plot a path
# -----------
# requires matplotlib
def plot_path (name, dt, a = None, v = None, x = None):
    fig = plt.axes()
    for path, label in zip([a, v, x], ["acc", "vel", "pos"]):
        if path is not None:
            ts = [dt*i for i in range(len(path))]
            fig.plot(ts, path, label = label)
    fig.legend()
    fig.set_title (name)
    f_name = "plot/" + name + ".pdf"
    plt.savefig (f_name)
    print ("-   plot: {}".format(f_name))
    fig.cla()


# Running the program
# ===================

# Single simulation
# -----------------
def run_sim (f, a0, v0, x0, dt, tf, integrator, x_tol,
                write = True, plot = False):
    print ()
    print ("Running simulation")
    print ("==================")
    print ("-   system: {}".format(f.__name__))
    print ("-   integrator: {}".format(integrator.__name__))
    print ("-   start dt: {}".format(dt))

    a, v, x, dt_f = converge_gen_path (f, a0, v0, x0, dt, tf, integrator, x_tol)
    print ("-   converged dt: {}".format(dt_f))

    name = "{}_{}_dt={:.5f}".format(f.__name__, integrator.__name__, dt_f)
    if write:
        write_data (name, dt_f, a, v, x)
    if plot:
        plot_path (name, dt_f, a, v, x)

# Called from terminal
# --------------------
if __name__ == "__main__":

    ### Command-line arguments
    dt    = float(sys.argv[1]) if len(sys.argv) > 1 else 10.0
    x0    = float(sys.argv[2]) if len(sys.argv) > 2 else 20000.0
    v0    = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
    a0    = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
    tf    = float(sys.argv[5]) if len(sys.argv) > 5 else 150.0
    x_tol = float(sys.argv[5]) if len(sys.argv) > 5 else 150.0

    ### Default simulations
    # [ (system, integrator) ]
    default_simulations = [ (acc_spring_mass, euler) \
                          , (acc_spring_mass, symplectic_euler) \
                          , (acc_spring_mass, rk4) \
                          , (acc_probe, euler) \
                          , (acc_probe, symplectic_euler) \
                          , (acc_probe, rk4) \
                          ]

    ### Run the simulations
    for system, integrator in default_simulations:
        run_sim (system, a0, v0, x0, dt, tf, integrator, x_tol)
