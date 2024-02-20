using Plots, Interpolations

function ∇²(f, h)
    ∇²f = zero(f)
    for y ∈ 2:(size(f, 2) - 1), x ∈ 2:(size(f, 1) - 1)
        ∇²f[x, y] = (f[x-1, y] + f[x+1, y] + f[x, y-1] + f[x, y+1] - 4*f[x, y]) / (h^2)
    end
    f[begin, :] = f[(begin + 1), :]
    f[end, :] = f[(end - 1), :]
    f[:, begin] = f[:, (begin + 1)]
    f[:, end] = f[:, (end - 1)]
    return ∇²f
end

function step(X, Y, dt, h, p)
    a, b, τ, k = p
    X_next = X + dt*(a*∇²(X, h) + X - X.^3 - Y .+ k)
    Y_next = Y + (dt / τ)*(b*∇²(Y, h) + X - Y)
    return (X_next, Y_next)
end

function solve(p, grid_size, t, dt)
    h = 2.0 / grid_size
    n = floor(Int, t / dt)
    U = rand(Float64, (grid_size, grid_size))
    V = rand(Float64, (grid_size, grid_size))
    for i ∈ 1:n
        U, V = step(U, V, dt, h, p)
    end
    return (U, V)
end

function Interp2D(data, factor)
    
    IC = CubicSplineInterpolation((axes(data,1), axes(data,2)), data)

    finerx = LinRange(firstindex(data,1), lastindex(data,1), size(data,1) * factor)
    finery = LinRange(firstindex(data,2), lastindex(data,2), size(data,2) * factor)
    nx = length(finerx)
    ny = length(finery)

    data_interp = Array{Float64}(undef, nx, ny)
    for j ∈ 1:ny, i ∈ 1:nx
        data_interp[i,j] = IC(finerx[i],finery[j])
    end

    return finerx, finery, data_interp

end

par = [0.0005, 0.005, 0.1, 0.005]

@time heatmap(Interp2D(solve(par, 100, 40.0, 0.001)[1], 16), c=:leonardo)