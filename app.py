import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv('acesso.cred')

mongo = os.getenv('DB_LINK')

client = MongoClient(mongo)
db = client["prog_eficaz"]

collection_user = db['usuarios']
collection_bike = db['bicicletas']
collection_emprestimo = db['emprestimos']


def add_user(nome, cpf, data_nascimento):
    collection_user.insert_one({'nome': nome, 'cpf': cpf, 'data_nascimento': data_nascimento})

def remove_user(cpf):
    collection_user.delete_one({'cpf': cpf})

def update_user(cpf, novo_nome, nova_data_nascimento):
    collection_user.update_one({'cpf': cpf}, {'$set': {'nome': novo_nome, 'data_nascimento': nova_data_nascimento}})

def add_bike(marca, modelo, cidade, em_uso):
    collection_bike.insert_one({'marca': marca, 'modelo': modelo, 'cidade': cidade, 'em_uso' : em_uso})

def remove_bike(marca, modelo):
    collection_bike.delete_one({'marca': marca, 'modelo': modelo})

def update_bike(marca, modelo, nova_cidade):
    collection_bike.update_one({'marca': marca, 'modelo': modelo}, {'$set': {'cidade': nova_cidade}})


def add_emprestimo(id_usuario, id_bike, data):
    collection_emprestimo.insert_one({'id_usuario': id_usuario, 'id_bike': id_bike, 'data': data})

def remove_emprestimo(id_usuario, id_bike):
    collection_emprestimo.delete_one({'id_usuario': id_usuario, 'id_bike': id_bike})

st.header("Usuários")
with st.expander("Adicionar Usuário"):
    nome = st.text_input("Nome")
    cpf = st.text_input("CPF")
    data_nascimento = st.text_input("Data de Nascimento")
    if st.button("Adicionar Usuário"):
        add_user(nome, cpf, data_nascimento)
        st.success(f'Usuário adicionado!')

with st.expander("Remover Usuário"):
    cpf_usuario = st.text_input("User CPF")
    if st.button("Remover Usuário"):
        remove_user(cpf_usuario)
        st.success(f'Usuário removido!')

with st.expander("Atualizar Usuário"):
    novo_cpf = st.text_input("CPF Usuário")
    novo_nome = st.text_input("Novo Nome")
    nova_data_nascimento = st.text_input("Nova Data de Nascimento")
    if st.button("Atualizar Usuário"):
        update_user(novo_cpf, novo_nome, nova_data_nascimento)
        st.success('Usuário atualizado!')

# Gerenciamento de Bicicletas
st.header("Bicicletas")
with st.expander("Adicionar Bicicleta"):
    marca = st.text_input("Marca da Bicicleta")
    modelo = st.text_input("Modelo da Bicicleta")
    cidade = st.text_input("Cidade")
    em_uso = st.selectbox("Bicicleta em uso", [True, False])

    if st.button("Adicionar Bicicleta"):
        add_bike(marca, modelo, cidade, em_uso)
        st.success(f'Bicicleta "{marca} {modelo}" adicionada!')

with st.expander("Remover Bicicleta"):
    marca_bike = st.text_input("Marca Bicicleta")
    modelo_bike = st.text_input("Modelo Bicicleta")
    if st.button("Remover Bicicleta"):
        remove_bike(marca_bike, modelo_bike)
        st.success(f'Bicicleta "{marca_bike} {modelo_bike}" removida!')

with st.expander("Atualizar Bicicleta"):
    nova_marca = st.text_input("Marca da Bike")
    novo_modelo = st.text_input("Modelo da Bike")
    nova_cidade = st.text_input("Nova Cidade")
    novo_status = st.selectbox("Novo Status", ["Disponível", "Em uso"])
    if st.button("Atualizar Bicicleta"):
        update_bike(nova_marca, novo_modelo, nova_cidade, novo_status)
        st.success('Bicicleta atualizada!')

st.header("Empréstimos")
with st.expander("Adicionar Empréstimo"):
    id_usuario = st.text_input("ID do Usuário")
    id_bike = st.text_input("ID da Bicicleta")
    data = st.text_input("Data do Registro")
    if st.button("Adicionar Empréstimo"):
        add_emprestimo(id_usuario, id_bike, data)
        st.success('Empréstimo adicionado!')

with st.expander("Remover Empréstimo"):
    id_usuario = st.text_input("ID Usuário")
    id_bike = st.text_input("ID Bicicleta")
    if st.button("Remover Empréstimo"):
        remove_emprestimo(id_usuario, id_bike)
        st.success('Empréstimo removido!')

st.header("Visualizar dados")
if st.button("Visualizar Usuários"):
    usuarios = collection_user.find()
    st.write(list(usuarios))

if st.button("Visualizar Bicicletas"):
    bicicletas = collection_bike.find()
    st.write(list(bicicletas))

if st.button("Visualizar Empréstimos"):
    emprestimos = collection_emprestimo.find()
    st.write(list(emprestimos))
