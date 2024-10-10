

from datetime import datetime


# Exemplo de lista de faltas
faltas = [
    {"data": "2024-10-01", "local": "Fazenda A", "motivo": "Doença"},
    {"data": "2024-10-05", "local": "Fazenda B", "motivo": "Compromisso familiar"},
    {"data": "2024-10-07", "local": "Fazenda A", "motivo": "Doença"},
    {"data": "2024-10-10", "local": "Fazenda C", "motivo": "Trânsito"},
    {"data": "2024-10-12", "local": "Fazenda A", "motivo": "Doença"},
]

# Função para filtrar faltas por data e local
def filtrar_faltas(faltas, data_inicio=None, data_fim=None, local=None):
    # Convertendo as strings de data para o formato datetime para comparações
    from datetime import datetime
    
    if data_inicio:
        data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
    if data_fim:
        data_fim = datetime.strptime(data_fim, "%Y-%m-%d")
    
    # Lista de faltas filtradas
    faltas_filtradas = []
    
    for falta in faltas:
        data_falta = datetime.strptime(falta["data"], "%Y-%m-%d")
        
        # Verifica as condições de filtro
        if data_inicio and data_falta < data_inicio:
            continue
        if data_fim and data_falta > data_fim:
            continue
        if local and falta["local"] != local:
            continue
        
        faltas_filtradas.append(falta)
    
    return faltas_filtradas

# Exemplo de uso do filtro
data_inicio = "2024-10-01"
data_fim = "2024-10-10"
local = "Fazenda A"

faltas_filtradas = filtrar_faltas(faltas, data_inicio, data_fim, local)

# Exibindo as faltas filtradas
for falta in faltas_filtradas:
    print(f"Data: {falta['data']}, Local: {falta['local']}, Motivo: {falta['motivo']}")
