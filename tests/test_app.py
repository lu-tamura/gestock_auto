import unittest
from unittest.mock import patch
from src.app import soma, eh_par, fatorial, cadastrar_usuario, cadastro, welcome, agendamento, enviar_sms, cadastro_usuario_sms_func
class TestApp(unittest.TestCase):
    
    def test_soma_numeros_positivos(self):
        resultado= soma(2,5)
        self.assertEqual(resultado, 7)



    def test_soma_numeros_negativos(self):
        resultado= soma (-1, -2)
        self.assertEqual(resultado, -3)

    def test_soma_numeros_zero(self):
        resultado= soma (0,0)
        self.assertEqual(resultado, 0)

#-------------------------------------------------

    def test_eh_par_positivo(self):
        resultado= eh_par(4)
        self.assertTrue(resultado, True)

    def test_eh_par_negativo(self):
        resultado= eh_par(-4)
        self.assertTrue(resultado, True)

    def test_eh_par_zero(self):
        resultado= eh_par(0)
        self.assertTrue(resultado, True)

    def test_eh_par_impar(self):
        resultado= eh_par(3)
        self.assertFalse(resultado, False)


#-------------------------------------------------

    def test_fatorial_positivo(self):
        resultado= fatorial(5)
        self.assertEqual(resultado, 120)

    def test_fatorial_zero(self):
        resultado= fatorial(0)
        self.assertEqual(resultado, 1)

    def test_fatorial_um(self):
        resultado= fatorial(1)
        self.assertEqual(resultado, 1)

    def test_fatorial_negativo(self):
        with self.assertRaises(ValueError):
            fatorial(-2) 

#------------------------------------------------

    def test_cadastrar_usuario_ok(self):
        resultado= cadastrar_usuario('louie', 'louie@gmail.com' )
        self.assertEqual(resultado, "sucesso")

    def test_cadastrar_usuario_erro(self):
        cadastrar_usuario('ivane', 'ivane@gmail.com')
        resultado= cadastrar_usuario('vivana', 'ivane@gmail.com')
        self.assertEqual(resultado, "Erro: O e-mail já está cadastrado.")

    @patch("src.app.save", return_value = "ola")
    def test_cadastrar_usuario_valido(self, mock_salvar):
        nome = "Carlos"
        cpf= "213471283"
        resultado= cadastro(nome,cpf)
        self.assertTrue(resultado)
        mock_salvar.assert_called_once_with({'nome': nome, 'cpf':cpf})

#------------------------------------------------

#exercícios valendo 0.5

#1
    
    @patch("src.app.send_mail", return_value = "True")
    def test_enviar_email(self, mock_salvar):
        resultado= welcome("louiee@gmail.com")
        self.assertEqual(resultado, "email de boas-vindas enviado")
        mock_salvar.assert_called_once_with("louiee@gmail.com")



#2
    @patch("src.app.save_tarefa", return_value=True)  # Mocka a função save_tarefa, não agendamento
    def test_agendar_tarefa(self, mock_salvar):
        tarefa = "Violão"
        horario = "21:00"
        
        compromisso = agendamento(tarefa, horario)
        
        # Verificando se o resultado da função agendamento é True
        self.assertTrue(compromisso)
        
        # Verificando se a função save_tarefa foi chamada com os parâmetros esperados
        mock_salvar.assert_called_once_with({'tarefa': tarefa, 'horario': horario})


#3

    @patch("src.app.send_sms", return_value = "True")
    def test_enviar_sms(self, mock_salvar):
        resultado= enviar_sms("11994099422")
        self.assertEqual(resultado, "sms enviado")
        mock_salvar.assert_called_once_with("11994099422")


#4 
    
    @patch("src.app.cadastro_sms_enviar", return_value="Cadastro realizado e SMS enviado.")  
    def test_cadastrar_usuario_sms_ok(self, mock_cadastro):
       
        resultado = cadastro_usuario_sms_func('louie', 'louie@gmail.com', '11994099422')

        
        self.assertEqual(resultado, "Cadastro realizado e SMS enviado.")

        
        mock_cadastro.assert_called_once_with('louie', 'louie@gmail.com', '11994099422')


if __name__ == '__main__':
    unittest.main()







#------------------------------------------------

    





#essa parte aqui pega o módulo principal