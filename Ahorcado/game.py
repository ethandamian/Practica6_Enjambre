import random

# Lista de palabras para el juego
word_list = ['python', 'network', 'socket', 'client', 'server', 'variable', 'function', 'method', 
    'class', 'object', 'attribute', 'constructor', 'inheritance', 'polymorphism', 
    'encapsulation', 'abstraction', 'algorithm', 'recursion', 'iteration', 'loop', 
    'condition', 'exception', 'try', 'except', 'finally', 'file', 'input', 'output', 
    'array', 'list', 'tuple', 'dictionary', 'set', 'stack', 'queue', 'thread', 
    'process', 'multithreading', 'concurrency', 'parallelism', 'synchronization', 
    'deadlock', 'resource', 'memory', 'heap', 'stack', 'pointer', 'reference', 
    'garbage', 'collection', 'optimization', 'complexity', 'big', 'data', 'machine', 
    'learning', 'artificial', 'intelligence', 'neural', 'network', 'tree', 'graph', 
    'node', 'edge', 'vertex', 'depth', 'breadth', 'search', 'binary', 'heap', 
    'merge', 'sort', 'quick', 'bubble', 'selection', 'insertion', 'hash', 'hashmap', 
    'cryptography', 'cipher', 'encryption', 'decryption', 'plaintext', 'ciphertext', 
    'authentication', 'authorization', 'token', 'session', 'cookie', 'protocol', 
    'ip', 'address', 'packet', 'firewall', 'router', 'switch', 'database', 'query', 
    'sql', 'nosql', 'orm', 'api', 'rest', 'graphql', 'json', 'xml', 'html', 'css']

class HangmanGame:
    def __init__(self):
        self.word = random.choice(word_list)  # Palabra que se debe adivinar
        self.word_display = ["_" for _ in self.word]  # Estado de la palabra
        self.incorrect_letters = []
        self.tries_left = 10
        self.terminated = False
        self.won = False

    # Verificar la letra ingresada
    def guess(self, letter):
        if letter in self.word:
            for i, l in enumerate(self.word):
                if l == letter:
                    self.word_display[i] = letter
        else:
            if letter not in self.incorrect_letters:
                self.incorrect_letters.append(letter)
                self.tries_left -= 1

        if self.has_won():
            self.terminated = True
            self.won = True
        elif self.tries_left <= 0:
            self.terminated = True

    # Verificar si el jugador ha ganado
    def has_won(self):
        return "_" not in self.word_display

    # Verificar si el jugador ha perdido
    def has_lost(self):
        return self.tries_left <= 0
    
    # Reiniciar el juego
    def reset(self):
        self.word = random.choice(word_list)
        self.word_display = ["_" for _ in self.word]
        self.incorrect_letters = []
        self.tries_left = 10
        self.terminated = False
        self.won = False