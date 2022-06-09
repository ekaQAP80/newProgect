per_cent = {}
per_cent['ТБК'] = 5.6
per_cent['СКБ'] = 5.9
per_cent['ВТБ'] = 4.28
per_cent['СБЕР'] = 4.0
sum_dep = int(input('Введите сумму вклада -'))
print('доход по вкладу в банках')
per_cent_list = [(k[:6], int(v*sum_dep/100)) for k, v in per_cent.items()]
print(per_cent_list)
per_cent_list2 = [int(v*sum_dep/100) for k, v in per_cent.items()]
print("максимальная сумма, которую вы можете заработать -",max(per_cent_list2))