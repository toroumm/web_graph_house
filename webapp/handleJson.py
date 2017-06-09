import json,re
import os,sys


COLORS = [ (202, 201, 197),  # Light gray
			(171, 9, 0),      # Red
    			(166, 78, 46),    # Light orange
    			(255, 190, 67),   # Yellow
    			(163, 191, 63),   # Light green
    			(122, 159, 191),  # Li	ght blue
    			(140, 5, 84),     # Pink
    			(166, 133, 93),   # Light brown
    			(75, 64, 191),    # Red blue
    			(237, 124, 60),    # orange
		]

#********************************************************************************************
def next_color(color_list):
		#Create a different color from a base color list.
		
		step = 20

		color = color_list[random.randint(0, len(color_list) - 1)]
		while True:
			#for color in color_list:

			yield map(lambda base: (base + step) % 256, color)

			step += 50

#********************************************************************************************


with open('dataZap.json') as d:
	data = json.load(d)

_dict = {}

for i in data:
	if data[i]['cidade'] == None:

		b = re.split('\n',data[i]['endereco'])
		
		bairro = b[0]
		endereco = re.split(u'\u2022',b[1])[0]		
		cidade = re.split(u'\u2022',b[1])[1]

		if cidade not in _dict.keys():
			_dict[cidade] = {'size':15, 'color':COLORS[0], 'bairros':[{'bairro':bairro, 'color':COLORS[2],'size':10, 'casas':[{'endereco':endereco, 'size':5, 'color':COLORS[3]}]}]}
		
		else:
			#print bairro, _dict[cidade]['bairros']

			#sys.exit()			
			check = True
			for j in _dict[cidade]['bairros']:
				
				if bairro == j['bairro']:
					_dict[cidade]['bairros'].append({'bairro':bairro, 'color':COLORS[2],'size':10, 'casas':[{'endereco':endereco, 'size':5, 'color':COLORS[3]}]})
					check = False
			
			if check:
				_dict[cidade]['bairros'].append({'bairro':bairro, 'color':COLORS[2],'size':10, 'casas':[{'endereco':endereco, 'size':5, 'color':COLORS[3]}]})

			else:
				
				_dict[cidade]['bairros']['casas'].append({'endereco':endereco, 'size':5, 'color':COLORS[3]})
			
		
	
		#print 'ENDERECO', len(b), cidade, bairro, endereco 
	else:
		print 'CIDADE', data[i]['cidade']


with open('/home/jeferson/Desktop/web_graph_house/webapp/templates/webapp/imoveis.json','wb') as jj:
	json.dump(_dict,jj)

