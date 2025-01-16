FROM python:3.10

WORKDIR /vertexai-custom-container
COPY . ./

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]