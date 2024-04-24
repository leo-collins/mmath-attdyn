using CairoMakie, DynamicalSystems

function A0plane_ds(u, p, t)
    a, b, c, d = p
    x, y = u

    du1 = a*x + b*y - x*y^2
    du2 = c*x + d*y + x*y^2

    return SVector(du1, du2)
end

struct A0plane{T}
    a::T
    b::T
    c::T
    d::T
end

P1 = A0plane(-2.0, 3.0, -3.0, 1.0)  # stable spiral
P2 = A0plane(-3.0, 1.0, 1.0, -3.0)  # stable node
P3 = A0plane(1.0, -3.0, 1.0, -0.9)  # unstable spiral w/ limit cycle
P4 = A0plane(3.0, 1.0, 2.0, 1.0)  # unstable node

P5 = A0plane(2.7, 1.0, 1.3, -3.0)  # pattern state stable spiral
P6 = A0plane(-0.1, 0.8, 3.1, -5.0)  # pattern state stable node
P7 = A0plane(2.7, 1.0, 1.3, -3.4)  # pattern state unstable spiral
P8 = A0plane(0.1, -1.0, 0.0, -1.0)  # pattern state unstable node

par = P8

par_ds = [par.a, par.b, par.c, par.d]
u0 = [-2.0, -2.0]

attdyn = CoupledODEs(A0plane_ds, u0, par_ds)
# X, t = trajectory(attdyn, 1000; Δt=0.01, Ttr=950)
fp, eigs, stable = fixedpoints(attdyn, IntervalBox(interval(-5, 5), interval(-5, 5)))

f(x, P::A0plane) = Point2f(
    P.a*x[1] + P.b*x[2] - x[1]*x[2]^2,
    P.c*x[1] + P.d*x[2] + x[1]*x[2]^2
)

f(x) = f(x, par)

x_nullcline(x, y, P::A0plane) = P.a * x + P.b * y - x * y^2
y_nullcline(x, y, P::A0plane) = P.c * x + P.d * y + x * y^2

x_null(x, y) = x_nullcline(x, y, par)
y_null(x, y) = y_nullcline(x, y, par)

x = y = range(-5, 5; length=500)

fig = Figure(size = (600, 400))
ax = Axis(fig[1, 1], xlabel = "x", ylabel = "y")
streamplot!(ax, f, x, y; color=color_func(dx::Point) = 1, colormap = :berlin, gridsize=(40, 40, 40))

zx = x_null.(x, y')

contour!(ax, x, y, zx, levels = [0], 
color = :red, linewidth = 2, label = "x-nullcline")

zy = y_null.(x, y')

contour!(ax, x, y, zy, levels = [0], 
color = :blue, linewidth = 2, label = "y-nullcline")

# lines!(ax, X[:, 1], X[:, 2]; color=:purple3, linewidth=5)
scatter!(ax, [0], [0]; color=:red, markersize=30)
scatter!(ax, [-4.47214], [-0.223607]; color=:red, markersize=30)
scatter!(ax, [4.47214], [0.223607]; color=:red, markersize=30)

# axislegend(ax, position = :rt)
fig
