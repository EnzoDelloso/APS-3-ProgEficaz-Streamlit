import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv('acesso.cred')

mongo = os.getenv('DB_LINK')

client = MongoClient(mongo)
db = client["prog_eficaz"]
collection = db["recursos"]

#codigo para implementar junto com o backend quando tiver pronto

# collection_user = db['usuarios']
# collection_bike = db['bicicletas']
# collection_emprestimo = db['emprestimos']

# def add_user(nome, cpf, data_nascimento)
#     collection_user.insert_one({'nome' : nome, 'cpf' : cpf, 'data_nascimento' : data_nascimento})

# def add_bike(marca, modelo, cidade):
#     collection_bike.insert_one({'marca' : marca, 'modelo' : modelo, 'cidade' : cidade})

# def add_emprestimo(user_id, bike_id, data_regitro):
#     collection_emprestimo.insert_one({'user_id' : user_id, 'bike_id' : bike_id, 'data_registro' : data_regitro})

# def remove_user(nome, cpf, data_nascimento)
#     collection_user.delete_one({'nome' : nome, 'cpf' : cpf, 'data_nascimento' : data_nascimento})

# def remove_bike(marca, modelo, cidade):
#     collection_bike.delete_one({'marca' : marca, 'modelo' : modelo, 'cidade' : cidade})

# def remove_emprestimo(user_id, bike_id, data_regitro):
#     collection_emprestimo.delete_one({'user_id' : user_id, 'bike_id' : bike_id, 'data_registro' : data_regitro})

def add_resource(name):
    collection.insert_one({"name": name})

def remove_resource(name):
    collection.delete_one({"name": name})

st.title("Gerenciador de Recursos")

st.header("Adicionar Recurso")
new_resource = st.text_input("Nome do Recurso")
if st.button("Adicionar"):
    if new_resource:
        add_resource(new_resource)
        st.success(f'Recurso "{new_resource}" adicionado!')
    else:
        st.error("Por favor, insira um nome válido.")

st.header("Remover Recurso")
resources = [doc["name"] for doc in collection.find()]
remove_resource_name = st.selectbox("Selecione um Recurso", resources)
if st.button("Remover"):
    remove_resource(remove_resource_name)
    st.success(f'Recurso "{remove_resource_name}" removido!')

st.header("Recursos Atuais")
if resources:
    st.write(resources)
else:
    st.write("Nenhum recurso disponível.")