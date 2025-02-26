from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

data_emprestimo = datetime.strptime('2020/12/20', '%Y/%m/%d')
data_final_emprestimo = datetime.strptime('2025/12/20', '%Y/%m/%d')
data_parcela_atual = datetime.strptime('2020/12/20', '%Y/%m/%d')
periodo_em_meses = (data_final_emprestimo.year - data_emprestimo.year) * 12
valor_emprestimo = 1000000
valor_parcela = valor_emprestimo/ periodo_em_meses
valor_pago = valor_parcela

                                    

while valor_pago <= valor_emprestimo:
    print(f'{data_parcela_atual.strftime('%d/%m/%Y')}, {valor_parcela:,.2f}, {valor_pago:,.2f}')
    data_parcela_atual += relativedelta(months=1)
    valor_pago += valor_parcela
