import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import time

# ------------------------------
# ENVIRONMENT SETUP
# ------------------------------

rooms = ["Room1", "Room2", "Room3", "Room4"]

# Random dirt placement for realism
environment = {room: random.choice(["Clean", "Dirty"]) for room in rooms}

# Mapping for grid positions
room_positions = {
    "Room1": (0, 1),  # Top-left
    "Room2": (1, 1),  # Top-right
    "Room3": (0, 0),  # Bottom-left
    "Room4": (1, 0)   # Bottom-right
}

agent_index = 0     # Agent starts at Room1
action_log = []     # Store actions


# ------------------------------
# REFLEX AGENT
# ------------------------------
def reflex_agent(state):
    """
    Simple Reflex Agent:
    - If room is dirty → Clean
    - Else → Move to next room
    """
    if state == "Dirty":
        return "Clean"
    else:
        return "Move"


# ------------------------------
# DRAW GRID FUNCTION
# ------------------------------
def draw_environment(env, agent_pos, step):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Step {step} — Agent in {rooms[agent_pos]}", fontsize=14)

    # Draw grid rooms
    for room, pos in room_positions.items():
        x, y = pos
        color = "#d9534f" if env[room] == "Dirty" else "#5cb85c"
        rect = patches.Rectangle((x, y), 1, 1, facecolor=color, edgecolor='black')
        ax.add_patch(rect)

        # Room name
        ax.text(x + 0.5, y + 0.65, room, ha='center', va='center', 
                color="white", fontsize=12, weight='bold')

        # Dirty/clean label
        ax.text(x + 0.5, y + 0.3, env[room], ha='center', va='center', 
                color="white", fontsize=10)

    # Draw agent
    ax.add_patch(
        patches.Circle((room_positions[rooms[agent_pos]][0] + 0.5,
                        room_positions[rooms[agent_pos]][1] + 0.5),
                        0.12, color='blue')
    )

    # Show update
    plt.pause(0.7)
    plt.close()


# ------------------------------
# RUN SIMULATION
# ------------------------------
plt.ion()
steps = 10

for step in range(1, steps + 1):
    current_room = rooms[agent_index]
    state = environment[current_room]
    action = reflex_agent(state)

    action_log.append(f"Step {step}: Agent in {current_room} → {action}")
    print(action_log[-1])

    draw_environment(environment, agent_index, step)

    if action == "Clean":
        environment[current_room] = "Clean"
    else:
        agent_index = (agent_index + 1) % len(rooms)

plt.ioff()
print("\nSimulation Completed!")
