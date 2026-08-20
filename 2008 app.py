import streamlit as st
import database as db

import base64

db.criar_tabela()

st.title("Site com wallpaper maneiro")
st.header("⭐️⋆౨ৎ˚⟡˖ ࣪☀️")
st.subheader("Formulário fofo")

with st.form("nome_do_formulario"):
    nome = st.text_input("Insira o nome do aluno")
    idade = st.number_input("Insira o idade do aluno", value=50)
    data = st.date_input("Insira a data de nascimento", value="today")
    nota = st.number_input("Insira a nota do aluno", value=0.0, step=0.5, min_value= 0.0, max_value=10.0)
    enviado = st.form_submit_button("Enviar")
    
    # declaramos as variáveis que vão receber os valores que o usuário vai preencher,
    # oq ele vai digitar, oq ele vai clicar, oq ele vai interagir.
    #através do if associado ao botão, a gnt consegue pegar
    # oq o usuário digitou, oq ele clicou, oq ele interagiu, oq ele preencheu e apresentar na tela.

    if enviado:
        msg = db.cadastro_aluno(nome, idade, nota)
        st.warning(msg)

with st.form("form_delete_aluno"):
    id_aluno = st.number_input("ID DO ALUNO!!!!!!", value=0, step=1, min_value=0)
    deletar = st.form_submit_button("Deletar Aluno", 
    help= "Ao cliclar aqui vc deleta o criancinha da escola, e ele vai chorar, e vc vai se sentir mal, mas é a vida, né?")

if deletar:
    msg = db.delete_aluno(id_aluno)
    st.success(msg)


#else: 
    #st.write("Resultado:")
    #st.write(f"Nome: {nome}")
    #st.write(f"Número: {numero}")
    #st.write(f"Data: {data}")
    #st.write(f"Nota: {nota}")  


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://cdn.wallpapersafari.com/46/69/Ib7BH1.jpg");
        background-size: cover;
    }
    """,
    unsafe_allow_html=True,
)

#assim colocamos um wallpaper de fundo no site, oq o usuário vai ver.
