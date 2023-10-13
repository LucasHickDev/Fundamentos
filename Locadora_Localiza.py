class Carros:
    def __init__(self,ano,cor,modelo,quilometragem,valor_diario,observacao):
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valor_diario = valor_diario
        self.observação = observacao

class Esportivo(Carros):
    def __init__(self, ano, cor, modelo, quilometragem, valor_diario, observacao, tempo, melhorias):
        super().__init__(ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.tempo = melhorias

class Utilitarios(Carros):
    def __init__(self, ano, cor, modelo, quilometragem, valor_diario, observacao,tamanho_portamalas,quantidade_pessoas,km_por_litro):
        super().__init__(ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.tamanho_portamalas = tamanho_portamalas
        self.quantidade_pessoas = quantidade_pessoas
        self.km_por_litro = km_por_litro

class Reservas:
    def __init__(self, cpf_cliente,data_inicial,data_final,status):
        self.cpf_cliente = cpf_cliente
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.status = status

class Alguem:
    def __init__(self,nome,cpf,idade,endereco,telefone,email):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

class Funcionario(Alguem):
    def __init__(self, nome, cpf, idade, endereco, telefone, email, data_contratado,salario,qts_alugueis, status):
        super().__init__(nome, cpf, idade, endereco, telefone,email)
        self.data_contratado = data_contratado
        self.salario = salario
        self.qts_alugueis = qts_alugueis
        self.status = status
      

class Cliente(Alguem):
    def __init__(self, nome, cpf, idade, endereco, telefone,data_nascimento,numero_cnh,foto_cnh,validade_cnh):
        super().__init__(nome, cpf, idade, endereco, telefone)
        self.data_nascimento = data_nascimento
        self.numero_cnh = numero_cnh
        self.foto_cnh = foto_cnh
        self.validade_cnh = foto_cnh

class Promocao(Cliente): 
    def __init__(self, nome, telefone,email, titulo, descricao, dt_validade) :
        super().__init__(nome,  telefone, email)
        self.titulo = titulo
        self.descricao = descricao
        self.dt_validade = dt_validade