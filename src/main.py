from downvideo import downvideo
from downaudio import downaudio

def main():
    print("\n Bem vindo, deseja baixar um vídeo/áudio?\n")
    url = input(" Digite a URL do vídeo/áudio: ")

    if not url:
        print("\n Nenhuma URL fornecida, encerrando o script.")
        return

    while True:
        formato = input("Digite [1] para Vídeo ou [2] para Áudio: ")
        if formato in ["1", "2"]:
            break
        print("\n Opção inválida. \nPor favor, escolha '1' para Vídeo ou '2' para Áudio.")
    
        try:
            if formato == "1":
                downvideo(url)
            else:
                downaudio(url)
            print("\n Download Finalizado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro durante o download: {e}")

if __name__ == "__main__":
    main()