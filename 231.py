# Fails 231.py
2 # Autors .....
3
4 from PythonMagick import Image 5
6 # Izgatavojam jaunu objektu - bilde
7 # Objekta izmeers 3x3 pixels
8 bilde = Image ( "3x3", "#22aaff" )
9
10 # Izgatavojam mainigos x un y
11 x=y=0
12
13 #Uzstaada objekta 'bilde' x,y pixela kraasu
14 bilde.pixelColor ( x, y, "#eeff22" )
15
16 # 3x3 pixels palielina liidz 200x200
17 bilde.scale ( "200x200" )
18
19 # Objektu 'bilde'' ieraksta failaa
20 bilde.write ( "231.png" )
