using DynamicalSystems, Plots, OrdinaryDiffEq
plotly()
# gr()

# diffeq = (alg = AutoTsit5(Rosenbrock23()), abstol = 1e-9, reltol = 1e-9)
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

par = [-1.1, -2.0, 1.0, 1.0, 1.0, 0.1, 0.431]
par2 = [-2.0, 3.0, -3.0, 1.0, 1.0, 0.1, 0.4]
u0 = [-1, 1, 0.01]
u1 = [-0.2289, 0.4036, 0.3486]

attdyn = CoupledODEs(opinion, u0, par; diffeq)
fp, eigs, stable = fixedpoints(attdyn, IntervalBox(-5..5, -5..5, 0..1))

X, t = trajectory(attdyn, 5000; Δt=0.1, Ttr=5000)

# attdyn1 = CoupledODEs(opinion, u1, par; diffeq)
# X1, t1 = trajectory(attdyn1, 5000; Δt=0.1, Ttr=0)



scene = plot(t, X[:, 1]; xlabel="t", ylabel="x", lw=2, legend=false, color=:black)
# plot!(scene, t, X1[:, 1], lw=2, color=:black)

# scene = plot(X[:, 1], X[:, 2], X[:, 3]; lw=3, legend=false, zlims=(0.0, 1.0), xlims=(-1,1), ylims=(-1,1),
# xlabel="x", ylabel="y", zlabel="A", linecolor=:black, camera=(20, 20))

# for i in range(length=length(fp))
#     if stable[i]
#         scatter!(scene, Tuple(fp[i]), markersize=3, markercolor=:green)
#     else
#         scatter!(scene, Tuple(fp[i]), markersize=3, markercolor=:red)
#     end
# end

# scene