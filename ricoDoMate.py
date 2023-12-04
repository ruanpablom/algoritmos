def rico_do_mate(qtdPessoasNaRoda, qtdLitrosDeAguaQueCabeNaTermica, qtdListrosDeAguaQueCabeNaCuia, listaDePessoas):
  quantidadeDeCuias = round(qtdLitrosDeAguaQueCabeNaTermica/qtdListrosDeAguaQueCabeNaCuia, 1)
  cuiasInteiras = int(quantidadeDeCuias)
  ultimaCuia = round((quantidadeDeCuias - cuiasInteiras) * qtdListrosDeAguaQueCabeNaCuia, 1)
  if ultimaCuia > 0:
    quantidadeDeCuias = int(cuiasInteiras + 1)
  else:
    ultimaCuia = qtdListrosDeAguaQueCabeNaCuia
  
  indexDaUltimaPessoa = int(quantidadeDeCuias % qtdPessoasNaRoda)
  return f'{listaDePessoas[indexDaUltimaPessoa - 1]} {ultimaCuia}'

print(['Lara','Maria', 'Renato', 'Juca']*10)