from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a tela inicial
@app.route('/')
def tela_inicial():
    return render_template('tela-inicial.html')


# Rota para a tela de login
@app.route('/login')
def login():
    return render_template('tela-login.html')


# Rota para a tela cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


# Rota para a tela home
@app.route('/home')
def home():
    return render_template('home.html')


# Rota para a tela de cadastro de turmas
@app.route("/cadastrar-turma")
def cadastrar_turma():
    return render_template("cadastrar-turmas.html")


# Rota para a tela de cadastro de trabalhos (GET e POST)
@app.route("/cadastrar-trabalho", methods=["GET", "POST"])
def cadastrar_trabalho():
    if request.method == 'POST':
        # Captura os dados do formulário
        titulo = request.form['titulo']
        id_curso = request.form['id_curso']
        descricao = request.form['descricao']
        palavras_chave = request.form['palavras_chave']
        link = request.form['link']

        # Aqui você pode adicionar lógica para salvar no banco de dados

        # Se tudo estiver correto, exibe mensagem de sucesso
        mensagem = "Trabalho cadastrado com sucesso!"
        return render_template('cadastrar-trabalhos.html', mensagem=mensagem)

        # Se ocorrer algum erro, exibe mensagem de erro
        # mensagem_erro = "Erro ao cadastrar o trabalho. Tente novamente."
        # return render_template('cadastrar-trabalhos.html', mensagem_erro=mensagem_erro)

    return render_template('cadastrar-trabalhos.html')


# Rota para cadastrar cursos (formulário)
@app.route('/cadastrar-cursos', methods=['GET', 'POST'])
def cadastrar_curso():
    if request.method == 'POST':
        # Simulando um erro, como por exemplo, se algum campo estiver vazio
        if not request.form['nome']:
            mensagem_erro = "Por favor, preencha todos os campos obrigatórios!"
            return render_template('cadastrar-cursos.html', mensagem_erro=mensagem_erro)

        # Aqui futuramente vai o código para salvar os dados no banco
        mensagem = "Curso cadastrado com sucesso!"
        return render_template('cadastrar-cursos.html', mensagem=mensagem)

    return render_template('cadastrar-cursos.html')


if __name__ == '__main__':
    app.run(debug=True)




