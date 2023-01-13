import os

parent = "/home/spile/Downloads/EGE_INF"

for i in range(1, 27):
	path = os.path.join(parent, str(i), 'description.md')
	path2 = os.path.join(parent, str(i), 'README.md')
	os.remove(path)
	with open(path2, 'w') as f:
		f.write(f'Задание номер {i}')

	print(f"Сделал все в папке {i}")