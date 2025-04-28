import unittest
import bcrypt

class TestPasswordHashing(unittest.TestCase):
    def test_password_hashing(self):
        senha = "senha123"
        hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        self.assertTrue(bcrypt.checkpw(senha.encode('utf-8'), hashed_senha))

    def test_password_storage(self):
        # Simule o armazenamento no banco e verifique se o hash é gerado
        senha = "senha123"
        hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        self.assertNotEqual(senha, hashed_senha.decode('utf-8'))  # A senha não deve ser armazenada em texto puro

if __name__ == '__main__':
    unittest.main()