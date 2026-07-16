db_chamados = {}

def gerar_novo_id():
    if not db_chamados:
        return 1
    return max(db_chamados.keys()) + 1

def salvar_chamado(chamado):
    if not chamado.status:
        chamado.status = "Aberto"
    db_chamados[chamado.id] = chamado
    return True

def buscar_chamado(id_chamado):
    return db_chamados.get(id_chamado)

def listar_todos():
    return list(db_chamados.values())

def atualizar_chamado(chamado):
    if chamado.id in db_chamados:
        db_chamados[chamado.id] = chamado
        return True
    return False