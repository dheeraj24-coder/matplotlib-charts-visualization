import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, figsize=(16, 12), facecolor="skyblue")

# ----------------------------
# 1. Bar Chart
# ----------------------------
team_wins = df["WinningTeam"].value_counts()

ax[0,0].bar(team_wins.index, team_wins.values, color="purple")
ax[0,0].set_facecolor("darkgrey")
ax[0,0].set_title("Matches Won by Each Team")
ax[0,0].set_xlabel("Teams")
ax[0,0].set_ylabel("Wins")
ax[0,0].tick_params(axis='x', rotation=90)

# ----------------------------
# 2. Line Chart
# ----------------------------
season_matches = df["Season"].value_counts().sort_index()

ax[0,1].plot(
    season_matches.index,
    season_matches.values,
    marker="o",
    color="red"
)
ax[0,1].set_title("Matches Played Each Season")
ax[0,1].set_facecolor("cyan")
ax[0,1].set_xlabel("Season")
ax[0,1].set_ylabel("Matches")
ax[0,1].grid(True)

# ----------------------------
# 3. Pie Chart
# ----------------------------
toss = df["TossDecision"].value_counts()

ax[1,0].pie(
    toss,
    labels=toss.index,
    autopct="%1.1f%%",
    startangle=90
)
ax[1,0].set_title("Toss Decision Distribution")

# ----------------------------
# 4. Scatter Chart
# ----------------------------
ax[1,1].scatter(
    df["Season"],
    df["Margin"],
    color="yellow",
    alpha=0.6
)
ax[1,1].set_title("Winning Margin by Season")
ax[1,1].set_facecolor("lightblue")
ax[1,1].set_xlabel("Season")
ax[1,1].set_ylabel("Winning Margin")

# ----------------------------
# Adjust Layout
# ----------------------------
plt.tight_layout()

plt.show()
