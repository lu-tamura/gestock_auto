#Crie uma função soma(a, b) que retorna a soma de a e b.



def soma(a,b):

    return a+b

#---------------------------------------------------------

#Crie uma função eh_par(n) que retorna True se n for par e False caso contrário.

def eh_par(n):
    if n%2 == 0:
        
        return True
    else:
        return False
    
#---------------------------------------------------------

#Crie uma função fatorial(n) que retorna o fatorial de n.

def fatorial(n):
    if n < 0:
        raise ValueError
    elif n== 0 or n == 1:
        return 1
    else:
        resultado= 1
        for i in range(1,n +1):
            resultado *= i
        return resultado

#---------------------------------------------------------

#criar uma função para cadastro de usuario
#ter uma array para armazenar os objetos contendo os dados dos usuarios, 
#esse objeto deve ter os campos nome e email e nao pode cadastrar o mesmo email 2 vezes

usuarios= []

def cadastrar_usuario(nome, email):
    
    novo_usuario= {
        "nome": nome,
        "email": email
    }

    for usuario in usuarios:
        if usuario["email"] == email:
            return "Erro: O e-mail já está cadastrado."

    usuarios.append(novo_usuario)
    return "sucesso"



#controller

def cadastro(nome,cpf):
    new_user = {
        "nome": nome,
        "cpf": cpf
    }
    return save(new_user)

#service
def save(new_user):
    if new_user['nome'] and new_user['cpf']:
        return True #salvo no BD
    return False #erro ao salvar no BD

# ---------------------------------------- exercícios ----------------------------------------  

#1
def welcome(email):
    if email:
        reposta= send_mail(email)
        if reposta:
            return "email de boas-vindas enviado"
        return "erro de provedor de email"

def send_mail(email):
    return True


#2
def agendamento(tarefa, horario):
    nova_tarefa = {
        "tarefa": tarefa,
        "horario": horario
    }
    return save_tarefa(nova_tarefa)

def save_tarefa(nova_tarefa):
    if nova_tarefa['tarefa'] and nova_tarefa['horario']:
        return True  # salvo no BD
    return False  # erro ao salvar no BD


#3
def enviar_sms(sms):
    if len(sms) != 11:
        return "Erro: O número de telefone deve ter 11 caracteres."
    if sms:
        resposta = send_sms(sms)
        if resposta:
            return "sms enviado"
        return "erro ao enviar sms"
    
    return "Erro: Nenhum número fornecido."

def send_sms(sms):
    return True

#4


usuarios2 = []

def cadastro_usuario_sms_func(nome, email, numero):
    return cadastro_sms_enviar(nome, email, numero)

def cadastro_sms_enviar(nome, email, numero):
    
    for usuario in usuarios2:
        if usuario["email"] == email:
            return "Erro: O e-mail já está cadastrado."
        
        
        if len(usuario["numero"]) != 11:
            return "Erro: O número de telefone deve ter 11 caracteres."
    
    
    novo_usuario = {
        "nome": nome,
        "email": email,
        "numero": numero
    }
    
    
    usuarios2.append(novo_usuario)
    
    
    
    
    resposta = send_sms_usuario(numero)
    
    if resposta:
        return "Cadastro realizado e SMS enviado."
    else:
        return "Cadastro realizado, mas erro ao enviar SMS."

def send_sms_usuario(numero):
    return True
