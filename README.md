## API de Usuários e Lição com Django e PostgreSQL
Descrição
Este projeto é uma API de gerenciamento de usuários e manipulação de conteúdo HTML armazenado no banco de dados. Ele foi desenvolvido utilizando Django, Django REST Framework e PostgreSQL. A aplicação permite a criação, leitura, atualização e exclusão de usuários, além da edição de conteúdo HTML.

## Como Clonar e Rodar o Projeto
1. Clone o Repositório
Primeiro, você precisa clonar este repositório do GitHub para a sua máquina local. No terminal, execute o seguinte comando:

bash
git clone https://github.com/LuizFelippeSilvaFagundes/teste_Api_backend_junior.git
Entre no diretório do projeto:

bash
cd seu-repositorio
2. Crie e Ative um Ambiente Virtual
Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto.

No Linux/MacOS:
bash
python3 -m venv venv
source venv/bin/activate
No Windows:
bash
python -m venv venv
venv\Scripts\activate
3. Instale as Dependências
Depois de ativar o ambiente virtual, você precisa instalar todas as dependências do projeto que estão listadas no arquivo requirements.txt. Use o seguinte comando:

bash
pip install -r requirements.txt
4. Configuração do Banco de Dados PostgreSQL
Este projeto usa PostgreSQL como banco de dados. Você deve configurar o banco de dados no arquivo settings.py. Substitua as informações pelo nome do banco, usuário e senha corretos.

Exemplo de configuração no settings.py:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco_de_dados',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Rode as Migrações
Para configurar o banco de dados, rode as migrações do Django:

bash
python manage.py makemigrations
python manage.py migrate
6. Crie um Superusuário
Se você quiser acessar o painel administrativo do Django, precisará criar um superusuário. Use o seguinte comando e siga as instruções para configurar um nome de usuário, e-mail e senha:

bash
python manage.py createsuperuser
7. Inicie o Servidor de Desenvolvimento
Agora, você pode rodar o servidor localmente. Use o seguinte comando:

bash
python manage.py runserver
Você poderá acessar a aplicação no seu navegador em http://127.0.0.1:8000/.

8. Acesse o Painel Administrativo
O Django oferece uma interface administrativa para gerenciar usuários e lições. Para acessá-la, vá até http://127.0.0.1:8000/admin/ e faça login com as credenciais do superusuário que você criou.

Testando a API
Você pode testar os endpoints da API usando ferramentas como Postman ou cURL. Aqui estão alguns exemplos de requisições que você pode testar.

1. Autenticação JWT
Endpoint para gerar um token JWT:

URL: http://127.0.0.1:8000/api/token/
Método: POST
Body:
json
{
  "email": "seu-email@gmail.com",
  "password": "sua-senha"
}
Resposta: Um token JWT que deve ser usado nas requisições seguintes.
Atualizar o Token JWT:

URL: http://127.0.0.1:8000/api/token/refresh/
Método: POST
Body:
json
Copiar código
{
  "refresh": "seu_refresh_token_aqui"
}
2. Endpoints de Usuários
Criar um Usuário:

URL: http://127.0.0.1:8000/api/usuarios/
Método: POST
Body:
json
{
  "nome": "João Silva",
  "email": "joao@gmail.com",
  "password": "senha123",
  "data_de_nascimento": "1990-05-20"
}
Listar Todos os Usuários:

URL: http://127.0.0.1:8000/api/usuarios/
Método: GET
Atualizar um Usuário:

URL: http://127.0.0.1:8000/api/usuarios/1/
Método: PUT
Body:
json
{
  "nome": "João Silva Atualizado",
  "email": "joao@gmail.com",
  "password": "nova_senha123",
  "data_de_nascimento": "1990-05-20"
}
Deletar um Usuário:

URL: http://127.0.0.1:8000/api/usuarios/1/
Método: DELETE
3. Manipulação de Lição
Editar o Conteúdo HTML de uma Lição:
URL: http://127.0.0.1:8000/api/licoes/1/editar-html/
Método: POST
Body:
json
{
  "conteudo_html": "<button style='color: red;'>Clique aqui</button>"
}
Conclusão
Agora você deve estar com o projeto rodando localmente e já pode testar os endpoints da API conforme a especificação. Se precisar de mais ajuda ou tiver algum problema, consulte a documentação ou entre em contato.

