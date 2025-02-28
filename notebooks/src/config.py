from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"

DADOS_ORIGINAIS = PASTA_DADOS / "diabetes.zip"
DADOS_TRATADOS = PASTA_DADOS / "diabetes_tratada.parquet"

PASTA_IMAGENS = PASTA_PROJETO / "imagens"
