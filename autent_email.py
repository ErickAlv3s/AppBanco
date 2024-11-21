import pyrebase
import json
import os



def autenticacao():
    caminho_arquivo = os.path.join(
        os.path.dirname(__file__), 'firebase_config.json')
    with open(caminho_arquivo, 'r') as arquivo:
        config = json.load(arquivo)
    return config


def incluir_novo_user():
    user = input('Nome do usuário: ')
    senha = input('Senha: ')
    dadosGravar = {"senha": "", "perfil": ""}
    dadosGravar['senha'] = senha
    dadosGravar['perfil'] = user
    db.child('user').child(user).set(dadosGravar)
    print('Cadastro realizado!!!')


if __name__ == '__main__':
    firebase = pyrebase.initialize_app(autenticacao())
    auth = firebase.auth()
    db = firebase.database()
    email = input('Entre com o e-mail: ')
    senha = input('Entre com a senha: ')
    try:
        # print(auth.sign_in_with_email_and_password(email,senha))
        auth.sign_in_with_email_and_password(email, senha)
        print('Login realizado com sucesso')
        opc = input('Deseja incluir usuário no banco? (S/N) ')
        if opc.upper() == 'S':
            incluir_novo_user()
    except:
        print('Senha invalida')

# para adicionar e-mail no cadastro
# auth.create_user_with_email_and_password(email,senha)
