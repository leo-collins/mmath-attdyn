using DynamicalSystems, Plots
plotly()

function opinion(u, p, t)
    a, b, c, d, α, ϵ, θ = p
    x, y, A = u

    σₐ = (a * d - 2 * b * c - 2 * sqrt(b^2 * c^2 - a * b * c * d)) / (a^2)
    σ = θ * σₐ

    D₁ = (σ * a + d) / (4 * σ)
    D₂ = σ * D₁

    du1 = a*x + b*y - x*y^2 - 2*D₁*A*x
    du2 = c*x + d*y + x*y^2 - 2*D₂*A*y
    du3 = α*A*(1-A)*(ϵ-x)*(ϵ+x)

    return SVector(du1, du2, du3)
end

par = [-1.1, -2.0, 1.0, 1.0, 1.0, 0.1, 0.4]
u0 = [0.0001, 0.0001, 0.9999]

attdyn = CoupledODEs(opinion, u0, par)
fp, eigs, stable = fixedpoints(attdyn, IntervalBox(-5..5, -5..5, 0..1))

X, t = trajectory(attdyn, 10000; Δt=0.1)

scene = plot(X[:, 1], X[:, 2], X[:, 3]; 
size=(960, 720), lw=3, legend=false, zlims=(0.0, 1.0), 
xlabel="x", ylabel="y", zlabel="A", linecolor=:black)

a, b, c, d, α, ϵ, θ = par
σₐ = (a * d - 2 * b * c - 2 * sqrt(b^2 * c^2 - a * b * c * d)) / (a^2)
σ = θ * σₐ

D₁ = (σ * a + d) / (4 * σ)
D₂ = σ * D₁
mat001 = [a-2*D₁ b 0; c d-2*D₂ 0; 0 0 -α*ϵ^2]

x_eig = 0.5*(-sqrt(a^2 - 2*a*d - 4*a*D₁ + 4*a*D₂ + 4*b*c + d^2 + 4*d*D₁ - 4*d*D₂ + 4*D₁^2 - 8*D₁*D₂ + 4*D₂^2)+a+d-2*D₁-2D₂)
y_eig = 0.5*(sqrt(a^2 - 2*a*d - 4*a*D₁ + 4*a*D₂ + 4*b*c + d^2 + 4*d*D₁ - 4*d*D₂ + 4*D₁^2 - 8*D₁*D₂ + 4*D₂^2)+a+d-2*D₁-2D₂)
println("x: $x_eig, y: $y_eig")