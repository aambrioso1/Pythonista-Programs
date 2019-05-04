from scene import *
import os
import time

path = os.getcwd()

name=input('Please enter you name.\n')

with open('names.txt', 'a') as f1:
        f1.write(name+'\n')
start = time.time() #time.clock()
class MyScene (Scene):
		
		def setup(self):
			self.background_color = 'midnightblue'
			self.star = SpriteNode('spc:StarGold')
			self.star.position = self.size
			self.star2 = SpriteNode('spc:StarGold')
			self.star2.position = self.size/2
			self.add_child(self.star)
			self.add_child(self.star2)
			
			#Labeling Game
			# The font of a `LabelNode` is set using a tuple of font name and size.
			score_font = ('Futura', 20)
			self.score_label = LabelNode('Ok '+ name + ', align the stars!',score_font, parent=self)
			# The label is centered horizontally near the top of the screen:
			self.score_label.position = (self.size.w/2, self.size.h - 50)
			# The score(time) should appear on top of everything else, so we set the `z_position` attribute here. The default `z_position` is 0.0, so using 1.0 is enough to make it appear on top of the other objects.
			self.score_label.z_position = 1
			self.score = 0
			
			self.highscore_label = LabelNode('Fastest time: ',score_font, parent=self)
			# The label is centered horizontally near the top of the screen:
			self.highscore_label.position = (self.size.w/2, self.size.h - 75)
			# The score(time) should appear on top of everything else, so we set the `z_position` attribute here. The default `z_position` is 0.0, so using 1.0 is enough to make it appear on top of the other objects.
			self.highscore_label.z_position = 1

		def update(self):
			x, y, z = gravity()
			
			if self.star.position == self.size/2:
				self.star.position = self.size/2
			else:
				mx = self.size[0] / 2
				pos = self.star.position
				pos += (x * 300, y * 300)
				
				#Don't allow the star to move beyond the # screen bounds:
					
				pos.x = max(10, min(self.size.w, pos.x)-10)
				pos.y = max(10, min(self.size.h, pos.y)-10)

				self.star.position = pos
				mx = self.size[0]/2
				my = self.size[1]/2
				dif = 3
				
				if mx - dif < pos[0] < mx + dif and my - dif < pos[1] < my + dif:
					self.star.position = self.size/2
					end = time.time()
					#time.clock()
					total_time=round(end - start,3)
					label= name + ' you took: '+str(total_time)+' seconds!'
					self.score_label.text=label
					
					with open('times.txt', 'a') as f1:
					    f1.write(str(total_time)+'\n')
					
					with open('highscore.txt') as f1:
					    oldtime = float(f1.read()) 
					
					if total_time < oldtime:
					    with open('highscore.txt', 'w') as f1: f1.write(str(total_time))
					    with open('highscorename.txt', 'w') as f1: f1.write(name)
					    
					
					with open('highscore.txt') as f1:
					    newtime = float(f1.read()) 
					with open('highscorename.txt') as f1: highscorename=f1.read()
					self.highscore_label.text='Fastest time: ' + str(newtime) + ' by ' + highscorename

run(MyScene(), PORTRAIT)


