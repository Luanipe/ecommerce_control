# 🛒 E-Commerce Control

Projeto de e-commerce desenvolvido como parte do processo seletivo para Desenvolvedor Full Stack Pleno na IBBI. A aplicação é composta por:

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) com autenticação JWT.
- **Frontend**: [Next.js](https://nextjs.org/) com roteamento baseado em páginas, estilizado com [Tailwind CSS](https://tailwindcss.com/) e componentes do [ShadCN UI](https://ui.shadcn.com/).
- **Client HTTP**: [Axios](https://axios-http.com/ptbr/docs/intro) para integração com o servidor FastAPI e serviços externos.
- **Banco de Dados**: [PostgreSQL](https://www.postgresql.org/).
- **Orquestração**: [Docker Compose](https://docs.docker.com/compose/).

---

## 🚀 Tecnologias Utilizadas

### Backend

- **FastAPI**: Framework moderno e de alto desempenho para APIs em Python.
- **Autenticação JWT**: Implementada para rotas protegidas.
- **Banco de Dados**: PostgreSQL, com variáveis de ambiente configuradas no `docker-compose.yml`.
- **Alembic**: Ferramenta em Python para gerenciar migrações de banco de dados.
- **Pytest**: Framework de testes Python que simplifica a escrita e execução de testes.

### Frontend

- **Next.js**: Framework React com suporte a SSR e SSG.
- **Tailwind CSS**: Utilizado para estilização rápida e responsiva.
- **ShadCN UI**: Biblioteca de componentes acessíveis e personalizáveis.
- **Axios**: Configurado globalmente com suporte a JWT.
- **Hooks Personalizados**: `useFetch` e `useLoad` para requisições GET e `usePush` para POST/PUT.

### DevOps

- **Docker**: Plataforma de código aberto que permite aos desenvolvedores construir, executar e gerenciar contêineres.
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

## 📌 Funcionalidades

- **Cadastro e Login de Usuários**: Com autenticação JWT.
- **Cadastro de Entidades**: Cadastro de categorias e produtos.
- **Listagem de Entidades**: Listagem de categorias, produtos e vendas.
- **Histórico de Vendas**: Para controle de estoque dos produtos, quem vendeu e quem comprou.
- **Rotas Protegidas**: Determinadas rotas acessíveis apenas para usuários autenticados.
- **Hooks Personalizados**: `useFetch` e `useLoad` para requisições GET e `usePush` para POST/PUT.
- **Estilização**: Utilização de Tailwind CSS e componentes do ShadCN UI.

---

## ⚙️ Pendências

- **Componentes Compostos**: Criar componentes com o padrão de composição para melhor construção e reaproveitamento.
- **Telas e Roteamento do Frontend**: Criar dashboard e tela de carrinho.
- **Carrinho de Compras**: Implementar o carrinho de compras (já possui entidade no banco)
- **Checkout de Produtos**: Implementar o módulo de checkout para registrar uma venda de determinado produto.
- **Redis**: Adicionar cache com redis nas rotas de produto e vendas.

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