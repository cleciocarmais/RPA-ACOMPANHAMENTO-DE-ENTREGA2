# ⚡ RPA ACOMPANHAMENTO DE ENTREGAS PARTE 2

Bot que acessa o site das transportadora **[Braspress, Controlog, Brindx]**, e baixa relatorio de entregas de cada transportadora e salva dentro do diretorio raiz. Despois junta o relatorio em um unica planilha pegando as colunaas **[notaFiscas,previsaoEntrega,dataEntrega,nomeOcorrencia]** e compara com os pedidos que estao na planilha online e verificando cada condição.

---

## 🎯 Objetivo
Automatizar o identificara e acompanhar as entregas de cada pedido
---

## 📂 Etapas de Funcionamento

### **1️⃣ Coleta de Dados**
- 🔐 Login no site da **Braspres,Controlog,Brindx** com credenciais configuradas  
- 📅 Acessa á pagina de entregas
- 📌 Filtro: **data inicial = data atual - 20**  
- 📌 Filtro: **data final = data atual**  
- 📥 Extração de todos os registros filtrados  
- 💾 Salvamento dos dados em uma planilha

---

### **2️⃣ Tratamento dos Dados**
- 🧹 Separação das colunas: **notaFiscas,previsaoEntrega,dataEntrega,nomeOcorrencia**  de cada relatorio
- 📊 Jundar tudo em uma unica planilha chamada planilha_rota_entregas


---

### **2️⃣ Verificao**
- Pegua a planilha de vplanilha_rota_entregas e planilha online e verificar:
    - Se numero de pedito contem na planilha online se nao  Status **Transportadora nao encontrada**
    - Se a coluna **PrevisaoEntrega** da planilha_online  estiver preenchida verificar na  **planilha_rota_entregas** se a coluna **data de entrega** esta preenchida, caso esteja verificar se ambas a datas sao iguais se for Status **Entregue** se não Status **Entregue com atraso**. Caso coluna **Data de entrega** não estive preenchida e data de previsa for diferente da data atual Status **Pedido Atrasado**
    -

---

### **4️⃣ Notificação Final**
- 📧 Envio de dois email uma com os dados de sem transportadora e outro para os vendedores com os status do pedido

---

## 🔧 Tecnologias Utilizadas
- **Python**
- **Selenium** (automação web)
- **Pandas** (tratamento de dados)
- **OpenPyXL** (manipulação de planilhas)

- **Email Automation**

---

## 👨‍💻 Autor
Desenvolvido por **Francisco Clécio Vivaldini** 🚀