# BIG ASSUMPTION: Sun is from the left (i.e. horizontal in the x direction)
import random
board = [
 [ {'player':'', 'tree':''}, {'player':'red', 'tree':'short'},{'player':'', 'tree':''},{'player':'blue', 'tree':'short'},{'player':'', 'tree':''}, ],

 [ {'player':'', 'tree':''},{'player':'blue', 'tree':'tall'},{'player':'', 'tree':''},{'player':'red', 'tree':'shortS'},{'player':'', 'tree':''},],

 [ {'player':'', 'tree':''},{'player':'', 'tree':''},{'player':'', 'tree':''},{'player':'', 'tree':''},{'player':'', 'tree':''},],

 [ {'player':'', 'tree':''},{'player':'', 'tree':''},{'player':'red', 'tree':'tall'},{'player':'blue', 'tree':'tall'},{'player':'red', 'tree':'tallS'},],

 [ {'player':'', 'tree':''},{'player':'red', 'tree':'short'},{'player':'blue', 'tree':'shortS'},{'player':'', 'tree':''},{'player':'', 'tree':''},],
]
# print (board)

def score_row(game_row):
  # Returns a tuple of scores. Needs to be implemented. "red" is first item, "blue" is second item
  return (0, 0) 



row1 = [
  {'player':'','tree':''}, 
  {'player':'red','tree':'short'}, 
  {'player':'blue','tree':'short'}, 
  {'player':'','tree':''} 
  ]
#testing  
print(row1[1]['tree'])
print(row1[1]['player'])

# Remove None value types in dictionaries list 
# Using list comprehension 
clean_up = [ele for ele in ({key: val for key, val in sub.items() if val} for sub in row1) if ele] 
print(str(clean_up))

# #sorted by player and trees but not by red and blue player 
#from collections import defaultdict
# res = defaultdict(list)
# for sub in clean_up:
#   for key in sub:
#     res[key].append(sub[key])
# print(str(dict(res)))



# this should be (1, 0) because the red tree gets sun, the blue tree is shaded
print(score_row(row1))

row = [{'player':'','tree':''}, {'player':'red','tree':'short'}, {'player':'blue','tree':'tall'}, {'player':'','tree':''} ]
# this should be (1, 2) because the tall tree is not shaded
print(score_row(row))

row = [{'player':'','tree':''}, {'player':'red','tree':'short'}, {'player':'blue','tree':'tall'}, {'player':'red','tree':'tall'} ]
# this should be (1, 2) because the last tall tree is shaded
print(score_row(row))

row = [{'player':'','tree':''}, {'player':'red','tree':'tall'}, {'player':'blue','tree':'short'}, {'player':'red','tree':'tall'} ]
# this should be (2, 0) because the first tall tree shades the other two trees
print(score_row(row))

# def player_rules(players):
# 	#selecting a piece
# 	# player1 = input(“Red player select a square”)
# 	# if board[‘tree’] == “short” or board[‘tree’] == “shortS” or board[‘tree’] == “tall” or board[‘tree’] == “tallS”:
# 	# 	print (“Select another square”)
# 	# else:
# 	# 	print (random.choice(trees))

# 	count_short = board.count(“short”)
# 	count_tall = board.count(“tall”)*2
# 	count_shortS = board.count(“shortS”)
#   count_tallS = board.count(“tallS”)*(2)
# 	sum_trees = count_short + count_tall - count_shortS - count_tallS
# 	if player1 > player2:
# 		print(“Red player wins”)
# 	elif player1 < player2:
# 		print(“Blue player wins”)
# 	else player1 == player2:
# 		print(“It’s a draw!”)
