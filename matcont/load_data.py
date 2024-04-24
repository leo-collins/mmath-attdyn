import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

main_hopf_branch = loadmat("data/main_hopf_branch.mat")
main_PO_branch = loadmat("data/main_PO_branch.mat")
PO1_branch1 = loadmat("data/periodicorbit1/PO1_branch1.mat")
PO1_branch2 = loadmat("data/periodicorbit1/PO1_branch2.mat")
PO2_branch1 = loadmat("data/periodicorbit2/PO2_branch1.mat")
PO2_branch2 = loadmat("data/periodicorbit2/PO2_branch2.mat")
PO3_branch1 = loadmat("data/periodicorbit3/PO3_branch1.mat")
PO3_branch2 = loadmat("data/periodicorbit3/PO3_branch2.mat")
PO4_branch1 = loadmat("data/periodicorbit4/PO4_branch1.mat")
PO4_branch2 = loadmat("data/periodicorbit4/PO4_branch2.mat")
PO5_branch1 = loadmat("data/periodicorbit5/PO5_branch1.mat")
PO5_branch2 = loadmat("data/periodicorbit5/PO5_branch2.mat")
PO6_branch1 = loadmat("data/periodicorbit6/PO6_branch1.mat")
PO6_branch2 = loadmat("data/periodicorbit6/PO6_branch2.mat")
PO2_PD1 = loadmat("data/periodicorbit2/PO2_PD1.mat")
PO2_PD2 = loadmat("data/periodicorbit2/PO2_PD2.mat")
PO2_PD3 = loadmat("data/periodicorbit2/PO2_PD3.mat")

main_hopf_branch_A_stable = main_hopf_branch["x"][2][:24]
main_hopf_branch_A_unstable = main_hopf_branch["x"][2][24:]
main_hopf_branch_theta_stable = main_hopf_branch["x"][3][:24]
main_hopf_branch_theta_unstable = main_hopf_branch["x"][3][24:]

main_PO_branch_max_A_stable = np.max(main_PO_branch["x"][2:-1:3], axis=0)[:235]
main_PO_branch_max_A_unstable = np.max(main_PO_branch["x"][2:-1:3], axis=0)[235:]
main_PO_branch_theta_stable = main_PO_branch["x"][-1][:235]
main_PO_branch_theta_unstable = main_PO_branch["x"][-1][235:]

PO1_branch1_max_A_stable = np.max(PO1_branch1["x"][2:-1:3], axis=0)[:49]
PO1_branch1_max_A_unstable = np.max(PO1_branch1["x"][2:-1:3], axis=0)[49:]
PO1_branch1_theta_stable = PO1_branch1["x"][-1][:49]
PO1_branch1_theta_unstable = PO1_branch1["x"][-1][49:]

PO1_branch2_max_A_stable = np.max(PO1_branch2["x"][2:-1:3], axis=0)[:14]
PO1_branch2_max_A_unstable = np.max(PO1_branch2["x"][2:-1:3], axis=0)[14:]
PO1_branch2_theta_stable = PO1_branch2["x"][-1][:14]
PO1_branch2_theta_unstable = PO1_branch2["x"][-1][14:]

PO2_branch1_max_A_stable = np.max(PO2_branch1["x"][2:-1:3], axis=0)[:34]
PO2_branch1_max_A_unstable = np.max(PO2_branch1["x"][2:-1:3], axis=0)[34:]
PO2_branch1_theta_stable = PO2_branch1["x"][-1][:34]
PO2_branch1_theta_unstable = PO2_branch1["x"][-1][34:]

PO2_branch2_max_A_stable = np.max(PO2_branch2["x"][2:-1:3], axis=0)[:13]
PO2_branch2_max_A_unstable = np.max(PO2_branch2["x"][2:-1:3], axis=0)[12:]
PO2_branch2_theta_stable = PO2_branch2["x"][-1][:13]
PO2_branch2_theta_unstable = PO2_branch2["x"][-1][12:]

PO3_branch1_max_A_stable = np.max(PO3_branch1["x"][2:-1:3], axis=0)[:18]
PO3_branch1_max_A_unstable = np.max(PO3_branch1["x"][2:-1:3], axis=0)[18:]
PO3_branch1_theta_stable = PO3_branch1["x"][-1][:18]
PO3_branch1_theta_unstable = PO3_branch1["x"][-1][18:]

