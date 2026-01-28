import os

lista_de_contatos = []

# TITULO
def titulo_projeto():
    os.system("cls")
    print(("𝑮𝑬𝑹𝑬𝑵𝑪𝑰𝑨𝑫𝑶 𝑫𝑬 𝑪𝑶𝑵𝑻𝑨𝑻𝑶𝑺\n"))    

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
                buscar_contato()
            elif escolha == 4:
                remover_contato()
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
            print(f"{numero:02d} → \n👤 Nome: {tarefa['nome:']}"
                    f"\n📞 Telefone: {tarefa['telefone:']}"
                    f"\n📧 Email: {tarefa['email:']}"
                    f"\n{'-'*30}")    
    voltar()

# BUSCAR CONTATOS
def buscar_contato():
    titulos("𝑩𝒖𝒔𝒄𝒂𝒓 𝑪𝒐𝒏𝒕𝒂𝒕𝒐")
    
    if not lista_de_contatos:
        print("\n🌟 Ops! Parece que sua lista de contatos ainda está em branco. 🏜️")
        print("Que tal adicionar alguém para dar vida a ela? ✨")
        print("-" * 30)
    else:
        
        buscar = input("Digite o nome que deseja buscar: ").lower()
        encontrado = False

        for contato in lista_de_contatos:
            if buscar in contato["nome:"].lower():
                print(
                    f"\n👤 Nome: {contato['nome:']}"
                    f"\n📞 Telefone: {contato['telefone:']}"
                    f"\n📧 Email: {contato['email:']}"
                    f"\n{'-'*30}"
                )
                encontrado = True

        if not encontrado:
            print(f"\n🔍 Ih! Procurei por '{buscar}', mas não encontrei ninguém com esse nome. 🕵️‍♂️")
            print("Verifique se digitou o nome certinho ou tente buscar apenas uma parte dele! ✨")
            print("-" * 35)
                
    voltar()

# REMOVER CONTATO
def remover_contato():
    titulos("𝑹𝒆𝒎𝒐𝒗𝒆𝒓 𝑪𝒐𝒏𝒕𝒂𝒕𝒐")

    if not lista_de_contatos:
        print("\n📭 Nenhum contato para remover.")
        voltar()
        return
    else:
        
        for i, contato in enumerate(lista_de_contatos, start=1):
            print(f"{i}: Nome: {contato['nome:']}")
         
    escolher_removido = input("\nDigite o número do contato que deseja remover: ")
         
    if not escolher_removido:
        print("\n🚫 Digite um número válido!")
        voltar()
        return   
    
    escolher_removido = int(escolher_removido)
    
    if escolher_removido >= 1 and escolher_removido <= len(lista_de_contatos):
        removido = lista_de_contatos.pop(escolher_removido - 1)
        print(f"\n🗑️ Contato '{removido['nome:']}' removido com sucesso!")
    else:
        print("\n🚫 Esse número não existe na lista.")

    voltar()      


visualizar_projeto()