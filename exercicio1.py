class FilaCircular:
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self.queue = [None] * capacidade
        self.head = 0
        self.tail = 0
        self.size = 0
        self.momento_volta = None

    def enqueue(self, item):
        if self.size == self.capacidade:
            print(f"Fila cheia! Não foi possível inserir {item}")
            return
        
        self.queue[self.tail] = item
        antigo_tail = self.tail
        self.tail = (self.tail + 1) % self.capacidade
        self.size += 1
        
        # Identifica se o ponteiro voltou para o início do array fixo
        if self.tail < antigo_tail:
            self.momento_volta = f"enqueue({item}) fez o tail voltar para a posição {self.tail}"

    def dequeue(self):
        if self.size == 0:
            print("Fila vazia!")
            return None
        
        item = self.queue[self.head]
        self.head = (self.head + 1) % self.capacidade
        self.size -= 1
        return item

# Executando o enunciado
fila = FilaCircular(capacidade=5)

# 1. Enqueue de A até D
for letra in ['A', 'B', 'C', 'D']:
    fila.enqueue(letra)
    
# 2. Dois dequeues
fila.dequeue()
fila.dequeue()

# 3. Três enqueues com E, F, G
for letter in ['E', 'F', 'G']:
    fila.enqueue(letter)

# Exibição dos resultados solicitados
print(f"Vetor final: {fila.queue}")
print(f"Head atual:  {fila.head}")
print(f"Tail atual:  {fila.tail}")
print(f"Size atual:  {fila.size}")
print(f"Momento da volta: {fila.momento_volta}")