PO3_branch2_max_A_stable = np.max(PO3_branch2["x"][2:-1:3], axis=0)[:55]
PO3_branch2_max_A_unstable = np.max(PO3_branch2["x"][2:-1:3], axis=0)[55:]
PO3_branch2_theta_stable = PO3_branch2["x"][-1][:55]
PO3_branch2_theta_unstable = PO3_branch2["x"][-1][55:]

PO4_branch1_max_A_unstable = np.max(PO4_branch1["x"][2:-1:3], axis=0)[:216]
PO4_branch1_theta_unstable = PO4_branch1["x"][-1][:216]

PO4_branch1_max_A_stable = np.max(PO4_branch1["x"][2:-1:3], axis=0)[216:304]
PO4_branch1_theta_stable = PO4_branch1["x"][-1][216:304]

PO4_branch1_max_A_unstable2 = np.max(PO4_branch1["x"][2:-1:3], axis=0)[304:]
PO4_branch1_theta_unstable2 = PO4_branch1["x"][-1][304:]

PO4_branch2_max_A_unstable = np.max(PO4_branch2["x"][2:-1:3], axis=0)
PO4_branch2_theta_unstable = PO4_branch2["x"][-1]

PO5_branch1_max_A_unstable = np.max(PO5_branch1["x"][2:-1:3], axis=0)[:37]
PO5_branch1_theta_unstable = PO5_branch1["x"][-1][:37]

PO5_branch1_max_A_stable = np.max(PO5_branch1["x"][2:-1:3], axis=0)[37:73]
PO5_branch1_theta_stable = PO5_branch1["x"][-1][37:73]

PO5_branch1_max_A_unstable2 = np.max(PO5_branch1["x"][2:-1:3], axis=0)[73:]
PO5_branch1_theta_unstable2 = PO5_branch1["x"][-1][73:]

PO5_branch2_max_A_unstable = np.max(PO6_branch2["x"][2:-1:3], axis=0)
PO5_branch2_theta_unstable = PO6_branch2["x"][-1]

PO6_branch1_max_A_unstable = np.max(PO6_branch1["x"][2:-1:3], axis=0)[:10]
PO6_branch1_theta_unstable = PO6_branch1["x"][-1][:10]

PO6_branch1_max_A_stable = np.max(PO6_branch1["x"][2:-1:3], axis=0)[10:35]
PO6_branch1_theta_stable = PO6_branch1["x"][-1][10:35]

PO6_branch1_max_A_unstable2 = np.max(PO6_branch1["x"][2:-1:3], axis=0)[35:]
PO6_branch1_theta_unstable2 = PO6_branch1["x"][-1][35:]

PO6_branch2_max_A_unstable = np.max(PO6_branch2["x"][2:-1:3], axis=0)
PO6_branch2_theta_unstable = PO6_branch2["x"][-1]

PO2_PD1_max_A_stable = np.max(PO2_PD1["x"][2:-1:3], axis=0)[:86]
PO2_PD1_theta_stable = PO2_PD1["x"][-1][:86]
PO2_PD1_max_A_unstable = np.max(PO2_PD1["x"][2:-1:3], axis=0)[85:]
PO2_PD1_theta_unstable = PO2_PD1["x"][-1][85:]

PO2_PD2_max_A_stable = np.max(PO2_PD2["x"][2:-1:3], axis=0)[:19]
PO2_PD2_theta_stable = PO2_PD2["x"][-1][:19]
PO2_PD2_max_A_unstable = np.max(PO2_PD2["x"][2:-1:3], axis=0)[18:]
PO2_PD2_theta_unstable = PO2_PD2["x"][-1][18:]

PO2_PD3_max_A = np.max(PO2_PD3["x"][2:-1:3], axis=0)
PO2_PD3_theta = PO2_PD3["x"][-1]


fig, ax = plt.subplots()

ax.plot(
    main_hopf_branch_theta_stable,
    main_hopf_branch_A_stable,
    linestyle="solid",
    c="black",
    zorder=0,
)

ax.plot(
    main_hopf_branch_theta_unstable,
    main_hopf_branch_A_unstable,
    linestyle="dashed",
    c="black",
    zorder=1,
)

ax.plot(
    main_PO_branch_theta_stable,
    main_PO_branch_max_A_stable,
    linestyle="solid",
    c="red",
    zorder=2,
)

ax.plot(
    main_PO_branch_theta_unstable,
    main_PO_branch_max_A_unstable,
    linestyle="dashed",
    c="red",
    zorder=2,
)

