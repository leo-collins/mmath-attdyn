using Plots, DynamicalSystems

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

par = [-1.1, -2.0, 1.0, 1.0, 1.0, 0.1, 0.425]
par2 = [-2.0, 3.0, -3.0, 1.0, 1.0, 0.1, 0.4]
u0 = [-1, -1, 0.01]
u1 = [-1, 1, 0.01]

attdyn = CoupledODEs(opinion, u0, par; diffeq)

n = 100
pvalues = 0.424:0.00001:0.4364
pmap = PoincareMap(attdyn, (3, 0.33); direction=-1)
# Y, t = trajectory(pmap, 500; Ttr=10000)
# Plots.scatter(Y[:, 1], Y[:, 2])

output = orbitdiagram(pmap, 2, 7, pvalues; n, Ttr=500)

L = length(pvalues)
x = Vector{Float64}(undef, n*L)
y = copy(x)
for j in 1:L
    x[(1 + (j-1)*n):j*n] .= pvalues[j]
    y[(1 + (j-1)*n):j*n] .= output[j]
end

attdyn = CoupledODEs(opinion, u1, par; diffeq)
pmap = PoincareMap(attdyn, (3, 0.33); direction=-1)
output = orbitdiagram(pmap, 2, 7, pvalues; n, Ttr=500)

x1 = Vector{Float64}(undef, n*L)
y1 = copy(x1)
for j in 1:L
    x1[(1 + (j-1)*n):j*n] .= pvalues[j]
    y1[(1 + (j-1)*n):j*n] .= output[j]
end

scene = Plots.scatter(x, y; markersize=0.8, mc=:black, ma=1,
dpi=200, legend=false, xlabel="θ", ylabel="y", markerstrokewidth=0)
Plots.scatter!(scene, x1, y1; markersize=0.8, mc=:red, markerstrokewidth=0, ma=0.1)
# plot!([0.2776, 0.2776, 0.2785, 0.2785, 0.2776], [1.597, 1.631, 1.631, 1.597, 1.597], color="red", lw=2)
# Plots.ylims!(-4, -3)
