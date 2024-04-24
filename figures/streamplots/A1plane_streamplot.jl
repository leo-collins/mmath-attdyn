using CairoMakie, DynamicalSystems

function A1plane_ds(u, p, t)
    a, b, c, d, D₁, D₂ = p
    x, y = u

    du1 = a*x + b*y - x*y^2 - 2*D₁*x
    du2 = c*x + d*y + x*y^2 - 2*D₂*y

    return SVector(du1, du2)
end

struct A1plane{T}
    a::T
    b::T
    c::T
    d::T
    D₁::T
    D₂::T
end

a = -5.0
b = -3.4
c = 3.0
d = 1.2
θ = 1.5

σₐ = (a * d - 2 * b * c - 2 * sqrt(b^2 * c^2 - a * b * c * d)) / a^2
σ = θ * σₐ

D₁ = (σ * a + d) / (4 * σ)
D₂ = σ * D₁

par = A1plane(a, b, c, d, D₁, D₂)
par_ds = [par.a, par.b, par.c, par.d, par.D₁, par.D₂]
u0 = [-2.0, -2.0]

attdyn = CoupledODEs(A1plane_ds, u0, par_ds)
fp, eigs, stable = fixedpoints(attdyn, IntervalBox(interval(-5, 5), interval(-5, 5)))

f(x, P::A1plane) = Point2f(
    P.a*x[1] + P.b*x[2] - x[1]*x[2]^2 - 2*P.D₁*x[1],
    P.c*x[1] + P.d*x[2] + x[1]*x[2]^2 - 2*P.D₂*x[2]
)

f(x) = f(x, par)

x_nullcline(x, y, P::A1plane) = P.a * x + P.b * y - x * y^2 - 2*P.D₁*x
y_nullcline(x, y, P::A1plane) = P.c * x + P.d * y + x * y^2 - 2*P.D₂*y

x_null(x, y) = x_nullcline(x, y, par)
y_null(x, y) = y_nullcline(x, y, par)

x = range(-1, 1; length=500)
y = range(-2, 2; length=500)


fig = Figure(size = (600, 500))
ax = Axis(fig[1, 1], xlabel = "x", ylabel = "y")
streamplot!(ax, f, x, y; 
color=color_func(dx::Point) = 1, colormap=:berlin, density=1.0, 
maxsteps=500, gridsize=(40, 40, 40), )

zx = x_null.(x, y')

contour!(ax, x, y, zx, levels=[0],
color=:red, linewidth=2)

zy = y_null.(x, y')

contour!(ax, x, y, zy, levels=[0],
color=:blue, linewidth=2)

scatter!(ax, [0], [0]; color=:green, markersize=30)
# scatter!(ax, [-0.191139], [1.56634]; color=:green, markersize=30)
# scatter!(ax, [0.191139], [-1.56634]; color=:green, markersize=30)

save("plots/a1planestable.png", fig)
# fig
