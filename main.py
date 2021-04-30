from PIL import Image, ImageFont,ImageDraw
import textwrap

frase_de_efeito = "\" " + "Vem monstro!" + " \"" # print(len(long_string)) nesse caso, o bot so aceita strings de no maximo 160 caracteres

fundo = Image.open("imgs_req/fundo_preto.jpg")

#------------------------------------------------ Adicionando texto ---------------------------------------------------------------
draw = ImageDraw.Draw(fundo)

text_formatado = textwrap.fill(frase_de_efeito,23) # segundo arg width
autor = "-Leo Stronda"

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

autor_image = Image.open("image_data/Leo_Stronda.jpg")
autor_image_newsize = autor_image.resize((428,584)) #Redmensionar para encaixar


parte_branca = Image.open("imgs_req/parte_branca_650_x_584.jpg")

imagem_concatenada = get_concat_h(parte_branca,autor_image_newsize)

mask = Image.open("imgs_req/gradiente.jpg").convert("L")

img_final = Image.composite(imagem_concatenada,fundo_mod,mask)

img_final.save("img_output/Imagem-Retornada-1.jpg")

img_final.show()

