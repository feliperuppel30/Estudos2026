from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos
print(data_final)

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total/numero_parcelas
for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:.2F}')

print (f'em {data_emprestimo.strftime("%d/%m/%Y")} pegou o  valor de R$ {valor_total:.2F}')
print(f'e pagará em {numero_parcelas} parcelas de R$ {valor_parcela:.2F}')
print(f'cada uma, com a última parcela vencendo em {data_final.strftime("%d/%m/%Y")}')