# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_first_goal = "Ruud Gullit"
player_second_goal = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player_first_goal + " " + str(goal_0) + ", " + player_second_goal + " " + str(goal_1)
report = f'{player_first_goal} scored in the {goal_0}nd minute\n{player_second_goal} scored in the {goal_1}th minute'
player = "Ronald Koeman"
first_name = player[:player.find(" ")]
last_name_len = len(player[player.find(" ") + 1:])
name_short = f'{player[0]}. {player[len(first_name) + 1:]}'

chant = (f'{first_name}! ' * len(first_name)).rstrip()
good_chant = chant[-1] != " "
