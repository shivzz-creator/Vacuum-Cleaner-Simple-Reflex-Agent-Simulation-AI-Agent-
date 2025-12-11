📘 Vacuum Cleaner — Simple Reflex Agent Simulation (AI Agent)

This project simulates a Simple Reflex Agent in a 2×2 Vacuum World environment, commonly used in introductory Artificial Intelligence courses.

The agent perceives whether a room is Dirty or Clean and chooses an action based solely on the current percept — no memory, no model of the world.

🎯 What This Simulation Demonstrates

Simple Reflex Agent behavior

Agent–environment interaction

State transitions

Grid-based environment visualization

Cleaning strategy without memory

Randomized environment dirt conditions

Step-by-step simulation visualization

🧠 Theory: Simple Reflex Agent

A Simple Reflex Agent selects actions only based on the current percept.

Agent Function
If CurrentState == Dirty → Clean  
Else → Move  

Characteristics
Feature	Description
Memory	❌ None
Internal Model	❌ None
Intelligence Level	⭐ Basic
Reactiveness	✔ Immediate
Goal-Oriented	❌ No
Utility-Based	❌ No

A simple reflex agent works well in fully observable environments but struggles with
hidden information or long-term planning.

🗺 Environment Layout (2x2 Grid)
+-------+-------+
|Room1  |Room2  |
|Clean/Dirty     |
+-------+-------+
|Room3  |Room4  |
|Clean/Dirty     |
+-------+-------+


Rooms are randomly initialized as "Clean" or "Dirty".

🚀 How the Agent Works

At every step:

Agent checks current room

If dirty → cleans it

If clean → moves to next room

Visualization updates

Logs are printed in console

The agent cycles through rooms in this order:

Room1 → Room2 → Room3 → Room4 → Repeat

🖼 Simulation Visualization

Each step shows:

Green room → Clean

Red room → Dirty

Blue circle → Agent position

Room labels
