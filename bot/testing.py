import unittest
import chats
from chats import conversa

idTest = 11111

class TestTalks(unittest.TestCase):
    

    # Faz nada, é só para ver se está tudo funcionando
    def test_if_works(self):
        def test_nesting(self):
            pass
        pass

    # Teste dos primeiros diálogos
    def test_ola(self):
        # Olás
        self.assertEqual(conversa('Olá',idTest), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Olá!',idTest), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Olá.',idTest), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Oi',idTest), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Oi!',idTest), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Oi?',idTest), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Hello?',idTest), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Hello!',idTest), 'Olá! Tudo bom?')

    def test_tudo_bom(self):
        # Tudo bons
        self.assertEqual(conversa('Tudo bom?',idTest), 'Tudo sim, e contigo?')
        self.assertEqual(conversa('Como você está?',idTest), 'Estou bem, e você?')

    def test_bom_dia(self):
        # Bom dias
        # Em breve, estes testes dependerão do horário do dia!
        # Cuidado se eles falharem!
        self.assertEqual(conversa('Bom dia!',idTest), 'Bom dia! Como você está?')
        # self.assertEqual(conversa('Boa tarde!',idTest), 'Boa tarde! Como você está?')
        # self.assertEqual(conversa('Boa noite!',idTest), 'Boa noite! Como você está?')

    def test_ola_bom_tudo(self):
        # Combinação de olá/bom dia com tudo bom
        self.assertEqual(conversa('Olá Tudo bom?',idTest), 'Olá! Tudo sim, e contigo?')
        self.assertEqual(conversa('Olá! Tudo bom?',idTest), 'Olá! Tudo sim, e contigo?')
        self.assertEqual(conversa('Bom dia! Tudo bom?',idTest), 'Bom dia! Tudo bem, e contigo?')

    def test_inicio_positivo(self):
        # Resposta positiva de tudo bom com pergunta pra iniciar conversa
        self.assertEqual(conversa('Tudo sim, e contigo?',idTest), 'Também! E aí, quais as novidades?')
        self.assertEqual(conversa('Tudo, e contigo?',idTest), 'Também! E aí, quais as novidades?')
        self.assertEqual(conversa('Tudo, e você?',idTest), 'Também! E aí, quais as novidades?')
        self.assertEqual(conversa('Sim, e com você?',idTest), 'Também! E aí, quais as novidades?')
        self.assertEqual(conversa('Sim',idTest), 'Nossa, obrigado por perguntar se eu tô bem. Quais as novidades?')

    def test_inicio_negativo(self):
        # Resposta negativa de tudo bom com pergunta pra iniciar conversa
        self.assertEqual(conversa('Não, e vc?',idTest), 'Estou bem, mas o que houve contigo? Quer conversar sobre isso?')
        self.assertEqual(conversa('Não, e você?',idTest), 'Estou bem, mas o que houve contigo? Quer conversar sobre isso?')
        self.assertEqual(conversa('Não',idTest), 'O que houve? Quer conversar sobre isso?')
        
    def test_dialogo_desabafo(self):
        # self.assertEqual(conversa(''), 'Que?')
        def test_morte_familia(self):
            self.assertEqual(conversa('Perdi um familiar.',idTest), '')
            
        def test_problema_familiar(self):
            self.assertEqual(conversa('Tenho um familiar com problemas',idTest), 'Que?')
            
        def test_problema_academico(self):
            self.assertEqual(conversa('Meu IRA tá negativo D:',idTest))
            self.assertEqual(conversa('Meu IRA está baixo D:',idTest))
            self.assertEqual(conversa('Não estou aguentando a rotina da UnB',idTest))
            
        def test_problema_financeiro(self):
            self.assertEqual(conversa('Estou com problemas financeiros',idTest))
            self.assertEqual(conversa('Não consigo pagar minhas contas',idTest))
            self.assertEqual(conversa('Fui demitido do estágio',idTest))
        
    def test_final_dialogo(self):
        self.assertEqual(conversa('Preciso ir',idTest), 'Ok, foi bom conversar com você!')
        self.assertEqual(conversa('Tchau',idTest), 'Até mais!')
        self.assertEqual(conversa('Bye',idTest), 'Até mais!')
    
    # TESTAR MAIS TARDE
    # def test_brincar(self):
    #     self.assertEqual(conversa('O que você sabe fazer?',idTest), 'Muitas coisas! Conversar, jogar, etc.')
    #     self.assertEqual(conversa('Que jogos?',idTest), 'Adivinhar o número, quer jogar?')
    #     self.assertEqual(conversa('Sim!',idTest), 'Adivinhe um número entre 1 e 100')
    #
    # def test_chat_negativo(self):
    #     self.assertEqual(conversa('Ando tão triste ultimamente',idTest), 'O que houve? Quer conversar?')
    #     self.assertEqual(conversa('Não estou conseguindo estudar direito :(',idTest), 'Poxa :( Você sabe o motivo de você não conseguir estudar direito?')
    #     self.assertEqual(conversa('Não...',idTest), 'Você quer ajuda? Posso te indicar umas ferramentas...')
    #     self.assertEqual(conversa('Quais ferramentas vc me indica?',idTest), 'Já ouviu falar no trello? Ou Wunderlist?')
    #
    # def test_chat_positivo(self):
    #     self.assertEqual(conversa('Meu dia foi muito bom',idTest),'Que bom! Me conte como foi')
    #     self.assertEqual(conversa('Estou feliz',idTest),'Maravilha! Compartilhe essa felicidade comigo')
    #     self.assertEqual(conversa('',idTest),'')

    # def test_conversa_inteira(self):
    #     self.assertEqual(conversa('oi',idTest), 'Olá! Tudo bom?')
    #     self.assertEqual(conversa('d boa, e tu?',idTest), 'Também! E aí, quais as novidades?')
    #     self.assertEqual(conversa('nada d mais, só entendiado',idTest), 'Te entendo, também estou cansado de uns e zeros... De qualquer forma, quer conversar sobre alguma coisa específica?')
    #     self.assertEqual(conversa('sim, eu to puto com o meu gato, ele mijou nas minhas coisas!',idTest), 'Eita! Mas gatos costumam fazer isso, não?')


if __name__ == '__main__':
    unittest.main()
