import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

main_branch = loadmat("data/patternstate/main_branch.mat")
negative_pattern_state_branch = loadmat("data/patternstate/negative_pattern_state_branch.mat")
positive_pattern_state_branch = loadmat("data/patternstate/positive_pattern_state_branch.mat")
negative_crit_homophily_branch = loadmat("data/patternstate/negative_crit_homophily_branch.mat")
positive_crit_homophily_branch = loadmat("data/patternstate/positive_crit_homophily_branch.mat")

main_branch_x_stable = main_branch["x"][0][:17]
main_branch_x_unstable = main_branch["x"][0][16:]
main_branch_theta_stable = main_branch["x"][3][:17]
main_branch_theta_unstable = main_branch["x"][3][16:]

negative_pattern_state_branch_x_stable = negative_pattern_state_branch["x"][0][:27]
negative_pattern_state_branch_x_unstable = negative_pattern_state_branch["x"][0][27:]
negative_pattern_state_branch_theta_stable = negative_pattern_state_branch["x"][3][:27]
negative_pattern_state_branch_theta_unstable = negative_pattern_state_branch["x"][3][27:]

positive_pattern_state_branch_x_stable = positive_pattern_state_branch["x"][0][:29]
positive_pattern_state_branch_x_unstable = positive_pattern_state_branch["x"][0][29:]
positive_pattern_state_branch_theta_stable = positive_pattern_state_branch["x"][3][:29]
positive_pattern_state_branch_theta_unstable = positive_pattern_state_branch["x"][3][29:]

negative_crit_homophily_branch_x = negative_crit_homophily_branch["x"][0]
negative_crit_homophily_branch_theta = negative_crit_homophily_branch["x"][3]

positive_crit_homophily_branch_x = positive_crit_homophily_branch["x"][0]
positive_crit_homophily_branch_theta = positive_crit_homophily_branch["x"][3]

fig, ax = plt.subplots()

ax.plot(
    main_branch_theta_stable,
    main_branch_x_stable,
    linestyle="solid",
    c="black",
)

ax.plot(
    main_branch_theta_unstable,
    main_branch_x_unstable,
    linestyle="dashed",
    c="black",
)

ax.plot(
    negative_pattern_state_branch_theta_stable,
    negative_pattern_state_branch_x_stable,
    linestyle="solid",
    c="blue",
)

ax.plot(
    negative_pattern_state_branch_theta_unstable,
    negative_pattern_state_branch_x_unstable,
    linestyle="dashed",
    c="blue",
)

ax.plot(
    positive_pattern_state_branch_theta_stable,
    positive_pattern_state_branch_x_stable,
    linestyle="solid",
    c="blue",
)

ax.plot(
    positive_pattern_state_branch_theta_unstable,
    positive_pattern_state_branch_x_unstable,
    linestyle="dashed",
    c="blue",
)

ax.plot(
    negative_crit_homophily_branch_theta,
    negative_crit_homophily_branch_x,
    linestyle="solid",
    c="red"
)

ax.plot(
    positive_crit_homophily_branch_theta,
    positive_crit_homophily_branch_x,
    linestyle="solid",
    c="red"
)

ax.scatter(
    [main_branch_theta_stable[-1]],
    [main_branch_x_stable[-1]],
    c="black",
    s=20,
    zorder=100
)

ax.scatter(
    [negative_pattern_state_branch_theta_stable[-1]],
    [negative_pattern_state_branch_x_stable[-1]],
    c="black",
    s=20,
    zorder=101
)

ax.scatter(
    [positive_pattern_state_branch_theta_stable[-1]],
    [positive_pattern_state_branch_x_stable[-1]],
    c="black",
    s=20,
    zorder=101
)


# ax.text(1.001, 0.005, "BP")
ax.set_ylim(-0.2, 0.2)
ax.set_xlim(0.9, 1.1)
ax.set_xlabel(r"$\theta$")
ax.set_ylabel(r"$x$")
plt.tight_layout()
plt.savefig("plots/pattern_bif.png", dpi=200)