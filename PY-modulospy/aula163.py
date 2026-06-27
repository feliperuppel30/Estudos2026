from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('21/01/2025 20:20:20', fmt)
data_fim = datetime.strptime('31/05/2026 22:30:40', fmt)

delta = data_fim-data_inicio
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())