import streamlit as st
import pyrebase
import json

def autenticacao():
    with open('firebase_config.json', 'r') as arquivo:
        config = json.load(arquivo)
    return config

def login():  
    st.title('Bem Vindo a Aplicação de CRUD com Firebase:sunglasses:')  
    firebase =pyrebase.initialize_app(autenticacao())
    auth = firebase.auth()
    db = firebase.database()
    placeholder = st.empty()
    autenticado = False
    perfil = 'login'
    with placeholder.form("login"):
        user = st.text_input('Login')
        pwd  = st.text_input('Senha',type='password')
        btnL = st.form_submit_button('Login')
        if btnL and pwd != '':
            dados = db.child('user').child(user).get()  # busca usuário
            if dados.val():
                dados = dados.val()
                perfil = dados['perfil']
                senha  = dados['senha']
            else:
                perfil = ''
                senha  = ''

            if (senha == pwd) and (perfil == 'admin' or perfil=='user'):
                st.success("Login efetuado com sucesso")
                autenticado = True
                placeholder.empty()
            else:
                st.error("Login ou senha inválida. Por favor Tente Novamente")
    return (autenticado, perfil)