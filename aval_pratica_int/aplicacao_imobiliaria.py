from model import *

imobiliaria = Imobiliaria()


def inserir_imovel():
    try:
        escolha = int(input('1- Residência\n2- Escritório\n Opção: '))
        cod = int(input('Código: '))
        regiao = input('Região: ')
        area = float(input('Área: '))
        if escolha == 1:
            quartos = int(input('Num quartos: '))
            res = Residencia(cod, regiao, area, True,quartos)
            if imobiliaria.inserir(res):
                print('Residência inserida com sucesso!!!\n\n')

        elif escolha == 2:
            area_util = float(input('Área útil: '))
            esc = Escritorio(cod, regiao, area, True, area_util)
            if imobiliaria.inserir(esc):
                print('Escritório inserido com sucesso!!!\n\n')
    except Exception:
        print("Erro ao inserir imóvel!!!\n\n")


def remover_imovel():
    try:
        cod = int(input('Informe o código: '))
        imovel = imobiliaria.obter_imovel(cod)
        if imobiliaria.remover(imovel):
            print("Removido com sucesso!\n\n")
    except Exception:
        print("Erro ao remover!!!\n\n")


def alugar_imovel():
    try:
        cod = int(input('Informe o código: '))
        imovel = imobiliaria.obter_imovel(cod)
        if imobiliaria.alugar(imovel):
            print("Alugado!!!\n\n")
    except Exception:
        print("Não foi possível alugar!!!\n\n")


def devolver_imovel():
    try:
        cod = int(input('Informe o código: '))
        imovel = imobiliaria.obter_imovel(cod)
        if imobiliaria.devolver(imovel):
            print("Devolvido com sucesso!!!\n\n")
    except Exception:
        print("Erro na devolução!\n\n")


def listar_imoveis(regiao):
    print(imobiliaria.listar_imovel(regiao))


opcao = 0

if __name__ == "__main__":
    while opcao != 6:
        print('=============================================')
        print('=                                           =')
        print('= 1) Inserir Imóvel                         =')
        print('= 2) Remover Imóvel                         =')
        print('= 3) Alugar Imóvel                          =')
        print('= 4) Devolver Imóvel                        =')
        print('= 5) Listar Imóveis                         =')
        print('= 6) Sair                                   =')
        print('=                                           =')
        print('=============================================')

        opcao = int(input('Informe sua opção: '))

        if opcao == 1:
            inserir_imovel()
        elif opcao == 2:
            remover_imovel()
        elif opcao ==3:
            alugar_imovel()
        elif opcao == 4:
            devolver_imovel()
        elif opcao == 5:
            reg = input('Se quiser informe a região: ')
            listar_imoveis(reg)
        elif opcao ==6:
            pass
        else:
            print("Opção inválida!!! \n\n")
