# Inteligência Artificial aplicada à patologia

Este projeto utiliza o [Health AI Developer Foundations (HAI-DEF)](https://developers.google.com/health-ai-developer-foundations), um conjunto de recursos e modelos pré-treinados desenvolvidos pelo time de pesquisa do Google e de fácil integração com a infraestrutura Google Cloud.

## Funcionalidades

- Modelo pronto de classificação de imagens histopatológicas benignas ou cancerígenas
- Conversão do modelo em formato `Keras` para `SavedModel`
- Aplicação Streamlit para fins de demonstração do modelo em interface amigável
- Container para integrar o modelo na Vertex AI, plataforma de inteligência artificial do Google Cloud

## Pré-requisitos

- Python 3.8 ou acima
- Pacotes Python requisitados (cheque os arquivos `requirements.txt`)

### Caso vá integrar o modelo em Google Cloud
- Projeto do Google Cloud: certifique-se de ter um Projeto do Google Cloud ativo. Se não tiver, você pode criar um no Google Cloud Console.
- Habilite a API do Artifact Registry: no seu projeto, habilite a API do Artifact Registry. Você pode fazer isso por meio do Cloud Console ou da ferramenta de linha de comando gcloud.
- Autenticação: certifique-se de que sua conta de usuário tenha as permissões necessárias para criar recursos no Artifact Registry. A função Artifact Registry Writer deve ser suficiente.

## Instalação

1. Clone o repositório:
```bash
git clone [repository-url]
cd ia-para-patologia
```

2. Crie um ambiente virtual isolado para cada projeto (`pathology-demo` e `vertexai-custom-container`):
```bash
python3 -m venv .env
source .env/bin/activate
```

3. Instale as dependências Python nos respectivos ambientes:
```bash
pip install -r requirements.txt
```

4. Crie o diretório para armazenar o modelo em formato `SavedModel` (pasta completa `fine_tuned_model_tf` gerada a partir do notebook `carregando_modelo_treinado.ipynb`):
```bash
cd pathology-demo
mkdir local_models
cd ..
cd vertexai-custom-container
mkdir local_model
```

## Uso

### Para utilização local da aplicação Streamlit:

1. Execute no terminal:
```bash
cd pathology-demo
streamlit run Home.py --server.port=8080
```

### Para integração com Vertex AI: 

1. Crie um repositório no Artifact Registry para armazenar sua imagem de container:
```bash
gcloud artifacts repositories create REPOSITORY_NAME \
    --repository-format=docker \
    --location=LOCATION
```

2. Construa a imagem do Docker:
```bash
docker build -t pathology .
```

2. Crie uma tag para a imagem:
```bash
docker tag pathology us-central1-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/pathology:latest
```

3. Empurre a imagem para o Artifact Registry
```bash
docker push us-central1-docker.pkg.dev/[PROJECT_ID]/REPOSITORY_NAME/pathology:latest
```

4. Importe o modelo no Model Registry da Vertex AI:
[Interface](https://cloud.google.com/vertex-ai/docs/model-registry/import-model)

5. Faça o deploy em um endpoint da Vertex AI:
[Interface](https://cloud.google.com/vertex-ai/docs/general/deployment)

6. Teste usando o arquivo `b64_for_test.txt`, que contém uma imagem de teste já em base64:
```json
{
    "instances": [
      "[BASE64]"
    ]
}  
```

Exemplo de resposta esperada:
```json
{
 "predictions": [
   {
     "prediction_percentage": "95%",
     "prediction_label": "Benigna"
   }
 ],
 "deployedModelId": "XXXXXX",
 "model": "projects/XXXXX/locations/us-central1/models/XXXXXXXX",
 "modelDisplayName": "pathology",
 "modelVersionId": "1"
}
```

## Estrutura do projeto

```
ia-para-patologia/
├── pathology-demo/             # Aplicação Streamlit
├── vertexai-custom-container/  # Docker container para integração na Vertex AI
├── fine_tuned_model.keras      # Modelo de classificação pronto
└── carregando_modelo_treinado  # Notebook de conversão de formatos de modelos
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

## Licença

Este projeto está licenciado sob a Licença Apache - veja o arquivo LICENSE para mais detalhes.
