import csv
import os

arquivo='gastos.csv'
def inicializar_arquivo():
    if not os.path.exists(arquivo):
        with open(arquivo,'w',newline='',encoding='utf-8') as f:
            writer=csv.writer(f)
            writer.writerow(['Descrição','Valor'])

def adicionar_gasto():
    descricao=input('Descrição da compra: ')
    valor=float(input('Valor da compra: '))

    with open(arquivo,'a',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow([descricao,valor])

    print('Gasto salvo com sucesso!✅')

def ver_gastos():
    print('\n--- Gastos da Fatura ---')
    with open(arquivo,'r',encoding='utf-8') as f:
        reader=csv.reader(f)
        next(reader)
        vazio= True
        for descricao,valor in reader:
            print(f'{descricao}: R$ {float(valor):.2f}')
            vazio=False
        if vazio:
            print('Nenhum gasto registrado.')
    print()
def total_fatura():
    total=0
    with open(arquivo,'r',encoding='utf-8')as  f:
        reader=csv.reader(f)
        next(reader)

        for _, valor in reader:
            total+=float(valor)
    print(f'\n💳 Total da Fatura: R$ {total:.2f}\n')

def excluir_gastos():
    gastos=[]
    with open(arquivo,'r',encoding='utf-8') as f:
        reader=csv.reader(f)
        cabecalho=next(reader)

        for linha in reader:
            gastos.append(linha)
    if not gastos:
        print('Nenhum gasto para excluir.')
        return
    print('--- Gastos ---')
    for i,(descricao,valor) in enumerate(gastos, start=1):
        print(f"{i} - {descricao}: R$ {float(valor):.2f}")
    opcao=input('Digite o número do gasto que deseja excluir: ')
    if not opcao.isdigit():
        print('Opção inválida!')
        return
    opcao=int(opcao)
    if opcao<1 or opcao>len(gastos):
        print('Número inválido!')
        return
    gasto_removido=gastos.pop(opcao - 1)
    with open(arquivo,'w',newline='',encoding='utf-8')as f:
        writer=csv.writer(f)
        writer.writerow(cabecalho)
        writer.writerows(gastos)
    print("🗑 Gasto '{gasto_removido[0]}' removido!")




#==== PROGRAMA PRNCIPAL ====
inicializar_arquivo()
while True:
    print('===\033[4;31m MENU FATURA DO CARTÃO\033[m ===')
    print('1 - Adicionar gasto')
    print('2 - Ver gasto')
    print('3 - Ver total da fatura')
    print('4 - Excluir gasto')
    print('5 - Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao== 1:
        adicionar_gasto()
        input('Pressione ENTER para voltar ao menu..')
    elif opcao== 2:
        ver_gastos()
        input('Pressione ENTER para voltar ao menu...')
    elif opcao== 3:
        total_fatura()
        input('Pressione ENTER para voltar ao menu...')
    elif opcao== 4:
        excluir_gastos()
        input('Pressione ENTER para voltar ao menu...')
    elif opcao== 5:
        print('\033[1;33mSaindo do programa\033[m...')
        break
    else:
        print('❌\033[4Opção inválida!\033[m❌')
        input('Pressione ENTER para tentar novamente...')
