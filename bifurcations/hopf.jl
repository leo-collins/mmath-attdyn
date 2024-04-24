using BifurcationKit, Parameters, Plots
const BK = BifurcationKit

function attdyn(u, p)
    @unpack a, b, c, d, α, ϵ, θ = p
    x, y, A = u

    σₐ = (a * d - 2 * b * c - 2 * sqrt(b^2 * c^2 - a * b * c * d)) / (a^2)
    σ = θ * σₐ

    D₁ = (σ * a + d) / (4 * σ)
    D₂ = σ * D₁

    [
        a*x + b*y - x*y^2 - 2*D₁*A*x,
        c*x + d*y + x*y^2 - 2*D₂*A*y,
        α*A*(1-A)*(ϵ-x)*(ϵ+x)
    ]
end

par = (a=-1.1, b=-2.0, c=1.0, d=1.0, α=1.0, ϵ=0.1, θ=0.7)
u0 = [0.1, -0.139543, 0.654976]

prob = BifurcationProblem(attdyn!, u0, par, (@lens _.θ);
record_from_solution = (x, p) -> (x = x[1], y = x[2], A=x[3]),)

opts_br = ContinuationPar(p_min=0.2, p_max=0.7, ds=0.04, dsmax=0.05,)

br = continuation(prob, PALC(), opts_br, bothside=true)

scene = plot(br, vars=(:param, :A))