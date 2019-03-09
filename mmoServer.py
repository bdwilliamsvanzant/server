import socket,struct,sys,threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 5199))
server_socket.listen(100)

chars={}#takes id and char info 

#update monsters info and cerify desc
monsters={1:["Sewer rat\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,5,10,0,20,5,2,46,"a sewer rat that looks to be rode by a pickle."],2:["Squirrel\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,10,5,0,20,25,3,43,"Even though its small it packs a mean bite."],3:["homework\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,15,15,0,30,5,4,49,"it seems endless but really is just one question."],4:["Research paper\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,5,30,0,40,25,5,46,"a research paper falling from the upper floors"],5:["Power cord\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,10,20,0,45,25,6,25,"harmless untill strained."],6:["Pop quiz\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,20,40,0,50,25,7,21,"you are not prepared."],7:["Client\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,35,30,0,55,25,8,26,"the gui is a lttle sticky."],8:["Midterm\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,40,10,0,50,25,10,51,"Even though it marks half way the end seems so far."],9:["Broken vanding machine\0\0\0\0\0\0\0\0\0\0",0b10111000,20,30,0,100,25,9,31,"its crashing from a sugar high."],10:["Final\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,5,30,0,100,25,11,26,"should be the last hurdle."],11:["Server\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,90,90,5,1000,55555,12,64,"the destroyer of dreams, ruiner of sleep, and ender of all hope!"]}

