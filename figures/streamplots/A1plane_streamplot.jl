using CairoMakie

struct A1plane{T}
    a::T
    b::T
    c::T
    d::T
    D₁::T
    D₂::T
end

a = -2.24
b = -3.44
c = 2.97
d = 1.0
θ = 1.1

σₐ = (a * d - 2 * b * c - 2 * sqrt(b^2 * c^2 - a * b * c * d)) / a^2
σ = θ * σₐ

D₁ = (σ * a + d) / (4 * σ)
D₂ = σ * D₁

P = A1plane(a, b, c, d, D₁, D₂)

f(x, P::A1plane) = Point2f(
    P.a*x[1] + P.b*x[2] - x[1]*x[2]^2 - 2*P.D₁*x[1],
    P.c*x[1] + P.d*x[2] + x[1]*x[2]^2 - 2*P.D₂*x[2]
)

f(x) = f(x, P)

fig, ax, pl = streamplot(f, -3..3, -3..3; 
colormap=:grays, density=1.0, maxsteps=500, gridsize=(40, 40, 40))
# you can also pass a function to `color`, to either return a number or color value
# streamplot(fig[1,2], f, -1.5 .. 1.5, -1.5 .. 1.5, color=(p)-> RGBAf(p..., 0.0, 1))
# fig