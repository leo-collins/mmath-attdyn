using DynamicalSystems, GLMakie

function toymap(u, p, n)
    x = u[1]
    a, ϕ = p
    xn = sign(x)*a*cos(abs(x)+ϕ)
    return SVector(xn)
end


u0 = [0.5]
p0 = [1.5, 0.0]

toy = DeterministicIteratedMap(toymap, u0, p0)

rrange_phi = 0:0.001:(2*pi)
rrange_a = 1:0.001:3

# X, t = trajectory(toy, 100)

interactive_cobweb(toy, rrange, 1; pindex=2, xmin=-pi, xmax=pi)
