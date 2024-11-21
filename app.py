import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title='',
    page_icon=":dragon:",
    layout="wide",
    initial_sidebar_state="expanded",
)

from _pages import login
from _pages import cliente
from _pages import usuario
from _pages import inicio

sidebar_style = """
    <style>
    .cover-glow {
        width: 100%;
        height: auto;
        padding: 3px;
        box-shadow: 
            0 0 5px #330000,
            0 0 10px #660000,
            0 0 15px #990000,
            0 0 20px #CC0000,
            0 0 25px #FF0000,
            0 0 30px #FF3333,
            0 0 35px #FF6666;
        position: relative;
        z-index: -1;
        border-radius: 30px;  /* Rounded corners */
    }
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    #stDecoration {display:none;}
    /* Oculta a primeira divisão (a linha de separação superior) */
    /*[data-testid="stSidebar"] > div:first-child {
    /*    display: none;
    /*}
    /* Opcional: Oculta a linha de separação e rodapé padrão */
    footer {
        visibility: hidden;
    }
    </style>
    """
st.markdown(sidebar_style, unsafe_allow_html=True)

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
    st.session_state.perfil = 'login'

def main():    
    with st.sidebar:
        if st.session_state.perfil == 'admin':
            mode = option_menu(
                menu_title = 'Opções',
                options = ['Inicio','Clientes','Usuários','Sair'],
                icons = ['house','card-text','people-fill','door-closed'],
                menu_icon = 'cast',
                default_index = 0,
            )
        if st.session_state.perfil == 'user':
            mode = option_menu(
                menu_title = 'Opções',
                options = ['Inicio','Clientes','Sair'],
                icons = ['house','card-text','door-closed'],
                menu_icon = 'cast',
                default_index = 0,
            )

    if mode == 'Inicio':
        inicio.main()

    if mode == 'Sair':
        st.success("Logout efetuado com sucesso")
        st.session_state.clear()
        btnL = st.button('Login')
        if btnL:
            login.login()

    if mode == 'Clientes':
        cliente.main()

    if mode == 'Usuários':
        usuario.main()

if __name__ == '__main__':
    if st.session_state.autenticado == False:
       st.session_state.autenticado, st.session_state.perfil = login.login()
    if st.session_state.autenticado == True:
        main()
