
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

ARQUIVO_CSV = "movimentacoes.csv"


def carregar_dados_mensais():
    dados = {}

    if not os.path.exists(ARQUIVO_CSV):
        print("Arquivo movimentacoes.csv nao encontrado.")
        return dados

    with open(
        ARQUIVO_CSV,
        "r",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                tipo = linha["tipo"].strip().lower()
                valor = float(linha["valor"].replace(",", "."))
                data = datetime.strptime(
                    linha["data"], "%d/%m/%Y"
                )

                if tipo not in ("receita", "despesa"):
                    continue

                mes_ano = data.strftime("%Y-%m")

                if mes_ano not in dados:
                    dados[mes_ano] = {
                        "receitas": 0.0,
                        "despesas": 0.0
                    }

                if tipo == "receita":
                    dados[mes_ano]["receitas"] += valor
                else:
                    dados[mes_ano]["despesas"] += valor

            except (ValueError, KeyError, AttributeError, TypeError):
                print("Uma movimentacao invalida foi ignorada.")

    return dados


def criar_grafico_mensal():
    dados = carregar_dados_mensais()

    if not dados:
        print("Nao ha dados validos para gerar o grafico.")
        return

    meses = sorted(dados.keys())

    receitas = [
        dados[mes]["receitas"]
        for mes in meses
    ]

    despesas = [
        dados[mes]["despesas"]
        for mes in meses
    ]

    posicoes = list(range(len(meses)))
    largura = 0.35

    plt.figure(figsize=(10, 6))

    barras_receitas = plt.bar(
        [p - largura / 2 for p in posicoes],
        receitas,
        largura,
        label="Receitas"
    )

    barras_despesas = plt.bar(
        [p + largura / 2 for p in posicoes],
        despesas,
        largura,
        label="Despesas"
    )

    plt.title("Receitas e Despesas por Mes")
    plt.xlabel("Mes")
    plt.ylabel("Valor (R$)")
    plt.xticks(posicoes, meses, rotation=45)
    plt.legend()

    for barras in (barras_receitas, barras_despesas):
        for barra in barras:
            valor = barra.get_height()
            plt.annotate(
                f"R$ {valor:.2f}",
                (barra.get_x() + barra.get_width() / 2, valor),
                ha="center",
                va="bottom",
                fontsize=8,
                rotation=45
            )

    plt.tight_layout()

    # Salvar o grafico como imagem
    plt.savefig(
        "grafico_mensal.png",
        dpi=150,
        bbox_inches="tight"
    )

    print("Grafico salvo em grafico_mensal.png")

    plt.show()


if __name__ == "__main__":
    criar_grafico_mensal()
