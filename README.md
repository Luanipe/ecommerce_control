# 🛒 E-Commerce Control

Projeto de e-commerce desenvolvido como parte do processo seletivo para Desenvolvedor Full Stack Pleno na IBBI. A aplicação é composta por:

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) com autenticação JWT.
- **Frontend**: [Next.js](https://nextjs.org/) com roteamento baseado em páginas, estilizado com [Tailwind CSS](https://tailwindcss.com/) e componentes do [ShadCN UI](https://ui.shadcn.com/).
- **Banco de Dados**: [PostgreSQL](https://www.postgresql.org/).
- **Orquestração**: [Docker Compose](https://docs.docker.com/compose/).

---

## 🚀 Tecnologias Utilizadas

### Backend

- **FastAPI**: Framework moderno e de alto desempenho para APIs em Python.
- **Autenticação JWT**: Implementada para rotas protegidas.
- **Banco de Dados**: PostgreSQL, com variáveis de ambiente configuradas no `docker-compose.yml`.
- **Alembic**: Ferramenta em Python para gerenciar migrações de banco de dados.

### Frontend

- **Next.js**: Framework React com suporte a SSR e SSG.
- **Tailwind CSS**: Utilizado para estilização rápida e responsiva.
- **ShadCN UI**: Biblioteca de componentes acessíveis e personalizáveis.
- **Axios**: Configurado globalmente com suporte a JWT.
- **Hooks Personalizados**: `useFetch` e `useLoad` para requisições GET e `usePush` para POST/PUT.

### DevOps

- **Docker Compose**: Facilita a orquestração de múltiplos serviços.

---

## 🐳 Como Rodar com Docker Compose

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Luanipe/ecommerce_control.git
   cd ecommerce_control
   ```
2. **Construa e inicie os containers:**
   ```bash
   docker-compose up --build
   ```
   - Se quiser rodar o compose em background, rode o comando acima com a flag `-d` no final.

3. **Acesse os serviços:**
   - Frontend: http://localhost:3000
   - Backend (Swagger UI): http://localhost:8000/docs
   - Banco de Dados: PostgreSQL na porta `5432` com:
     - Usuário: `admin`
     - Senha: `password`
     - Banco - `commerce`

---

## 🔐 Autenticação

- **Registro e Login**: Realizados na mesma tela de forma dinâmica.
- **Armazenamento do Token**: O token JWT é armazenado no localStorage.
- **Proteção de Rotas**: Implementada no frontend para redirecionar usuários não autenticados para a tela de login.

---

## 🛠️ Comandos Úteis
- **Parar os containers**:

    ```bash
    docker-compose down
    ```
- **Acessar o shell do backend**:
    ```bash
    docker exec -it server /bin/sh
    ```

---

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/Luanipe/ecommerce_control/blob/master/LICENSE) para mais detalhes.

--- 

## 👤 Autor
- **Luan Ipê**: [github.com/Luanipe](https://github.com/Luanipe)