from instabot import Bot
import time

bot = Bot()

bot.login(username="seu-user-name-aqui", password="sua-senha-aqui")

imagem = ['imagem0', 'imagem1.jpg', 'imagem2.jpg', 'imagem3.jpg']

frase = '@seu-@-aqui #-sua-#-aqui'

print('Iniciando automação de postagens...')

for i in range(1, 4):
    img = imagem[i]
    # coloque a foto na mesma pasta onde o script se encontra.
    # Caso contrario coloque o caminho completo da imagem.
    # Só funciona com imagens JPG.
    # A imagem é descartada depois do upload.
    bot.upload_photo(img, caption=frase)

    print(f'Post({i}) concluido!')
    print('Aguardando 30 segundos...')
    for x in range(1, 30):
        print(x, '. ', end='')
        time.sleep(1)
    print('')

print('')
print('.')
print('.')
print('.')
print('')
print('Automação de Postagens concluidas com sucesso!')${{ secrets.GITHUB_TOKEN }}