using Plots, LaTeXStrings

function stability(x)
    a, b, c, d = [-5.0, -3.4, 3, 1.2]
    σ = 0.054
    # D₁ = 10
    D₁ = (σ*a + d) / (4*σ)
    D₂ = D₁ * σ
    return 4*D₁*D₂*x^2 - 2*(a*D₂ + d*D₁)*x + a*d - b*c
end

function x_axis(y)
    return 0
end

x = range(0.4, 1.6; length=100)
y = stability.(x)
x_ax = x_axis.(x)

scene = plot(x, y; 
ylims=((-0.4, 0.6)), lw=2, c=:red, legend=false, 
xlabel=L"$A$", ylabel=L"$\Delta$", dpi=200)
plot!(scene, x, x_ax; lw=2, c=:black)
savefig("plots/stability_curve4.png")