ax.plot(
    PO1_branch1_theta_stable,
    PO1_branch1_max_A_stable,
    linestyle="solid",
    c="blue",
    zorder=1,
)

ax.plot(
    PO1_branch1_theta_unstable,
    PO1_branch1_max_A_unstable,
    linestyle="dashed",
    c="blue",
    zorder=1,
)

ax.plot(
    PO1_branch2_theta_stable,
    PO1_branch2_max_A_stable,
    linestyle="solid",
    c="blue",
    zorder=1,
)

ax.plot(
    PO1_branch2_theta_unstable,
    PO1_branch2_max_A_unstable,
    linestyle="dashed",
    c="blue",
    zorder=1,
)

ax.plot(
    PO2_branch1_theta_stable,
    PO2_branch1_max_A_stable,
    linestyle="solid",
    c="red",
    zorder=3,
)

ax.plot(
    PO2_branch1_theta_unstable,
    PO2_branch1_max_A_unstable,
    linestyle="dashed",
    c="red",
    zorder=3,
)

ax.plot(
    PO2_branch2_theta_stable,
    PO2_branch2_max_A_stable,
    linestyle="solid",
    c="red",
    zorder=1,
)

ax.plot(
    PO2_branch2_theta_unstable,
    PO2_branch2_max_A_unstable,
    linestyle="dashed",
    c="red",
    zorder=1,
)

ax.plot(
    PO3_branch1_theta_stable,
    PO3_branch1_max_A_stable,
    linestyle="solid",
    c="blue",
    zorder=2,
)

ax.plot(
    PO3_branch1_theta_unstable,
    PO3_branch1_max_A_unstable,
    linestyle="dashed",
    c="blue",
    zorder=2,
)

ax.plot(
    PO3_branch2_theta_stable,
    PO3_branch2_max_A_stable,
    linestyle="solid",
    c="blue",
    zorder=2,
)

ax.plot(
    PO3_branch2_theta_unstable,
    PO3_branch2_max_A_unstable,
    linestyle="dashed",
    c="blue",
    zorder=2,
)

ax.plot(
    PO4_branch1_theta_unstable,
    PO4_branch1_max_A_unstable,
    linestyle="dashed",
    c="red",
)

ax.plot(
    PO4_branch1_theta_stable,
    PO4_branch1_max_A_stable,
    linestyle="solid",
    c="red",
)

ax.plot(
    PO4_branch1_theta_unstable2,
    PO4_branch1_max_A_unstable2,
    linestyle="dashed",
    c="red",
)

ax.plot(
    PO4_branch2_theta_unstable,
    PO4_branch2_max_A_unstable,
    linestyle="dashed",
    c="red",
)

ax.plot(
    PO5_branch1_theta_unstable,
    PO5_branch1_max_A_unstable,
    linestyle="dashed",
    c="blue",
)

ax.plot(
    PO5_branch1_theta_stable,
    PO5_branch1_max_A_stable,
    linestyle="solid",
    c="blue",
)

ax.plot(
    PO5_branch1_theta_unstable2,
    PO5_branch1_max_A_unstable2,
    linestyle="dashed",
    c="blue",
)

ax.plot(
    PO5_branch2_theta_unstable,
    PO5_branch2_max_A_unstable,
    linestyle="dashed",
    c="blue",
)

ax.plot(
    PO6_branch1_theta_unstable,
    PO6_branch1_max_A_unstable,
    linestyle="dashed",
    c="red",
    zorder=1,
)

ax.plot(
    PO6_branch1_theta_stable,
    PO6_branch1_max_A_stable,
    linestyle="solid",
    c="red",
    zorder=1,
)

ax.plot(
    PO6_branch1_theta_unstable2,
    PO6_branch1_max_A_unstable2,
    linestyle="dashed",
    c="red",
    zorder=1,
)

ax.plot(
    PO6_branch2_theta_unstable,
    PO6_branch2_max_A_unstable,
    linestyle="dashed",
    c="red",
    zorder=1,
)

ax.plot(
    PO2_PD1_theta_stable,
    PO2_PD1_max_A_stable,
    linestyle="solid",
    c="green",
)

ax.plot(
    PO2_PD1_theta_unstable,
    PO2_PD1_max_A_unstable,
    linestyle="dashed",
    c="green",
)

ax.plot(
    PO2_PD2_theta_stable,
    PO2_PD2_max_A_stable,
    linestyle="solid",
    c="purple",
)

