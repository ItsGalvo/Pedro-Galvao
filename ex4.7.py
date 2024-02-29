import re

def limpar_valor(valor):
    novo_valor = re.sub(r'[^a-zA-Z0-9]', '', valor)
    if novo_valor != valor:
        print(f"O valor '{valor}' foi modificado para '{novo_valor}'")
    return novo_valor

nome_usuario = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")

nome_usuario_limpo = limpar_valor(nome_usuario)
senha_limpa = limpar_valor(senha)

print("\nNome de usuário limpo:", nome_usuario_limpo)
print("Senha limpa:", senha_limpa)
