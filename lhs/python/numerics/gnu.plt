set terminal postscript eps size 5,3 enhanced color \
    font 'Helvetica,24' linewidth 2

set title "Spring Mass - Euler Symplectic Solver - dt = 0.1"
set output "plt.eps"
set xlabel "t (s)"
set ylabel "a (ms^{-2}), v (m s^{-1}), x (m)"
set key right top
set size 1.7,1.7
plot "sys_spring_mass_symplectic_euler_dt=0.1.dat" \
            using 1:2 with lines lt 1 lc rgb "red" title "Acceleration", \
     "sys_spring_mass_symplectic_euler_dt=0.1.dat" \
            using 1:3 with lines lt 1 lc rgb "green" title "Velocity", \
     "sys_spring_mass_symplectic_euler_dt=0.1.dat" \
            using 1:4 with lines lt 1 lc rgb "blue" title "Position" \
