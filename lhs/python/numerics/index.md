---
title: Numerical Integration in Python
...


Numerically Solving Differential Equations
==========================================

In many physics courses, we need to solve differential equations numerically.
Exact solutions are often impossible or very tedious to find. This guide, and
the accompanying `simulation.py` file, demonstrates how to build an integrator
from scratch. This guide is intended to show how to use Euler and Runge-Kutta
integrators for systems where we have an exact differential equation for
acceleration (or force, using $F = ma$).

Define the System
-----------------

We'll use a spring-mass system (quite common in physics) as our example here.
Later, you'll be asked to reproduce these steps for a probe falling to the
surface of a planet - a slightly more complicated system.

![Spring mass system](spring_mass.png)

First, we start with the exact descriptions of physical systems. This system can
be described with the following differential equation:

$\frac{d^2x}{dt^2} = a_s + a_d$

where $a_s$ is the acceleration due to the force from the spring, and $a_d$ is
the acceleration from a damping force. We know the force from the spring gives
us an acceleration like:

$a_s = \frac{-k * x}{m}$

where $k$ is the spring constant, $x$ is the position of the mass (relative to
the equilibrium position of the spring), and $m$ is the mass.

The acceleration due to damping is:

$a_d = \frac{-b * v}{m}$

where $b$ is the drag/damping coefficient, $v$ is the velocity of the mass, and
$m$ is the mass.

So we'll need a function, `sys_spring_mass`, that takes position, velocity, and
acceleration, and return the acceleration of the mass. The definition of this
function will look like this (fill in the rest):

```python
def sys_spring_mass (a, v, x):
    # calculate new acceleration here based on old values (`a`, `v`, `x`)
    return an   # `an` is the new acceleration
```

Discrete Integration
--------------------

Given the equations we've written down, we know the force on the system (and
thus the acceleration) as long as we know the position and velocity. To solve
this system approximately, we need to make time discrete - so instead of a
smooth position function, we will calculate position at each "step" in time. We
call the discretized blocks of time $dt$, where $dt$ can be something like 1
second, or 0.1 seconds, etc. Intuitively, the smaller our timestep, the closer
we get to the continuous solution.

So we can start our system with an arbitrary position, velocity, and
acceleration. To calculate the acceleration at the next timestep, we use our
equations we defined above. To calculate velocity, we can use the previous
acceleration, since acceleration is defined as the change in velocity over time:

$v_{t+1} = v_t + dv_t \quad [=m/s]$

$\frac{dv_t}{dt} = a_t \quad [=m/s^2]$

$dv_t = a_t * dt \quad [=m/s]$

$v_{t+1} = v_t + a_t * dt \quad [=m/s]$

And we can do a similar discretization for the next position:

$x_{t+1} = x_t + v_t * dt \quad [=m]$

This has a fancy name - the Euler integration method!

We'll need to write a python function, `euler`, which takes an acceleration
function, the current acceleration, velocity, position, and the size of our
`dt`, and returns the acceleration, velocity, and position at the next timestep.

This function will have this signature:

```python
def euler (f, a, v, x, dt):
    # some code here to calculate the next `a`, `v`, and `x`
    return an, vn, xn
```

where `f` is the acceleration function we define (system dependent, for our
spring mass system `f = sys_spring_mass` - defined above). `a`, `v`, and `x` are
the current acceleration, velocity, and position. `an`, `vn`, and `xn` are the
updated values that we calculate. We calculate these values using the
mathematical relations we've defined above.

Making this useful
------------------

So now we have an acceleration function, `sys_spring_mass`, and a function which
uses the previous timestep data to calculate `a`, `v`, and `x` at the next
timestep.

Next we need a function which can integrate this system over time, so we can
start with some initial conditions and watch the system evolve over time.
Fortunately, most of the heavy lifting is done for us - we've already defined a
function which can integrate one timestep - `euler` - and we've already defined
our system - `sys_spring_mass`. We now need to just apply our integrator to our
system many times to get the overall path of the object.

Our function definition will look like this:

```python
def gen_path (f, a0, v0, x0, dt, num, integrator):
    # Some code which calculates the path of the object
    return a, v, x
```

`a`, `v`, and `x` are now lists instead of individual numbers. The first item in
the `a` list, for example, corresponds to the initial acceleration, while the
second item in that list corresponds to the acceleration at the time `dt` in the
future, and the `n`th item corresponds to the acceleration at time `dt * n` in
the future.

We have to give our system initial conditions (starting position, velocity, and
acceleration), so we supply them with `a0`, `v0`, and `x0`. An example call to
this function would look like this:

```python
sm_a, sm_v, sm_x = gen_path (sys_spring_mass, 0, 0, 50, 0.1, 1000, euler)
```

This would specify that we want to find the path that a spring-mass system takes
when started with no acceleration or velocity, but pulled back 50 "units"
(meters). We will use the `euler` integrator, and integrate out to 1000
timesteps in the future using a timestep size of 0.1 "units" (seconds).

After we have this data, we can plot it, or save it to a file. Neither of those
are shown here, but the `simulation.py` file contains code to do both.


Improving our methods
=====================

Adaptive Integration
--------------------

We have thus far numerically integrated a differential equation by passing a
time step `dt` and number of points `num`. However, how do we know that our
answer has converged correctly? Think about Riemann integration, where we
approximate a curve with several rectangles- what if the rectangles are really
fat and don't estimate the curve well? We could fix this problem by making the
time step really really small, and the number of steps really really large, but
this kind of ad hoc implementation is not ideal.

To solve this issue, we introduce adaptive quadrature. In this method, we supply
a tolerance `tol`, and an end time `t_end`. We start the time step `dt` at 1, and
then halve `dt` each iteration. For each iteration, we call the `error`
the difference in `x` by using `dt` and `dt/2` as our time steps. If the error
is larger than the tolerance, we halve the time step again (so that we use
`dt/4`). Eventually, with a fine enough time step, the error in `x` will become
very small. As a small caveat, as we decrease the time step, we need more time
steps to simulate to the same point; accordingly, we set `num`=`t_end/dt`.

With this method, we can be confident that our numerical result has converged
within some tolerance (if this were not the case, we would never be sure that
any of our results are correct!). Since we now have a guaranteed tolerance, the
solvers that we use will all be equivalent in terms of accuracy. However, some
solvers will converge to within tolerance in fewer iterations than others, which
corresponds to a quicker solver.
