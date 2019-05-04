import ui

#Set Variables and lists for the game
board = [['*','*','*'],['*','*','*'],['*','*','*']]
moves= ['TL', 'TC', 'TR', 'CL', 'CC', 'CR', 'BL', 'BC', 'BR']
values=('X','O')
turn=['X']
move_key={'T':0, 'L':0, 'C':1,'B':2, 'R':2}

def Wins(player, M):
#Checks to see if player has three in a row on board M.
	if player =='X':
		check ='O'
	else:
	 	check ='X'
	w=[]
	T_M=[[row[i] for row in M] for i in range(3)]
	#T_M is the transpose of M
	D1=[M[0][0],M[1][1],M[2][2]]
	#Downward diagonal elements of M
	D2=[M[2][0],M[1][1],M[0][2]]
	#Upward diagonal elements of M
	w.append((check not in D1) and ('*' not in D1))
	w.append((check not in D2) and ('*' not in D2))
	w.append((check not in M[0]) and ('*' not in M[0]))
	w.append((check not in M[1]) and ('*' not in M[1]))
	w.append((check not in M[2]) and ('*' not in M[2]))
	w.append((check not in T_M[0]) and ('*' not in T_M[0]))
	w.append((check not in T_M[1]) and ('*' not in T_M[1]))
	w.append((check not in T_M[2]) and ('*' not in T_M[2]))
	value = True in w
	return value

def button_tapped(sender):
	label = sender.superview['Label']
	move=sender.name
	x=move_key.get(move[0])
	y=move_key.get(move[1])
	board[x][y]=turn[0]
	sender.title=turn[0]
	
	if Wins(turn[0], board):
		label.text=turn[0]+' Wins!'

		
	if turn[0]=='O':
		turn[0]='X'
		
	else:
		turn[0]='O'

v=ui.load_view('TicTacToe').present('sheet')

