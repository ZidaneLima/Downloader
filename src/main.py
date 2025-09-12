from down import down

def main():
    print("\n Bem vindo, deseja baixar um vídeo/live?\n")
    url = input(" Digite a URL do vídeo: ")

    if not url:
        print("\n Nenhuma URL fornecida, encerrando o script.")
        return
    
    try:
        down(url)
        print("\n Download Finalizado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")

if __name__ == "__main__":
    main()
