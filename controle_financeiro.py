
import csv
import os
import math
from datetime import datetime

ARQUIVO_CSV = "movimentacoes.csv"

CAMPOS = ["tipo", "descricao", "valor", "data"]


def carregar_historico():
    if not os.path.exists(ARQUIVO_CSV):
        return []

    historico = []

    with open(
        ARQUIVO_CSV,
        "r",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                valor = float(linha["valor"])
                tipo = linha["tipo"].strip().lower()
                descricao = linha["descricao"].strip()
                data = linha.get("data") or "Data nao informada"

                if tipo not in ("receita", "despesa"):
                    continue

                historico.append({
                    "tipo": tipo,
                    "descricao": descricao,
                    "valor": valor,
                    "data": data
                })

            except (ValueError, KeyError, TypeError):
                print("Aviso: uma linha invalida foi ignorada.")

    return historico


def salvar_movimentacao(movimentacao):
    arquivo_existe = (
        os.path.exists(ARQUIVO_CSV)
        and os.path.getsize(ARQUIVO_CSV) > 0
    )

    with open(
        ARQUIVO_CSV,
        "a",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=CAMPOS
        )

        if not arquivo_existe:
            escritor.writeheader()

        escritor.writerow(movimentacao)


def ler_valor(tipo):
    while True:
        entrada = input(
            f"Valor da {tipo}: R$ "
        ).strip()

        entrada = entrada.replace(",", ".")

        try:
            valor = float(entrada)

            if not math.isfinite(valor) or valor <= 0:
                print("Digite um valor positivo e valido.")
                continue

            return valor

        except ValueError:
            print("Digite um numero valido.")


def cadastrar_movimentacao(tipo, historico):
    descricao = input(
        "Descricao da movimentacao: "
    ).strip()

    if not descricao:
        print("A descricao nao pode ficar vazia.")
        return

    valor = ler_valor(tipo)
    data = datetime.now().strftime("%d/%m/%Y")

    movimentacao = {
        "tipo": tipo,
        "descricao": descricao,
        "valor": f"{valor:.2f}",
        "data": data
    }

    try:
        salvar_movimentacao(movimentacao)

    except OSError as erro:
        print(f"Erro ao salvar o CSV: {erro}")
        return

    movimentacao["valor"] = valor
    historico.append(movimentacao)

    print("\nMovimentacao cadastrada com sucesso!")
    print(f"Data: {data}")
    print(f"Descricao: {descricao}")
    print(f"Valor: R$ {valor:.2f}")


def consultar_saldo(historico):
    receitas = sum(
        item["valor"]
        for item in historico
        if item["tipo"] == "receita"
    )

    despesas = sum(
        item["valor"]
        for item in historico
        if item["tipo"] == "despesa"
    )

    print("\n--- RESUMO FINANCEIRO ---")
    print(f"Total de receitas: R$ {receitas:.2f}")
    print(f"Total de despesas: R$ {despesas:.2f}")
    print(f"Saldo atual: R$ {receitas - despesas:.2f}")


def mostrar_historico(historico):
    print("\n--- HISTORICO DE MOVIMENTACOES ---")

    if not historico:
        print("Nenhuma movimentacao cadastrada.")
        return

    for numero, item in enumerate(historico, start=1):
        print(f"\nMovimentacao {numero}")
        print(f"Data: {item['data']}")
        print(f"Tipo: {item['tipo'].capitalize()}")
        print(f"Descricao: {item['descricao']}")
        print(f"Valor: R$ {item['valor']:.2f}")


def relatorio_mensal(historico):
    mes = input("Digite o mes (MM): ").strip()
    ano = input("Digite o ano (AAAA): ").strip()

    if (
        len(mes) != 2
        or not mes.isdigit()
        or not 1 <= int(mes) <= 12
        or len(ano) != 4
        or not ano.isdigit()
    ):
        print("Mes ou ano invalido.")
        return

    receitas = 0.0
    despesas = 0.0
    quantidade = 0

    for item in historico:
        try:
            data = datetime.strptime(
                item["data"], "%d/%m/%Y"
            )
        except ValueError:
            continue

        if data.month == int(mes) and data.year == int(ano):
            quantidade += 1

            if item["tipo"] == "receita":
                receitas += item["valor"]
            elif item["tipo"] == "despesa":
                despesas += item["valor"]

    print("\n--- RELATORIO MENSAL ---")
    print(f"Periodo: {mes}/{ano}")
    print(f"Movimentacoes: {quantidade}")
    print(f"Receitas: R$ {receitas:.2f}")
    print(f"Despesas: R$ {despesas:.2f}")
    print(f"Saldo mensal: R$ {receitas - despesas:.2f}")


def exportar_relatorio_mensal(historico):
    mes = input("Digite o mes (MM): ").strip()
    ano = input("Digite o ano (AAAA): ").strip()

    if (
        len(mes) != 2
        or not mes.isdigit()
        or not 1 <= int(mes) <= 12
        or len(ano) != 4
        or not ano.isdigit()
    ):
        print("Mes ou ano invalido.")
        return

    receitas = 0.0
    despesas = 0.0
    quantidade = 0
    movimentacoes_periodo = []

    for item in historico:
        try:
            data = datetime.strptime(
                item["data"], "%d/%m/%Y"
            )
        except (ValueError, TypeError):
            continue

        if data.month == int(mes) and data.year == int(ano):
            quantidade += 1
            movimentacoes_periodo.append(item)

            if item["tipo"] == "receita":
                receitas += item["valor"]
            elif item["tipo"] == "despesa":
                despesas += item["valor"]

    arquivo_saida = f"relatorio_{ano}_{mes}.csv"

    try:
        with open(
            arquivo_saida,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as arquivo:
            escritor = csv.writer(arquivo)

            escritor.writerow(["RELATORIO FINANCEIRO MENSAL"])
            escritor.writerow(["Periodo", f"{mes}/{ano}"])
            escritor.writerow(["Movimentacoes", quantidade])
            escritor.writerow(["Receitas", f"{receitas:.2f}"])
            escritor.writerow(["Despesas", f"{despesas:.2f}"])
            escritor.writerow([
                "Saldo mensal",
                f"{receitas - despesas:.2f}"
            ])

            escritor.writerow([])
            escritor.writerow([
                "Data",
                "Tipo",
                "Descricao",
                "Valor"
            ])

            for item in movimentacoes_periodo:
                escritor.writerow([
                    item["data"],
                    item["tipo"],
                    item["descricao"],
                    f"{item['valor']:.2f}"
                ])

        print("\nRelatorio exportado com sucesso!")
        print(f"Arquivo: {arquivo_saida}")
        print(f"Movimentacoes exportadas: {quantidade}")

    except OSError as erro:
        print(f"Erro ao exportar o relatorio: {erro}")


def main():
    historico = carregar_historico()

    print(
        f"\nMovimentacoes carregadas: {len(historico)}"
    )

    while True:
        print("\n" + "=" * 38)
        print("        CONTROLE FINANCEIRO")
        print("=" * 38)
        print("1 - Cadastrar receita")
        print("2 - Cadastrar despesa")
        print("3 - Consultar saldo")
        print("4 - Ver historico")
        print("5 - Relatorio mensal")
        print("6 - Sair")
        print("7 - Exportar relatorio mensal para CSV")

        opcao = input("\nEscolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_movimentacao("receita", historico)

        elif opcao == "2":
            cadastrar_movimentacao("despesa", historico)

        elif opcao == "3":
            consultar_saldo(historico)

        elif opcao == "4":
            mostrar_historico(historico)

        elif opcao == "5":
            relatorio_mensal(historico)

        elif opcao == "6":
            print("Encerrando o Controle Financeiro.")
            break

        elif opcao == "7":
            exportar_relatorio_mensal(historico)

        else:
            print("Opcao invalida. Escolha uma opcao de 1 a 7.")


if __name__ == "__main__":
    main()
