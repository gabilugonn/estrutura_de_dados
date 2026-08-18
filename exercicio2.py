from collections import deque

# Prioridade: quanto maior o número, maior a prioridade
PRIORIDADE = {"alta": 3, "media": 2, "baixa": 1}

fila_prioridade = []   # lista de processos aguardando (nome, prioridade)
executados = []        # processos que já executaram
finalizados = []       # processos que finalizaram
suspensos = []         # processos suspensos
em_execucao = None     # processo atualmente executando


def entrar_processo(nome, prioridade):
    fila_prioridade.append((nome, prioridade))


def ordenar_fila():
    # Ordena por prioridade (maior primeiro); mantém ordem de chegada (estável)
    fila_prioridade.sort(key=lambda p: PRIORIDADE[p[1]], reverse=True)


def iniciar_proximo():
    global em_execucao
    ordenar_fila()
    if fila_prioridade:
        em_execucao = fila_prioridade.pop(0)
        executados.append(em_execucao[0])
        print(f"Executando: {em_execucao[0]}")


def suspender(nome):
    global fila_prioridade
    fila_prioridade = [p for p in fila_prioridade if p[0] != nome]
    suspensos.append(nome)
    print(f"{nome} suspenso")


def finalizar_execucao():
    global em_execucao
    if em_execucao:
        finalizados.append(em_execucao[0])
        print(f"{em_execucao[0]} finalizado")
        em_execucao = None


# Simulação dos eventos 

# 1) Entram A(baixa), B(média), C(alta)
entrar_processo("A", "baixa")
entrar_processo("B", "media")
entrar_processo("C", "alta")

# 2) O primeiro processo começa a executar
iniciar_proximo()

# 3) Entram D(média), E(média), F(baixa)
entrar_processo("D", "media")
entrar_processo("E", "media")
entrar_processo("F", "baixa")

# 4) B é suspenso
suspender("B")

# 5) O processo em execução finaliza
finalizar_execucao()

# 6) O próximo processo começa a executar
iniciar_proximo()

# 7) Esse processo finaliza
finalizar_execucao()

# Resultado 
print("\n--- RESULTADO ---")
print("Executados:", executados)
print("Fila de prioridade final:", [p[0] for p in fila_prioridade])
print("Fila de finalizados:", finalizados)
print("Suspensos:", suspensos)
