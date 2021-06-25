# Write your function, here.
def track_robot(instructions):
  totals = {'left': 0, 'right': 0, 'up': 0, 'down': 0}
  for step in instructions:
      step = step.split()
      totals[step[0]] += int(step[1])
  return [totals['right'] - totals['left'], totals['up'] - totals['down']]


print(track_robot(["right 10", "up 50", "left 30", "down 10"]))
# Prints [-20, 40]

print(track_robot([]))
# Prints [0, 0]
# If there are no instructions, the robot doesn't move.

print(track_robot(["right 100", "right 100", "up 500", "up 10000"]))
# Prints [200, 10500]