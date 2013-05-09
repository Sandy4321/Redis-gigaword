all:
	python 100Clients.py recap.input Outputs mapping.map 1 > Measurements/1.txt
	python 100Clients.py recap.input Outputs mapping.map 4 > Measurements/4.txt
	python 100Clients.py recap.input Outputs mapping.map 20 > Measurements/20.txt
	python 100Clients.py recap.input Outputs mapping.map 50 > Measurements/50.txt
	python 100Clients.py recap.input Outputs mapping.map 100 > Measurements/100.txt
	python 100Clients.py recap.input Outputs mapping.map 200 > Measurements/200.txt
