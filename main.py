from Cpf_Cnpj_factory import Documento, DocCpf, DocCnpj
import re
from TelefonesBr import TelefonesBr
from DatasBr import DatasBr
from Acesso_cep import BuscaEndereco
import requests

#Rodando exemplo da factory Cpf/Cnpj
exemplo_cnpj = '35379838000112'
exemplo_cpf = '15316264754'

documento = Documento.cria_documento(exemplo_cpf)
print(documento)

#Rodando exemplo de validação e formatação de um telefone BR
telefone = '7926481234'

fone_objeto = TelefonesBr(telefone)
print(fone_objeto)

#Rodando exemplo de datas por extenso
data = DatasBr()
print(data.mes_cadastro_extenso())
print(data.dia_cadastro_extenso())
print(data.tempo_cadastro())

#Rodando exemplo de buscador de Cep
cep = '49020700'
objeto_cep = BuscaEndereco(cep)
print(objeto_cep.acessa_via_cep())

r = requests.get('https://viacep.com.br/ws/49020700/json/')
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro)
print(cidade)
print(uf)