#keeps health and gold info for updating
monst_stats={1:["Sewer rat\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,5,10,0,20,5,2,46,"a sewer rat that looks to be rode by a pickle."],2:["Squirrel\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,10,5,0,20,25,3,43,"Even though its small it packs a mean bite."],3:["homework\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,15,15,0,30,5,4,49,"it seems endless but really is just one question."],4:["Research paper\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,5,30,0,40,25,5,46,"a research paper falling from the upper floors"],5:["Power cord\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,10,20,0,45,25,6,25,"harmless untill strained."],6:["Pop quiz\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,20,40,0,50,25,7,21,"you are not prepared."],7:["Client\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,35,30,0,55,25,8,26,"the gui is a lttle sticky."],8:["Midterm\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,40,10,0,50,25,10,51,"Even though it marks half way the end seems so far."],9:["Broken vanding machine\0\0\0\0\0\0\0\0\0\0",0b10111000,20,30,0,100,25,9,31,"its crashing from a sugar high."],10:["Final\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,5,30,0,100,25,11,26,"should be the last hurdle."],11:["Server\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0",0b10111000,90,90,5,1000,55555,12,64,"the destroyer of dreams, ruiner of sleep, and ender of all hope!"]}


#update rooms and set desc
rooms={1:[1,"well",53,"an inconveint place to put a well led you to fall in.",2],2:[2,"sewer",46,"it smells of drained energy drinks and sorrow.",3],3:[3,"parking lot",32,"a squirrel infested parking lot.",4],4:[4,"hallway",37,"abandoned assignments lie everywhere.",5],5:[5,"stairwell",34,"seems empty but you hear a ruffle.",6],6:[6,"classroom",21,"class seems to quiet.",7],7:[7,"room 310",23,"the room of nightmares.",8],8:[8,"tutoring center",38,"lots of random knowledge lies in here.",9],9:[9,"library",58,"a place for silence yet something is making sound in back.",10],10:[10,"testing center",48,"all crammed knowledge is lost entering the room.",11],11:[11,"finals room",16,"no joy lies here",12],12:[12,"computer science lab",36,"no humans have been here only husks.",0]}

#accepts sent for non-changing actions
def accept(type,client):
	x=bytearray()
	x+=(8).to_bytes(1,"little")
	x+=(type).to_bytes(1,"little")
	client.send(x)

#error log function
def error(type,client):
	if (type==0):
		x=bytearray()
		mess="Error: Unkown error."
		x+=(7).to_bytes(1, "little")
		x+=(0).to_bytes(1, "little")
		x+=len(mess).to_bytes(1, "little")
		x+=mess.encode("utf-8")
		client.send(x)
	elif (type==1):
		x=bytearray()
		mess="Error: Bad room. Attempt to change to an inappropriate room."
		x+=(7).to_bytes(1, "little")
		x+=(1).to_bytes(1, "little")
		x+=len(mess).to_bytes(1, "little")
		x+=mess.encode("utf-8")
		client.send(x)
	elif (type==2):
		x=bytearray()
		mess="Error: Player Exists."
		x+=(7).to_bytes(1, "little")
		x+=(2).to_bytes(1, "little")
		x+=len(mess).to_bytes(1, "little")
		x+=mess.encode("utf-8")
		client.send(x)
	elif (type==3):
		x=bytearray()
		mess="Error: Bad Monster. Attempt to loot a nonexistent or not present monster."
		x+=(7).to_bytes(1, "little")
		x+=(3).to_bytes(1, "little")
		x+=len(mess).to_bytes(1, "little")
		x+=mess.encode("utf-8")
		client.send(x)
	elif (type==4):
		x=bytearray()
		mess="Error: Stat error. Caused by setting inappropriate player stats."
		x+=(7).to_bytes(1, "little")
		x+=(4).to_bytes(1, "little")
		x+=len(mess).to_bytes(1, "little")
		x+=mess.encode("utf-8")
		client.send(x)
	elif (type==5):
		x=bytearray()
		mess="Error: Not Ready. Caused by attempting an action too early, for example changing rooms before sending START or CHARACTER."
		x+=(7).to_bytes(1, "little")
		x+=(5).to_bytes(1, "little")
		x+=len(mess).to_bytes(1, "little")
		x+=mess.encode("utf-8")
		client.send(x)
	elif (type==6):
		x=bytearray()
		mess="Error: No target."
		x+=(7).to_bytes(1, "little")
		x+=(6).to_bytes(1, "little")
		x+=len(mess).to_bytes(1, "little")
		x+=mess.encode("utf-8")
		client.send(x)
	elif (type==7):
		x=bytearray()
		mess="Error: No fight."
		x+=(7).to_bytes(1, "little")
		x+=(7).to_bytes(1, "little")
		x+=len(mess).to_bytes(1, "little")
		x+=mess.encode("utf-8")
		client.send(x)
	elif (type==8):
		x=bytearray()
		mess="Error: No player vs. player combat on the server."
		x+=(7).to_bytes(1, "little")
		x+=(8).to_bytes(1, "little")
		x+=len(mess).to_bytes(1, "little")
		x+=mess.encode("utf-8")
		client.send(x)

def move_room(client,chars,rooms,monsters):
	new_room =  int.from_bytes(ord(client.recv(1)).to_bytes(1, "little") + ord(client.recv(1)).to_bytes(1, "little"), "little")
	#check connections to current room then check if new room is in their links else error
	oldroom=(chars[client][7])
	print(oldroom)
	if(new_room==rooms[oldroom][4]):
		chars[client][7]=new_room
		update_info(client,chars,rooms,monsters)
	else:
		error(1,client)

def pvp_fight(client):#no pvp make sure no error occurs
	error(8,client)

def loot(client,chars,rooms,monsters):#calculates gold after kill
	monst_room=chars[client][7]
	chars[client][6]+=monsters[monst_room][6]

def start(client,chars,rooms,monsters):
	update_info(client,chars,rooms,monsters)

def room(client,chars,rooms):
	curr_room=chars[client][7]
	x=bytearray()
	x+=(9).to_bytes(1,"little")
	x+=(rooms[curr_room][0]).to_bytes(2,"little")
	x+=(rooms[curr_room][1]).encode("utf-8")
	x+=(rooms[curr_room][2]).to_bytes(2,"little")
	x+=(rooms[curr_room][3]).encode("utf-8")
	client.send(x)

def character(client):#takes user id and sends back character info
	x=bytearray()
	x+=(10).to_bytes(1,"little")
	x+=(chars[client][0]).encode("utf-8")
	x+=(chars[client][1]).to_bytes(1,"little")
	x+=(chars[client][2]).to_bytes(2,"little")
	x+=(chars[client][3]).to_bytes(2,"little")
	x+=(chars[client][4]).to_bytes(2,"little")	
	x+=(chars[client][5]).to_bytes(2,"little")
	x+=(chars[client][6]).to_bytes(2,"little")
	x+=(chars[client][7]).to_bytes(2,"little")
	x+=(chars[client][8]).to_bytes(2,"little")
	x+=(chars[client][9]).encode("utf-8")
	client.send(x)

def characters(client):#takes user room and sends others chars in room may cause error

	for x in chars:
		if (chars[client][7]==chars[x][7]):
			x=bytearray()
			x+=(10).to_bytes(1,"little")
			x+=(chars[client][0]).encode("utf-8")
			x+=(chars[client][1]).to_bytes(1,"little")
			x+=(chars[client][2]).to_bytes(2,"little")
			x+=(chars[client][3]).to_bytes(2,"little")
			x+=(chars[client][4]).to_bytes(2,"little")	
			x+=(chars[client][5]).to_bytes(2,"little")
			x+=(chars[client][6]).to_bytes(2,"little")
			x+=(chars[client][7]).to_bytes(2,"little")
			x+=(chars[client][8]).to_bytes(2,"little")
			x+=(chars[client][9]).encode("utf-8")
			client.send(x)

def game(client):
	x=bytearray()
	desc="While running away from networking class you fell in a well. There's only one way out and thats through the hole in the wells wall."		
	x+=(11).to_bytes(1,"little")
	x+=(100).to_bytes(2,"little")
	x+=(65535).to_bytes(2,"little")
	x+=(len(desc)).to_bytes(2,"little")
	x+=(desc).encode("utf-8")	
	client.send(x)

def connection(client,chars,rooms):
	curr_room=chars[client][7]
	next_room=curr_room+1
	room_name=rooms[next_room][1]
	room_desc_len=rooms[next_room][2]
	room_desc=rooms[next_room][3]
	x=bytearray()
	x+=(13).to_bytes(1,"little")
	x+=(next_room).to_bytes(2,"little")
	x+=(room_name).encode("utf-8")
	x+=(room_desc_len).to_bytes(2,"little")
	x+=(room_desc).encode("utf-8")
	client.send(x)

def monster_room(client,chars,rooms,monsters):
	curr_room=chars[client][7]
	x=bytearray()
	x+=(10).to_bytes(1,"little")
	x+=(monsters[curr_room][0]).encode("utf-8")
	x+=(monsters[curr_room][1]).to_bytes(1,"little")
	x+=(monsters[curr_room][2]).to_bytes(2,"little")
	x+=(monsters[curr_room][3]).to_bytes(2,"little")	
	x+=(monsters[curr_room][4]).to_bytes(2,"little")
	x+=(monsters[curr_room][5]).to_bytes(2,"little")
	x+=(monsters[curr_room][6]).to_bytes(2,"little")
	x+=(monsters[curr_room][7]).to_bytes(2,"little")
	x+=(monsters[curr_room][8]).to_bytes(2,"little")
	x+=(monsters[curr_room][9]).encode("utf-8")
	client.send(x)

def update_info(client,chars,rooms,monsters):
	connection(client,chars,rooms)
	monster_room(client,chars,rooms,monsters)
	room(client,chars,rooms)
	character(client)
	characters(client)

#set up recieve handling
def server_recv(msg,client,chars,rooms,monsters,monst_stats):
	if (msg==1):
		msg_len=int.from_bytes(ord(client.recv(1)).to_bytes(1, "little") + ord(client.recv(1)).to_bytes(1, "little"), "little")
		recv_name=(client.recv(32)).decode('utf-8')
		send_name=(client.recv(32)).decode('utf-8')
		mesg=(client.recv(msg_len)).decode('utf-8')
		for x in chars:
			if(recv_name==chars[x][0]):
					x=bytearray()
					x+=(msg_len).to_bytes(2,"little")
					x+=(recv_name).encode("utf-8")
					x+=send_name.encode("utf-8")
					x+=mesg.encode("utf-8")
					client.send(x)
					accept(1,client)
			else:
				error(6,client)
	elif(msg==2):
		move_room(client,chars,rooms,monsters)
		update_info(client,chars,rooms,monsters)
	elif(msg==3):	
		curr_room=chars[client][7]
		if(chars[client][7]==1):
			error(7,client)
		else:
			if(monsters[curr_room][5]<=0):
				error(7,client)
			else:
				if(((chars[client][2])-(monsters[curr_room][3]))<=0):
						if(((monsters[curr_room][2])-(chars[client][3]))<=0):
								update_info(client,chars,rooms,monsters)
						else:
							if((chars[client][5])>0):
								(chars[client][5])-=((monsters[curr_room][3])-(chars[client][3]))
								update_info(client,chars,rooms,monsters)
							else:
								chars[client][5]=100
								chars[client][6]=0
								chars[client][7]=rooms[1][0]
								update_info(client,chars,rooms,monsters)
				else:
					(monsters[curr_room][5])-=(chars[client][2])-(monsters[curr_room][3])
					if(monsters[curr_room][5]<=0):
							loot(client,chars,rooms,monsters)
							monsters[curr_room][5]=monst_stats[curr_room][5]
							update_info(client,chars,rooms,monsters)
								
		update_info(client,chars,rooms,monsters)			
	elif(msg==4):	
		error(8,client)
	elif(msg==5):
		update_info(client,chars,rooms,monsters)
	elif(msg==6):
		start(client,chars,rooms,monsters)	
	elif(msg==10):
		data=client.recv(32)
		charname=""
		for i in data:
			if i != 0:
				charname+=chr(i)
			else:
				break
		charname.ljust(32)
		client.recv(1)
		flags=0b11011000
		atk=int.from_bytes(ord(client.recv(1)).to_bytes(1,"little")+ord(client.recv(1)).to_bytes(1,"little"),"little")
		defense=int.from_bytes(ord(client.recv(1)).to_bytes(1,"little")+ord(client.recv(1)).to_bytes(1,"little"),"little")
		regen=int.from_bytes(ord(client.recv(1)).to_bytes(1,"little")+ord(client.recv(1)).to_bytes(1,"little"),"little")
		client.recv(6)		
		health=100
		gold=0
		currroom=rooms[1][0]
		desclen=int.from_bytes(ord(client.recv(1)).to_bytes(1,"little")+ord(client.recv(1)).to_bytes(1,"little"),"little")
		chardesc=(client.recv(desclen)).decode("utf-8")	
		for x in chars:
			if(charname==chars[x][0]):
				error(2,client)
		if(atk+defense+regen>100 or atk+defense+regen<100):
			error(4,client)
		else:
			chars[client]=[charname,flags,atk,defense,regen,health,gold,currroom,desclen,chardesc]		
			accept(10,client)
			#broadcast
	elif(msg==12):
		a=client
		del chars[a]
		client.close()
	else:
		error(0,client)

#receive a message type and then send to server receive
def recieved_connections(client):
	while True:
		message_type=ord(client.recv(1))
		print(message_type)	#checking what message is incoming
		server_recv(message_type,client,chars,rooms,monsters,monst_stats)
	
#allow 100 connections start thread
def main():
	server_socket.listen(100)
	while True:
		client, caddr = server_socket.accept()
		game(client)
		threading.Thread(target=recieved_connections,args=(client,)).start()

main()
