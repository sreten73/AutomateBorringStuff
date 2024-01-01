from PIL import Image

wmatrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')

wmatrix.show()
mask.show()

print(wmatrix.size)
print(mask.size)

mask = mask.resize((1015,559))
#Get mask be transparent
mask.putalpha(200)
mask.show()
#Paste mask over wmatrix
wmatrix.paste(mask,(0,0),mask)
wmatrix.show()