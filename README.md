# Inteligência Artificial aplicada à patologia

Este projeto utiliza o [Health AI Developer Foundations (HAI-DEF)](https://developers.google.com/health-ai-developer-foundations), um conjunto de recursos e modelos pré-treinados desenvolvidos pelo time de pesquisa do Google e de fácil integração com a infraestrutura Google Cloud.

## Funcionalidades

- Modelo pronto de classificação de imagens histopatológicas benignas ou cancerígenas
- Conversão do modelo em formato `Keras` para `SavedModel`
- Aplicação Streamlit para fins de demonstração do modelo em interface amigável

## Pré-requisitos

- Python 3.8 ou acima
- Pacotes Python requisitados (cheque o arquivo `requirements.txt` para a aplicação Streamlit ou dentro do próprio notebook para os demais)

## Instalação

1. Clone o repositório:
```bash
git clone [repository-url]
cd ia-para-patologia
```

2. Crie um ambiente virtual:
```bash
python3 -m venv .env
source .env/bin/activate
```

3. Instale as dependências Python:
```bash
pip install -r pathology-demo/requirements.txt
```

4. Crie o diretório para armazenar o modelo em formato `SavedModel` (pasta completa `fine_tuned_model_tf` gerada a partir do notebook `carregando_modelo_treinado.ipynb`):
```bash
cd pathology-demo
mkdir local_models
```

## Uso

1. Para utilização local da aplicação Streamlit:
```bash
cd pathology-demo
streamlit run Home.py --server.port=8080
```

## Estrutura do projeto

```
ia-para-patologia/
├── carregando_modelo_treinado  # Notebook de conversão de formatos de modelos
├── fine_tuned_model.keras      # Modelo de classificação pronto
└── pathology-demo/             # Aplicação Streamlit
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

## Licença

Este projeto está licenciado sob a Licença Apache - veja o arquivo LICENSE para mais detalhes.
