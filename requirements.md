# Requisitos funcionais 
1. RF01	O sistema deve apresentar um menu interativo com os tipos de ataques disponíveis.

2. RF02	O sistema deve aceitar como entrada um IP, domínio, range de rede ou hostname.

3. RF03	O sistema deve realizar reconhecimento passivo (ex: whois, dnsdumpster, etc).

4. RF04	O sistema deve realizar varredura de portas com ferramentas como nmap e masscan.

5. RF05	O sistema deve realizar enumeração de serviços com base nos resultados do scanner.

6. RF06	O sistema deve realizar força bruta de serviços (FTP, SSH, HTTP) com wordlists.

7. RF07	O sistema deve realizar exploração automatizada de serviços vulneráveis (via scripts próprios ou wrappers como sqlmap).

8. RF08	O sistema deve salvar os resultados em arquivos organizados por sessão.

9. RF09	O sistema deve gerar relatórios simples (formato .txt, .md, .html).

10. RF10	O sistema deve suportar modo “manual” e modo “automático” (com ataque encadeado).

11. RF11	O sistema deve registrar logs de cada etapa do ataque para auditoria posterior.

# Requisitos Não Funcionais (RNF)
Código	Descrição
1. RNF01	O sistema deve ser compatível com distribuições Linux (Ubuntu, Kali, Parrot).

2. RNF02	O sistema deve funcionar em modo terminal (CLI), sem necessidade de GUI.

3. RNF03	O sistema deve ser modular para facilitar adição de novos ataques e ferramentas.

4. RNF04	O sistema deve rodar com performance aceitável, mesmo em máquinas virtuais.

5. RNF05	O sistema deve utilizar logs e separação de arquivos para facilitar debugging.

6. RNF06	O sistema deve tratar erros de forma segura (ex: falhas no subprocess, entradas inválidas).

7. RNF07	O sistema deve usar bibliotecas open-source apenas.

8. RNF08	O sistema deve alertar o usuário sobre uso ético e legal antes de iniciar.