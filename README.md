<h6>Odoo</h6>
<h1 align="center"> Módulo CRM customizado </h1>
<h6 align="center">by Keiko</h6>

CRM Custom é uma melhoria para o módulo de CRM do framework Odoo. Neste módulo foram adicionados novos campos para cadastramento das informações relativas aos clientes potenciais de uma empresa fantasia que vende produtos para condominios.

----------

<h3> Funcionalidades adicionais implementadas neste módulo </h3>

Atributos adicionais:
   - Quantidade de unidades;
   - Quantidades de blocos;
   - Qunatidade de moradores;
   - Tipo de portaria (Própria ou terceirizada);
   - Horário da portaria(24 horas ou 12 horas).
 
 Relatório: Constando nome do cliente e os dados de qualificação, também conta o atributos adicionais inseridos.
 
 ----------
 
<h3> Requisitos </h3>

   - Sistema operacional Linux
   - Pycharm
   - Módulo do Odoo 12.0

----------

<h3>Estrutura do Diretório</h3>

Para a instalação deste módulo siga a seguinte estrutura:
  
 ```
├── projects
│   └── 12.0
          ├── odoo
          └── crm_custom
 ```

----------

<h3> Guia de instalação </h3>

1. Clone o repositório com o comando:

```
git clone https://github.com/keikomori/crm_custom.git
```

2. Realize a instalação do módulo Odoo 12.0 dentro do repositório deste projeto (caso deseje seguir a mesma estrutura).

[Guia de instalação](https://github.com/keikomori/install-odoo) 

3. No PyCharm crie um novo projeto, você pode seguir esse tutorial legal que pode te direcionar nas configurações

[Tutorial do uso do PyCharm](https://www.cybrosys.com/blog/configure-pycharm-odoo-13-development-ubuntu-20-04)

Lembrando que deve ser definido o caminho do `Script path` e `Parameters` nas configurações de Run/Debug do PyCharm

4. Lá nas configurações `Parameters`:

    ```
    -c {caminho até essa pasta}/12.0/.odoorc -d {nome do banco} -u -u custom_crm
    ```

5. Lá nas configurações `Script path`:

    ```
    {caminho até essa pasta}/12.0/odoo/odoo-bin
    ```
    
6. Prontinho, agora é só rodar e realizar a instalação do Módulo: `CRM custom`. É fácil encontrá-lo ;D é o primeiro módulo em Apps.

8. Está tudo em inglês??? Oh! Esse módulo também inclui as traduções dos novos termos que foram inseridos. Basta adicionar a tradução. Yay!

----------

<h3> E o relatório, onde pode ser visualizado? </h3>

Lá no menu do CRM em Reporting temos o CRM Custom, que contém todos os atributos adicionais que foram inseridos neste módulo.

----------

{... FIM!}
