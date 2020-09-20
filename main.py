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

# for row in board:
#   for piece in row:
#     player1 = board[1]['tree']
    # if player 1 == :
    # print (player1)

def score_row(game_row):
  # Returns a tuple of scores. Needs to be implemented. "red" is first item, "blue" is second item
  return (0, 0) 


row1 = [  {'player':'','tree':''},   {'player':'red','tree':'short'},   {'player':'','tree':''},   {'player':'blue','tree':'short'},   {'player':'','tree':''}   ]
# this should be (1, 1) 
print(score_row(row1))

row2 = [{'player':'','tree':''}, {'player':'blue','tree':'tall'}, {'player':'','tree':''}, {'player':'red','tree':'shortS'}, {'player':'','tree':''} ]
# this should be (-1, 2) 
print(score_row(row2))

row4 = [{'player':'','tree':''}, {'player':'','tree':''}, {'player':'red','tree':'short'}, {'player':'blue','tree':'tall'}, {'player':'red','tree':'tallS'} ]
# this should be (-1, 2) 
print(score_row(row4))

row5 = [{'player':'','tree':''}, {'player':'red','tree':'short'}, {'player':'blue','tree':'shortS'}, {'player':'','tree':''}, {'player':'','tree':''} ]
# this should be (1, -1) 
for x in row5:
    for y in x:
        if x.get(y) == 'short':
            x.update({y: "1"})
  print (row5)
print(score_row(row5))

# values of each tree
tree_score = {  'short': 1, 'shortS': -1, 'tall': 2, 'tallS': -2,}
print ('\n')


# Remove None value types in dictionaries list 
# Using list comprehension 
clean_up1 = [ele for ele in ({key: val for key, val in sub.items() if val} for sub in row1) if ele] 
clean_up2 =[ele for ele in ({key: val for key, val in sub.items() if val} for sub in row2) if ele] 
clean_up4 =[ele for ele in ({key: val for key, val in sub.items() if val} for sub in row4) if ele] 
clean_up5 =[ele for ele in ({key: val for key, val in sub.items() if val} for sub in row5) if ele] 

clean_up = clean_up1 +clean_up2 + clean_up4 + clean_up5
# prints all the list with no empty values
print(str(clean_up))
# print ('\n')

#testing output: short, red 
# print(row1[1]['tree'])
# print(row1[1]['player'])

#sorted by player and trees but not by red and blue player 
# from collections import defaultdict
# res = defaultdict(list)
# for sub in clean_up:
#   for key in sub:
#     res[key].append(sub[key])
# print(str(dict(res)))
# for sub in clean_up:
#   # for key in sub:
#   red = clean_up[1]['tree']
#     # if player 1 == :
#   print (red)



# def player_rules(players):
	#selecting a piece
	# player1 = input(“Red player select a square”)
	# if board[‘tree’] == “short” or board[‘tree’] == “shortS” or board[‘tree’] == “tall” or board[‘tree’] == “tallS”:
	# 	print (“Select another square”)
	# else:
	# 	print (random.choice(trees))
  # player1 = row1[1]['player']
  # player2 = row1[0]['player']
	# count_short = board.count('short')
	# count_tall = board.count('tall')*2
	# count_shortS = board.count('shortS')
  # # count_tallS = board.count('tallS')*2
	# sum_trees = count_short + count_tall - count_shortS - count_tallS
	# if player1 > player2:
	# 	print('Red player wins')
	# elif player1 < player2:
	# 	print('Blue player wins')
	# else player1 == player2:
	# 	print('It’s a draw!'')