using DynamicalSystems, Plots

function toymap2d(u, p, n)
    x, y = u
    a, b, ϕ, θ = p
    xn = sign(x)*a*cos(abs(x)+ϕ)
    yn = sign(y)*b*cos(abs(x)+θ)
    return SVector(xn, yn)
end

u0 = [0.3, 0.3]
p = [4.1, 1.3, 2, 0.5]

toy2d = DeterministicIteratedMap(toymap2d, u0, p)

X, t = trajectory(toy2d, 10000)

scatter(X[:, 1], X[:, 2])