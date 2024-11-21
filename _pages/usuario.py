import streamlit as st
from _pages import login
import pyrebase
import pandas as pd
from collections import Counter

def incluir():
    firebase =pyrebase.initialize_app(login.autenticacao())
    auth = firebase.auth()
    db = firebase.database()
    placeholder = st.empty()

    form = st.form(key='usuarios', clear_on_submit=True) 
    with form:
        user= st.text_input('Login')
        pwd = st.text_input('Senha',type='password')
        perfis = ['admin','user']
        perfil  = st.selectbox('Selecione o perfil: ',perfis)
        col1, col2 = st.columns(2)
        with col1:
            btn = st.form_submit_button('Incluir',type='primary')
        with col2:            
            clear = st.form_submit_button('Limpar')
        if btn and pwd != '':
            #cadastrar novo usuario
            dadosGravar = {"senha":"","perfil":""}
            dadosGravar['senha'] = pwd
            dadosGravar['perfil'] = perfil
            if db.child('user').child(user).get().val():  # busca usuário
                st.success('Usuário já cadastrado!')
            else:
                with st.spinner('Gravando......'):  
                    db.child('user').child(user).set(dadosGravar)
                st.success('Gravado com Sucesso!!!')
        if clear:
            user = ''


def consultar():
    firebase =pyrebase.initialize_app(login.autenticacao())
    auth = firebase.auth()
    db = firebase.database()
    placeholder = st.empty()
    st.divider()
    dados = db.child('user').get()

    df = pd.DataFrame.from_dict(dict(dados.val()))
    st.table(df)

def alterar():
    firebase =pyrebase.initialize_app(login.autenticacao())
    auth = firebase.auth()
    db = firebase.database()
    placeholder = st.empty()

    form = st.form(key='usuarios', clear_on_submit=True) 
    with form:
        user= st.text_input('Login')
        pwd = st.text_input('Senha',type='password')
        col1, col2 = st.columns(2)
        with col1:
            btn = st.form_submit_button('Alterar',type='primary')
        with col2:            
            clear = st.form_submit_button('Limpar')
        if btn and user != '':
            if db.child('user').child(user).get().val():  # busca usuário
                db.child('user').child(user).update({'senha':pwd})
                st.success('Senha alterada com sucesso!')
            else:
                st.success('Usuário não cadastrado!')

def excluir():
    firebase =pyrebase.initialize_app(login.autenticacao())
    auth = firebase.auth()
    db = firebase.database()
    placeholder = st.empty()

    form = st.form(key='usuarios', clear_on_submit=True) 
    with form:
        user= st.text_input('Login')
        pwd = st.text_input('Senha',type='password')
        col1, col2 = st.columns(2)
        with col1:
            btn = st.form_submit_button('Excluir',type='primary')
        with col2:            
            clear = st.form_submit_button('Limpar')
        if btn and user != '':
            dados = db.child('user').child(user).get()  # busca usuário
            if dados.val():
                dados = dados.val()
                perfil = dados['perfil']
                senha  = dados['senha']
            else:
                perfil = ''
                senha  = ''

            if senha == pwd:
                db.child('user').child(user).remove()
                st.success("Excluído com sucesso")
            else:
                st.error("Login ou senha inválida. Por favor Tente Novamente")


def main():
    st.title('Cadastro de Usuários :family:')  

    st.header('O que deseja fazer?')
    option = st.radio('',['Incluir', 'Consultar', 'Alterar', 'Excluir']) 
    
    if option == 'Incluir':
        incluir()

    if option == 'Consultar':
        consultar()        

    if option == 'Alterar':
        alterar()                

    if option == 'Excluir':
        excluir()                        