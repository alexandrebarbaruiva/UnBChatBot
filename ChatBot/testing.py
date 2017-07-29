import unittest
import chats
from chats import conversa

class TestTalks(unittest.TestCase):

    # Faz nada, é só para ver se está tudo funcionando
    def test_if_works(self):
        pass

    # Teste dos primeiros diálogos
    def test_ola(self):
        # Olás
        self.assertEqual(conversa('Olá'), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Olá!'), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Olá.'), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Oi'), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Oi!'), 'Olá! Tudo bom?')
        self.assertEqual(conversa('Oi?'), 'Olá! Tudo bom?')

    def test_tudo_bom(self):
        # Tudo bons
        self.assertEqual(conversa('Tudo bom?'), 'Tudo sim, e contigo?')

    def test_bom_dia(self):
        # Bom dias
        # Em breve, estes testes dependerão do horário do dia!
        # Cuidado se eles falharem!
        self.assertEqual(conversa('Bom dia!'), 'Bom dia! Como você está?')

    def test_ola_bom_tudo(self):
        # Multiplos
        self.assertEqual(conversa('Olá Tudo bom?'), 'Olá! Tudo sim, e contigo?')
        self.assertEqual(conversa('Olá! Tudo bom?'), 'Olá! Tudo sim, e contigo?')
        self.assertEqual(conversa('Bom dia! Tudo bom?'), 'Bom dia! Tudo bem, e contigo?')

    def test_inicio_positivo(self):
        self.assertEqual(conversa('Tudo sim, e contigo?'), 'Também! E aí, quais as novidades?')
        self.assertEqual(conversa('Sim, e com você?'), 'Também! E aí, quais as novidades?')

    def test_inicio_negativo(self):
        self.assertEqual(conversa('Não, e vc?'), 'Estou bem, mas o que houve contigo? Quer conversar sobre isso?')

    # def test_brincar(self):
    #     self.assertEqual(conversa('O que você sabe fazer?'), 'Muitas coisas! Conversar, jogar, etc.')
    #     self.assertEqual(conversa('Que jogos?'), 'Adivinhar o número, quer jogar?')


    # def test_iniciador_de_conversas(self):
    #     self.assertEqual()

if __name__ == '__main__':
    unittest.main()
