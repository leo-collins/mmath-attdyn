using ChaosTools, Plots, DynamicalSystems, OrdinaryDiffEq, DataFrames, CSV

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

par = [-1.1, -2.0, 1.0, 1.0, 1.0, 0.1, 0.429]
par2 = [-2.0, 3.0, -3.0, 1.0, 1.0, 0.1, 0.4]
u0 = [0.5, -0.5, 0.3]

attdyn = CoupledODEs(opinion, u0, par; diffeq)

systems = [deepcopy(attdyn) for _ in 1:Threads.nthreads()-1]
pushfirst!(systems, attdyn)

θs = 0.1:0.0001:0.5
λs = zeros(length(θs), 3)

Threads.@threads for i in eachindex(θs)
    system = systems[Threads.threadid()]
    set_parameter!(system, 7, θs[i])

    λs[i, :] .= lyapunovspectrum(system, 100000; Δt=0.01, Ttr=10000)
end

scene = plot(θs, λs[:, 1], label="λ₁", xlabel="θ", ylabel="λ", dpi=200, lw=2)
plot!(scene, θs, λs[:, 2], label="λ₂", lw=2)
plot!(scene, θs, λs[:, 3], label="λ₃", lw=2)

data = DataFrame(λs, :auto)
data[:, :θs] = θs
CSV.write("lyapunov/lyapunov_full2.csv", data)
scene