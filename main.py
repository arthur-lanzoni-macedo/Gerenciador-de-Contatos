import os

lista_de_contatos = []

# TITULO
def titulo_projeto():
    os.system("cls")
    print(("𝒢ℰℛℰ𝒩𝒞ℐ𝒜𝒟𝒪ℛ 𝒟ℰ 𝒞𝒪𝒩𝒯𝒜𝒯𝒪𝒮\n"))    

# MENU DE OPÇÕES
def opcao_menu():
    print("1- Adicionar novo contato")
    print("2- Listar todos os contatos")
    print("3- Buscar contato")
    print("4- Remover contato")
    print("5- Exportar lista")    
    print("6- Sair do sistema")
    
# ESCOLHA AS OPÇÕES
def escolha_das_opcoes():

    while True:
        
        try:
            escolha = int(input("\nEscolha uma opção: "))
            if escolha == 1:
                adicionar_contato()
            elif escolha == 2:
                listar_contato()
            elif escolha == 3:
                print("teste 3")
            elif escolha == 4:
                print("teste 4")
            elif escolha == 5:
                print("teste 5")
            elif escolha == 6:
                sair_do_programa()
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()
            

# OPÇÃO INVÁLIDA     
def opcao_invalida():
    print("\n⚠️ Opção inválida! Pressione Enter para tentar novamente.")
    input()
    voltar_ao_menu()
    
# TITULOS
def titulos(texto):
    os.system("cls")
    print(texto)
    print()

# VOLTAR AO MENU  
def voltar_ao_menu():
    os.system("cls")
    titulo_projeto()
    opcao_menu()

# SCRIPT VOLTAR
def voltar():
    print("\n⌨️  Pressione [Enter] para voltar ao menu... 🔙")
    input()
    voltar_ao_menu()
        
# SAIR
def sair_do_programa():
    print("\n👋 Saindo do sistema... Até logo!")
    exit()

# VISUALIZAR PROJETO
def visualizar_projeto():            
    titulo_projeto()
    opcao_menu()
    escolha_das_opcoes()

# ADICIONAR CONTATOS
def adicionar_contato():
    titulos("𝑨𝒅𝒊𝒄𝒊𝒐𝒏𝒂𝒓 𝑪𝒐𝒏𝒕𝒂𝒕𝒐")
    
    nome = input("Digite o nome do contato: ")
    telefone = int(input("Digite o telefone: "))
    email = input("Digite o email: ")
    
    contato = {}
    contato["nome:"] = nome
    contato["telefone:"] = telefone
    contato["email:"] = email
    
    lista_de_contatos.append(contato)
        
    print("\n✅ Contato capturado com sucesso!")
    voltar()
    
# LISTAR CONTATOS
def listar_contato():
    titulos("𝑳𝒊𝒔𝒕𝒂 𝒅𝒆 𝑪𝒐𝒏𝒕𝒂𝒕𝒐𝒔")
    
    
    if not lista_de_contatos:
        print("Sua agenda parece um pouco solitária... 👤✨")
        print("Que tal adicionar o primeiro contato para começar a sua rede?")    
    else:
        print(f"Total de conexões salvas: {len(lista_de_contatos)} 📱\n")
        
        for numero, tarefa in enumerate(lista_de_contatos, start=1): 
            print(f"{numero:02d} → {tarefa}") 
            print("--------------------")
    
    voltar()
   
visualizar_projeto()