ax.plot(
    PO2_PD2_theta_unstable,
    PO2_PD2_max_A_unstable,
    linestyle="dashed",
    c="purple",
)

ax.plot(
    PO2_PD3_theta,
    PO2_PD3_max_A,
    linestyle="solid",
    c="orange",
)


ax.scatter(
    [main_hopf_branch["x"][3][23]],
    [main_hopf_branch["x"][2][23]],
    c="black",
    zorder=3,
    s=20,
)

ax.scatter(
    [main_PO_branch_theta_unstable[1]],
    [main_PO_branch_max_A_stable[-1]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO1_branch1_theta_unstable[0]],
    [PO1_branch1_max_A_stable[-1]],
    c="black",
    zorder=3,
    s=20,
)

ax.scatter(
    [PO1_branch2_theta_stable[-1]],
    [PO1_branch2_max_A_stable[-1]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO2_branch1_theta_unstable[0]],
    [PO2_branch1_max_A_stable[-1]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO2_branch2_theta_unstable[0]],
    [PO2_branch2_max_A_unstable[0]],
    c="black",
    zorder=3,
    s=20,
)

ax.scatter(
    [PO3_branch1_theta_unstable[0]],
    [PO3_branch1_max_A_unstable[0]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO3_branch2_theta_unstable[0]],
    [PO3_branch2_max_A_stable[-1]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO4_branch1_theta_unstable[-1]],
    [PO4_branch1_max_A_unstable[-1]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO4_branch1_theta_stable[-1]],
    [PO4_branch1_max_A_stable[-1]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO5_branch1_theta_unstable[-1]],
    [PO5_branch1_max_A_unstable[-1]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO5_branch1_theta_stable[-1]],
    [PO5_branch1_max_A_stable[-1]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO6_branch1_theta_unstable[-1]],
    [PO6_branch1_max_A_unstable[-1]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO6_branch1_theta_stable[-1]],
    [PO6_branch1_max_A_stable[-1]],
    c="black",
    zorder=3,
    s=10,
)

ax.scatter(
    [PO2_PD1_theta_unstable[0]],
    [PO2_PD1_max_A_unstable[0]],
    c="black",
    zorder=3,
    s=20,
)

ax.scatter(
    [PO2_PD2_theta_unstable[0]],
    [PO2_PD2_max_A_unstable[0]],
    c="black",
    zorder=3,
    s=20,
)

ax.scatter(
    [PO2_PD3_theta[-1]],
    [PO2_PD3_max_A[-1]],
    c="black",
    zorder=3,
    s=20,
)

# ax.text(0.46, 0.18, "H")
# ax.text(0.41, 0.36, "PD")
# ax.text(0.42, 0.31, "SN")
# ax.text(0.465, 0.385, "SN")
# ax.text(0.463, 0.25, "SN")
# ax.text(0.375, 0.283, "SN")
# ax.text(0.36, 0.32, "SN")
# ax.text(0.36, 0.32, "SN")
# ax.text(0.325, 0.245, "SN")
# ax.text(0.305, 0.27, "PD")
# ax.text(0.275, 0.205, "SN")
# ax.text(0.255, 0.193, "SN")
# ax.text(0.223, 0.163, "SN")
# ax.text(0.204, 0.15, "PD")
# ax.text(0.16, 0.11, "SN")
# ax.set_ylim(0.0, 0.5)
# ax.set_xlim(0.15, 0.55)

ax.text(0.4251, 0.347, "PD")
ax.text(0.4277, 0.366, "PD")
ax.text(0.4282, 0.372, "PD")
ax.text(0.4282, 0.377, "PD")
ax.text(0.4297, 0.336, "SN")
ax.set_ylim(0.33, 0.38)
ax.set_xlim(0.425, 0.432)

ax.set_xlabel(r"$\theta$")
ax.set_ylabel(r"$\max A$")

# ax2 = ax.twinx()
# ax2.set_ylabel(r"$\lambda$")

# arr = np.loadtxt("../lyapunov/lyapunov_full2.csv",
#                  delimiter=",", skiprows=1)
# lambda1 = arr[:, 0]
# lambda2 = arr[:, 1]
# thetas = arr[:, 3]

# ax2.plot(thetas, lambda1, alpha=0.6)
# # ax2.plot(thetas, lambda2)
# ax2.set_ylim(0.0, 0.005)


plt.tight_layout()
plt.savefig("plots/pd_cascade.png", dpi=200)
