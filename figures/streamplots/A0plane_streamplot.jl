using CairoMakie, DynamicalSystems

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
P6 = A0plane(-0.1, 0.8, 3.1, -5.0)  # pattern state
P7 = A0plane(2.7, 1.0, 1.3, -3.4)  # pattern state unstable spiral
P8 = A0plane(0.1, -1.0, 0.0, -1.0)  # pattern state unstable node

par = P4

f(x, P::A0plane) = Point2f(
    P.a*x[1] + P.b*x[2] - x[1]*x[2]^2,
    P.c*x[1] + P.d*x[2] + x[1]*x[2]^2
)

f(x) = f(x, par)

x_nullcline(x, y, P::A0plane) = P.a * x + P.b * y - x * y^2
y_nullcline(x, y, P::A0plane) = P.c * x + P.d * y + x * y^2

x_null(x, y) = x_nullcline(x, y, par)
y_null(x, y) = y_nullcline(x, y, par)

x = y = range(-3, 3; length=500)

fig = Figure(size = (600, 400))
ax = Axis(fig[1, 1], xlabel = "x", ylabel = "y")
streamplot!(ax, f, x, y; colormap = :grays, gridsize=(40, 40, 40))

zx = x_null.(x, y')

contour!(ax, x, y, zx, levels = [0], 
color = :red, linewidth = 1.5, label = "x-nullcline")

zy = y_null.(x, y')

contour!(ax, x, y, zy, levels = [0], 
color = :blue, linewidth = 1.5, label = "y-nullcline")

axislegend(ax, position = :rt)
fig

# fig, ax, pl = streamplot(f, -3..3, -3..3; 
# colormap=:grays, density=1.0, maxsteps=500, gridsize=(40, 40, 40))
# you can also pass a function to `color`, to either return a number or color value
# streamplot(fig[1,2], f, -1.5 .. 1.5, -1.5 .. 1.5, color=(p)-> RGBAf(p..., 0.0, 1))
# fig