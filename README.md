# Inteligência Artificial aplicada à patologia

Este projeto utiliza o [Health AI Developer Foundations (HAI-DEF)](https://developers.google.com/health-ai-developer-foundations), um conjunto de recursos e modelos pré-treinados desenvolvidos pelo time de pesquisa do Google e de fácil integração com a infraestrutura Google Cloud.

## Funcionalidades

- Modelo pronto de classificação de imagens histopatológicas benignas ou cancerígenas
- Conversão do modelo em formato `Keras` para `SavedModel`

## Pré-requisitos

- Python 3.8 ou acima
- Pacotes Python requisitados (cheque o arquivo `requirements.txt`)

## Instalação

1. Clone o repositório:
```bash
git clone [repository-url]
cd ia-para-patologia
```

2. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

## Uso

TO DO

## Estrutura do projeto

```
ia-para-patologia/
├── carregando_modelo_treinado  # Notebook de conversão de formatos de modelos
├── fine_tuned_model.keras      # Modelo de classificação pronto
└── requirements.txt  # Python dependencies
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

## Licença

Este projeto está licenciado sob a Licença Apache - veja o arquivo LICENSE para mais detalhes.
