import pyscreenshot as ImageGrab

def main():
    imagem = ImageGrab.grab()
    imagem.save('screenShot1.jpg', 'jpeg')

if __name__ == "__main__":
    main()