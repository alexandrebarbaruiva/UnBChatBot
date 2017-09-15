"""
Modulo responsavel pela interacao com o banco de dados.
TODO: Melhorar a documentacao
"""
import os
import sqlite3


class DAO():
    """Objeto responsavel por manipular o banco de dados."""
    def __init__(self, database_path="chatbot.db"):
        self._database_path = database_path
        self._is_connected = False
        if not os.path.exists(database_path):
            print('Banco de dados nao encontrado.')
            print('Deseja (re)criar um novo banco?(y/n)')
            ans = input().lower()
            if ans.startswith('y'):
                self.create_new_bank()

    def __connect(self):
        """Faz a conexao com o db"""
        if not self._is_connected:
            self._conn = sqlite3.connect(self._database_path)
            self._cursor = self._conn.cursor()
            self._is_connected = True

    def __close(self):
        """Commita novas mudancas e fecha conexao com o db"""
        if self._is_connected:
            self._conn.commit()
            self._conn.close()
            self._is_connected = False

    def create_new_bank(self):
        """
        Cria um novo banco de dados baseado
        em um script passado pelo usuario
        """
        script = input(
            'Digite o nome do arquivo contendo o script de criacao do banco: ')
        while not os.path.exists(script):
            script = input('Arquivo nao encontrado, favor digitar novamente: ')
        self._database_path = input('Digite o nome do arquivo do novo banco: ')
        self.__connect()
        with open(script, 'r') as f:
            self._cursor.executescript(f.read())
        self.__close()
        print('Banco de dados criado com sucesso')

    def execute(self, query, params=()):
        """
        Executa uma query e retorna o resultado. Trata excecoes
        causadas pelo sqlite imprimindo os erros para o console.
        """
        self.__connect()
        try:
            self._cursor.execute(query, params)
        except sqlite3.Error as e:
            print('Ocorreu um erro durante a execucao da query', query)
            print('Mensagem do erro:', e)
        finally:
            data = self._cursor.fetchall()
            self.__close()
        return data


class DataHandler():
    """Faz a interacao com o banco de dados de uma maneira mais especifica."""
    def __init__(self):
        self._bd = DAO()

    def get_user_by_id(self, telegram_id):
        """Retorna os dados do usuario baseado no seu ID"""
        data = self._bd.execute(
            'SELECT * FROM USUARIO WHERE TELEGRAM_ID = ?;', (int(telegram_id),)
            )
        return data

    def get_user_message_history(self, telegram_id):
        """Retorna uma lista contendo todas a mensagens de um usuario"""
        data = self._bd.execute(
            """ SELECT TEXTO FROM MENSAGEM JOIN USUARIO
            ON USUARIO.TELEGRAM_ID = MENSAGEM.USUARIO WHERE TELEGRAM_ID = ?;
            """, (int(telegram_id),)
            )
        return data

    def store_new_user(self, telegram_id, name=''):
        """Guarda as informacoes de um novo usuario no BD"""
        self._bd.execute(
            """INSERT INTO USUARIO(TELEGRAM_ID, NOME)
               VALUES(?, ?)""", (int(telegram_id), str(name))
            )

    def store_new_message(self, telegram_id, text):
        """Guarda uma nova mensagem de texto de um usuario"""
        self._bd.execute(
            """INSERT INTO MENSAGEM(NUMERO, TEXTO, USUARIO)
               VALUES(NULL, ?, ?)""", (str(text), int(telegram_id))
            )

    # TODO: Pegar historia de mensagens a partir de uma certa data


if __name__ == '__main__':
    """Cria um novo banco de dados quando executado"""
    print('Um novo banco de dados sera criado, deseja continuar? (y/n)')
    ans = input().lower()
    if ans.startswith('y'):
        a = DAO()
        a.create_new_bank()