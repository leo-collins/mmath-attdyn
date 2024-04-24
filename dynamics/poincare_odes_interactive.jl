using GLMakie, DynamicalSystems

diffeq = (alg = AutoVern9(Rodas5P()), abstol = 1e-12, reltol = 1e-12)

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

par = [-1.1, -2.0, 1.0, 1.0, 1.0, 0.1, 0.45]
par2 = [-2.0, 3.0, -3.0, 1.0, 1.0, 0.1, 0.4]
u0 = [-1, -1, 0.01]
u1 = [-0.2289, 0.4036, 0.3486]

attdyn = CoupledODEs(opinion, u0, par; diffeq)

X, t = trajectory(attdyn, 500.0; Ttr=10000.0, Δt=0.01)

interactive_poincaresos_scan(X, 3; direction=-1)