from PIL import Image, ImageFont,ImageDraw
import textwrap
import sqlite3
import io

#------------------------------------------------ Consultando o banco---------------------------------------------------------------
banco = sqlite3.connect("image_data_ultimate.db")

cursor = banco.cursor()

row =  cursor.execute("SELECT * FROM philosophers_table ORDER BY random() LIMIT 1") # retorna uma linha aleatória

for x in row:
    rec_im = x[2] # a terceira coluna da row indexada por dois eh a imagem
    pensador = x[1] 

autor_image = Image.open(io.BytesIO(rec_im))

cursor.close()
banco.close()

#------------------------------------------------ Adicionando texto ---------------------------------------------------------------

frase_de_efeito = "\" " + "Frase Randomicamente Engraçada" + " \"" # print(len(long_string)) nesse caso, o bot so aceita strings de no maximo 160 caracteres

fundo = Image.open("imgs_req/fundo_preto.jpg")

draw = ImageDraw.Draw(fundo)

text_formatado = textwrap.fill(frase_de_efeito,23) # segundo arg width
autor = "-" + pensador

font1 = ImageFont.truetype("fonts/arial_narrow_7.ttf",50)
font2 = ImageFont.truetype("fonts/arial_narrow_7.ttf",30)


draw.text((80,140),text_formatado,(255,255,255),font=font1) #desenha frase
draw.text((45,525),autor,(255,255,255),font=font2) # desenha autor

fundo_mod = fundo # so para deixar claro alteração

#----------------------------------------------- Concatena duas imagens ---------------------------------------------------------

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


autor_image_newsize = autor_image.resize((428,584)) #Redmensionar para encaixar

parte_branca = Image.open("imgs_req/parte_branca_650_x_584.jpg")

imagem_concatenada = get_concat_h(parte_branca,autor_image_newsize)

mask = Image.open("imgs_req/gradiente.jpg").convert("L")

img_final = Image.composite(imagem_concatenada,fundo_mod,mask)

img_final.show()