import matplotlib.pyplot as plt
from scipy.io import loadmat

main_branch = loadmat("data/crit homophily from pattern/main_branch.mat")
bottom_branch = loadmat("data/crit homophily from pattern/bottom_branch.mat")
top_branch = loadmat("data/crit homophily from pattern/top_branch.mat")

main_branch_epsilon_stable = main_branch["x"][3][:20]
main_branch_A_stable = main_branch["x"][2][:20]
main_branch_epsilon_unstable = main_branch["x"][3][19:]
main_branch_A_unstable = main_branch["x"][2][19:]

bottom_branch_epsilon_unstable = bottom_branch["x"][3][:19]
bottom_branch_A_unstable = bottom_branch["x"][2][:19]
bottom_branch_epsilon_stable = bottom_branch["x"][3][19:]
bottom_branch_A_stable = bottom_branch["x"][2][19:]

top_branch_epsilon = top_branch["x"][3]
top_branch_A = top_branch["x"][2]

fig, ax = plt.subplots()

ax.plot(
    main_branch_epsilon_stable,
    main_branch_A_stable,
    linestyle="solid",
    c="black",
    zorder=1,
)

ax.plot(
    main_branch_epsilon_unstable,
    main_branch_A_unstable,
    linestyle="dashed",
    c="black",
    zorder=1,
)

ax.plot(
    bottom_branch_epsilon_stable,
    bottom_branch_A_stable,
    linestyle="solid",
    c="red",
    zorder=1,
)

ax.plot(
    bottom_branch_epsilon_unstable,
    bottom_branch_A_unstable,
    linestyle="dashed",
    c="red",
    zorder=1,
)

ax.plot(
    top_branch_epsilon,
    top_branch_A,
    linestyle="solid",
    c="red",
    zorder=1,
)

ax.scatter(
    [main_branch_epsilon_stable[-1]],
    [main_branch_A_stable[-1]],
    c="black",
    s=20,
    zorder=10,
)

ax.scatter(
    [bottom_branch_epsilon_unstable[-1]],
    [bottom_branch_A_unstable[-1]],
    c="black",
    s=20,
    zorder=10,
)

ax.text(0.17, 0.873, "SN")
ax.text(0.175, 1.01, "T")
ax.set_ylim(0.6, 1.1)
ax.set_xlim(0.0, 0.25)
ax.set_xlabel(r"$\varepsilon$")
ax.set_ylabel(r"$A$")
plt.tight_layout()
plt.savefig("plots/crit_hom_epsilon.png", dpi=200)
