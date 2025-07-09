# Instruções do Agente para Geração de Desafios de Algoritmos

## Visão Geral do Projeto

Este repositório tem como objetivo auxiliar nos estudos de **estruturas de dados e algoritmos** em profundidade, especialmente visando entrevistas técnicas para **Software Engineering**. A ideia é criar um ambiente semelhante a plataformas de desafios (como HackerRank ou LeetCode), porém totalmente local e personalizado. Um **agente (IA)** irá gerar automaticamente desafios de programação a partir de um conceito dado, incluindo casos de teste automatizados e esboços de soluções (com partes faltando para o praticante implementar). Dessa forma, será possível praticar diferentes tópicos de algoritmos, entender *trade-offs* e aprimorar a implementação em Python com foco em desempenho e boas práticas.

 

Cada desafio gerado será **autocontido** e independente, permitindo executá-lo e resolvê-lo sem dependências externas além do Python padrão. Os desafios terão testes automatizados escritos em **PyTest**, podendo ser executados em paralelo ou em conjunto – garantindo uma validação rápida de suas soluções com um único comando de teste. A seguir detalhamos os objetivos, funcionamento do agente gerador, estrutura sugerida do repositório e convenções a serem seguidas.



## Objetivos e Funcionalidades Desejadas

- **Cobertura Abrangente de Conceitos:** Dado um **conceito** de estrutura de dados ou algoritmo (ex: *árvores binárias*, *grafos*, *ordenamento*, etc.), o agente deve propor **várias tarefas** práticas relacionadas. Isso permite explorar diferentes aspectos do conceito e reforçar o entendimento teórico através da implementação. Por exemplo, para o conceito *árvores binárias*, poderíamos ter tarefas sobre balanceamento de árvore, percursos em largura e profundidade, inserção e remoção em BST, etc.
- **Aprendizado Orientado a Testes:** Cada tarefa incluirá um conjunto de **testes automatizados** que validam a solução. Isso incentiva uma abordagem *Test-Driven Development (TDD)* durante os estudos. A utilização de testes torna mais fácil e rápido verificar a correção e robustez das soluções, além de forçar a consideração de casos de borda e eficiência[adamj.eu](https://adamj.eu/tech/2019/04/21/solving-algorithmic-problems-in-python-with-pytest/#:~:text=In either case%2C using automated,wish I knew this earlier). Em Python, o framework PyTest é preferido por sua simplicidade e poder expressivo, sendo amplamente considerado superior ao módulo integrado `unittest` para esse tipo de validação[adamj.eu](https://adamj.eu/tech/2019/04/21/solving-algorithmic-problems-in-python-with-pytest/#:~:text=In Python%2C there’s no better,in unittest).
- **Soluções Parciais para Implementação:** O agente fornecerá um *esqueleto* de solução para cada problema: isto inclui a assinatura da função ou método a ser implementado, possivelmente partes auxiliares já prontas (por exemplo, classes de dados como um nó de árvore), e marcações claras dos trechos que o usuário deverá escrever. Trechos não implementados serão indicados explicitamente, por exemplo com `raise NotImplementedError()` ou comentários `# TODO` no corpo da função. O uso de `NotImplementedError` em funções inacabadas é uma prática comum para lembrar o desenvolvedor de completá-las e evitar que stubs vazios falhem silenciosamente[stackoverflow.com](https://stackoverflow.com/questions/49346946/i-dont-understand-why-raise-notimplementederror-is-necessary-here-python#:~:text=,and there would be bugs).
- **Independência e Paralelismo:** As tarefas geradas devem ser **autocontidas**, de modo que possam ser resolvidas em qualquer ordem. Isso significa que cada desafio inclui todo o código necessário para rodar seus testes (por exemplo, se for necessária uma estrutura de dado auxiliar como uma árvore ou grafo, essa estrutura deve ser definida no próprio desafio ou incluída nos arquivos dele). Tarefas não devem depender de funções ou módulos definidos em outros desafios. Assim, é possível trabalhar em vários desafios em paralelo ou pular entre eles sem se preocupar com efeitos colaterais. Além disso, todos os desafios podem ser executados sequencialmente nos testes automatizados sem interferência mútua.
- **Execução Rápida de Testes:** Deve ser fácil rodar **todos os testes** do repositório de uma vez, para verificar se todas as soluções (implementadas pelo usuário) estão corretas. Idealmente, um único comando no terminal (por exemplo `pytest` na raiz do projeto) deverá descobrir e executar todos os casos de teste em todos os desafios[fig.io](https://fig.io/manual/pytest#:~:text=,current directory and its subdirectories). Também é desejável que haja suporte a rodar testes de um único desafio isoladamente (por exemplo, via `pytest caminho/para/desafio/`), o que é facilitado pela independência de cada conjunto de arquivos.
- **Evolução Contínua com Qualidade:** À medida que o repositório crescer com novos desafios, pretende-se que **todos os testes permaneçam passando** (ou seja, as soluções para desafios anteriores continuam corretas após eventuais melhorias, e os desafios novos só são adicionados quando o usuário estiver pronto para implementá-los). Dessa forma, o repositório serve como um registro do progresso do aprendizado – sempre em estado consistente e verificado. O agente deve, portanto, ser usado para gerar desafios incrementais, e o usuário os implementa para manter o *build* passando.

## Papel e Funcionamento do Agente (Codex)

O **Agente Codex** será responsável por automatizar a geração dos desafios conforme as diretrizes acima. Ele será orientado por um arquivo de instruções (chamado aqui de `AGENTES.md`) que descreve passo a passo o que deve ser feito quando um novo conceito ou tema é fornecido. Em resumo, o comportamento esperado do agente é:



1. **Analisar o Conceito de Entrada:** A entrada fornecida ao agente pode ser:

   - Um **conceito isolado** (e.g., `"Árvores Binárias"` ou `"Algoritmo de Dijkstra"`), indicando um tema específico de estrutura de dados ou algoritmo a ser explorado.
   - Um **texto descritivo** contendo vários conceitos e sugestões de problemas. Nesse caso, o agente deve identificar os diferentes tópicos mencionados e extrair deles possíveis desafios. Por exemplo, um texto que discuta **pilhas, filas e árvores** poderia levar o agente a propor desafios separados para cada uma dessas estruturas.

   O agente deve interpretar a entrada e **elencar um conjunto de desafios** apropriados. Cada desafio deve focar em um aspecto prático do conceito, cobrindo desde casos básicos até nuances mais avançadas ou armadilhas típicas.

2. **Proposição de Múltiplas Tarefas:** Com base na análise, o agente irá propor um **conjunto de tarefas** (um conceito geralmente rende múltiplos problemas). Para cada tarefa, ele deve idealmente fornecer:

   - Um breve **enunciado ou descrição** do problema a ser resolvido (pode ser inserido como comentário no código ou em docstring da função, para contextualizar o desenvolvedor).
   - O nome da função ou funcionalidade a ser implementada, de preferência indicando claramente o que ela faz (por exemplo, `balance_bst(tree)` para uma função que balanceia uma árvore de busca binária).

3. **Geração da Solução Interna e Casos de Teste:** Para assegurar que os testes serão confiáveis, o agente primeiramente **gera uma solução correta** para o problema internamente (sem necessariamente mostrar essa solução completa ao usuário). Com base nessa solução, ele então cria um arquivo de **testes automatizados** usando PyTest. Os testes devem:

   - Cobrir casos típicos e casos extremos (*edge cases*) do problema, incluindo entradas pequenas, entradas inválidas ou extremas, e cenários de pior caso para performance.
   - Verificar a correção do resultado e possivelmente a eficiência (por exemplo, garantindo que um algoritmo de ordenação ordene corretamente e possa lidar com uma lista grande dentro de limites de tempo razoáveis).
   - Incluir múltiplos testes atômicos usando asserções simples (`assert`), em vez de grandes testes monolíticos, para facilitar identificar qual aspecto falhou.

   *Racional:* A inclusão de testes robustos é crucial. Conforme destacado por especialistas, escrever testes automáticos ajuda a pensar em todos os casos de um problema e torna o processo de resolução mais eficiente[adamj.eu](https://adamj.eu/tech/2019/04/21/solving-algorithmic-problems-in-python-with-pytest/#:~:text=In either case%2C using automated,wish I knew this earlier). O PyTest será usado para esta finalidade por ser considerado uma ferramenta poderosa e simples para escrever testes em Python[adamj.eu](https://adamj.eu/tech/2019/04/21/solving-algorithmic-problems-in-python-with-pytest/#:~:text=In Python%2C there’s no better,in unittest).

4. **Criação de Arquivos de Código por Tarefa:** Para cada desafio, o agente criará pelo menos **dois arquivos**:

   - **Arquivo de Implementação (stub):** Contém o código inicial para a solução. Nele estarão definidas as funções/classes que o usuário deve implementar. Algumas partes do código podem vir prontas (por exemplo, estruturas de dados auxiliares ou funções utilitárias, caso o foco da tarefa seja outro). As partes principais a serem implementadas estarão marcadas:

     - Incluir um placeholder como `raise NotImplementedError()` dentro de funções não implementadas (isso fará qualquer chamada falhar explicitamente até que o usuário escreva a lógica, lembrando-o do trecho pendente)[stackoverflow.com](https://stackoverflow.com/questions/49346946/i-dont-understand-why-raise-notimplementederror-is-necessary-here-python#:~:text=,and there would be bugs). Alternativamente, poderia ser usado um simples `pass` ou um comentário `# TODO: implementar`, mas o uso de exceção deixa o comportamento mais explícito.

     - Exemplo de marcação no código:

       ```
       def balance_bst(root):
           # TODO: Implementar balanceamento da BST 
           raise NotImplementedError("Função balance_bst ainda não implementada")
       ```

       Acima, a assinatura e propósito da função são dados, mas a implementação fica a cargo do usuário.

     - Se for relevante, o agente também pode prover docstrings ou comentários explicando o que a função deve fazer, para contextualizar. Por exemplo:

       ```
       def balance_bst(root):
           """
           Rebalanceia uma árvore de busca binária (BST) dada sua raiz, retornando a raiz da nova árvore balanceada.
           """
           # ... estrutura de dados auxiliar ...
           raise NotImplementedError()
       ```

     - Qualquer estrutura de dados necessária para resolver o problema deve estar disponível. Por exemplo, se o desafio é sobre árvores, podemos incluir a definição de um nó de árvore binária:

       ```
       class TreeNode:
           def __init__(self, valor, esquerda=None, direita=None):
               self.valor = valor
               self.esquerda = esquerda
               self.direita = direita
       ```

       Dessa forma, o usuário não perde tempo implementando a estrutura base e pode focar no algoritmo (busca, inserção, balanceamento, etc.). Essas partes fornecidas devem estar corretas e bem testadas.

   - **Arquivo de Testes:** Contém vários métodos de teste usando PyTest, nomeados com prefixo `test_`. Por exemplo, `test_balance_bst()` poderia criar diversas árvores (balanceadas e desbalanceadas) e verificar se após chamar `balance_bst()` a árvore resultante atende às propriedades (diferença de alturas das subárvores não maior que 1, por exemplo). Os testes devem ser suficientemente descritivos e independentes. Cada arquivo de teste será focado apenas na funcionalidade daquele desafio e usará apenas elementos definidos no stub ou bibliotecas padrão do Python.

5. **Estrutura de Diretórios para os Desafios:** O agente deve organizar os arquivos criados de forma lógica no repositório. A sugestão é agrupar desafios por conceito em pastas separadas. Por exemplo:

   ```
   algorithms/                 # Diretório principal de desafios (nome sugestivo)
   ├── árvores_binarias/       # Pasta para desafios do conceito "Árvores Binárias"
   │   ├── __init__.py         # Torna a pasta um pacote Python (facilita imports nos testes)
   │   ├── balance_bst.py      # Arquivo de implementação (stub) para desafio 1
   │   ├── test_balance_bst.py # Testes automáticos para desafio 1
   │   ├── percurso_bfs.py     # Outro desafio dentro de árvores binárias (stub)
   │   └── test_percurso_bfs.py# Testes para esse outro desafio
   └── grafos/
       ├── __init__.py
       ├── dijkstra.py         # Desafio de algoritmo de caminho mínimo
       └── test_dijkstra.py
   ```

   Neste exemplo, os desafios de *árvores binárias* foram agrupados na pasta `árvores_binarias`. Cada desafio dentro dela tem arquivos nomeados de acordo com sua funcionalidade. Note que usamos nomes descritivos e em **snake_case** (letras minúsculas e sublinhados) tanto para módulos quanto para funções, seguindo as convenções do PEP 8[peps.python.org](https://peps.python.org/pep-0008/#:~:text=Modules should have short%2C all,use of underscores is discouraged). A inclusão de um arquivo `__init__.py` em cada diretório de conceito transforma-os em **pacotes Python**, o que ajuda o PyTest a importar corretamente os módulos durante a execução dos testes[docs.pytest.org](https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html#:~:text=pytest will find ,foo.bar.tests.test_foo). Com essa estrutura, mesmo que diferentes pastas possuam arquivos de teste com nomes iguais (por exemplo, múltiplas pastas contendo um `test_solution.py`), não haverá conflito porque cada arquivo de teste será importado dentro do namespace do seu pacote de conceito[docs.pytest.org](https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html#:~:text=pytest will find ,foo.bar.tests.test_foo)[docs.pytest.org](https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html#:~:text=pytest will find ,conftest). Em outras palavras, PyTest saberá diferenciar `árvores_binarias.test_balance_bst` de `grafos.test_balance_bst` caso nomes se repitam, graças à hierarquia de pacotes.

    

   **Importante:** Os arquivos de teste devem importar o código do próprio desafio de forma relativa ou absoluta conforme a estrutura definida. Por exemplo, `test_balance_bst.py` poderia conter:

   ```
   from .balance_bst import balance_bst, TreeNode
   ```

   Isso importa a função e classe do módulo `balance_bst.py` dentro do mesmo pacote. Essa abordagem funciona porque definimos o `__init__.py` e executaremos os testes a partir do diretório raiz do projeto, tornando os pacotes reconhecíveis no `PYTHONPATH` pelo PyTest[docs.pytest.org](https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html#:~:text=pytest will find ,foo.bar.tests.test_foo). Caso não utilizássemos pacotes, PyTest ainda poderia descobrir os testes, mas exigiria que os nomes de arquivos de teste fossem únicos globalmente ou ajuste manual de path[docs.pytest.org](https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html#:~:text=pytest will find ,conftest). Com a estrutura proposta, ganhamos melhor organização e escalabilidade.

6. **Revisão e Ajustes:** O agente deve, após gerar os arquivos, **verificar** (na medida do possível) se tudo está consistente:

   - **Consistência dos Testes:** Garantir que os testes realmente falham inicialmente (dado que a implementação está incompleta) e passariam se a implementação estivesse correta. Idealmente, o agente pode usar a solução interna gerada para executar os testes e validar que eles pegam falhas e passam com a solução completa.
   - **Ausência de Dependências Externas:** Checar que nenhum teste ou código está importando bibliotecas de terceiros ou módulos fora do padrão. Todos os desafios devem rodar em um ambiente Python padrão sem configurações extras. (Se desejado, pode-se até restringir o agente a usar apenas módulos built-in nos testes, a não ser que o propósito de um desafio seja justamente usar uma biblioteca específica, o que não parece ser o foco aqui).
   - **Legibilidade:** Garantir que os nomes de arquivos, funções e variáveis estão claros e aderentes às convenções Python (PEP8)[peps.python.org](https://peps.python.org/pep-0008/#:~:text=Modules should have short%2C all,use of underscores is discouraged). Isso inclui usar nomes em inglês ou português de forma consistente (idealmente inglês para código, a não ser que se prefira português dado o contexto; manter consistência é o mais importante).
   - **Isolamento:** Confirmar que não há *resíduos* de código ou referências cruzadas entre desafios. Por exemplo, um teste de um desafio não deve acidentalmente importar algo de outro desafio. Cada pasta/conceito pode ter seu próprio namespace isolado.

7. **Registro das Tarefas:** Opcionalmente, o agente pode atualizar um arquivo índice (como um `README.md` principal ou um índice dentro de cada pasta de conceito) listando os desafios disponíveis, suas descrições resumidas e talvez o status (implementado ou pendente). Isso ajudaria a navegar pelo repositório conforme ele cresce. Esse passo não é obrigatório, mas melhora a documentação.

Após todos esses passos, o agente terá criado a estrutura necessária para o usuário atacar os problemas. A interação então passa para o usuário, que irá abrir os arquivos de implementação gerados (`*.py` com `NotImplementedError`) e trabalhar para fazer os testes passarem.



## Convenções de Nomeação e Estilo

Para manter o repositório organizado e profissional, seguem algumas convenções que o agente deve aplicar ao gerar nomes de arquivos, pastas e elementos de código:



- **Nomes de Pastas (Conceitos):** Usar nomes descritivos e curtos, em minúsculas. Pode-se usar underscores para separar palavras se necessário. Ex: `arvores_binarias`, `grafos`, `ordenacao`. Se preferir, pode usar inglês nos nomes técnicos (`binary_trees`, `graphs`), dependendo do padrão escolhido para o projeto. O importante é consistência. (PEP 8 recomenda nomes de módulos/pacotes em letras minúsculas, com underscores para legibilidade[peps.python.org](https://peps.python.org/pep-0008/#:~:text=Modules should have short%2C all,use of underscores is discouraged)).
- **Nomes de Arquivos de Código:** Seguir o mesmo estilo do pacote. Idealmente o nome do arquivo indica a função principal ou desafio. Exemplos: `balance_bst.py`, `percurso_bfs.py`, `dijkstra.py`. Evitar nomes genéricos demais como `solution.py` repetido em várias pastas, pois isso dificulta identificar o conteúdo; em vez disso, incorporar o tópico no nome do arquivo. Além disso, nomes únicos evitam conflitos se os testes forem executados sem pacote (a PyTest por padrão importa testes como módulos globais se não detecta pacote, e nomes duplicados poderiam conflitar[docs.pytest.org](https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html#:~:text=pytest will find ,conftest)).
- **Nomes de Arquivos de Teste:** Sempre começar com `test_` (ou terminar com `_test.py`) para que o PyTest os reconheça automaticamente[fig.io](https://fig.io/manual/pytest#:~:text=,current directory and its subdirectories). De preferência, seguir com o mesmo nome do arquivo de código que testam. Exemplo: para `balance_bst.py`, usar `test_balance_bst.py`. Isso deixa claro o pareamento e facilita navegação. Dentro dos arquivos de teste, as funções de teste também devem ter nomes descritivos começando em `test_` e podem indicar o cenário: ex: `test_balance_bst_arvore_vazia()` , `test_balance_bst_desbalanceada_esquerda()`, etc.
- **Nomes de Funções e Classes:** Usar `snake_case` para funções e métodos, e `CamelCase` para classes, conforme convenção Python[peps.python.org](https://peps.python.org/pep-0008/#:~:text=Modules should have short%2C all,use of underscores is discouraged)[peps.python.org](https://peps.python.org/pep-0008/#:~:text=Class names should normally use,the CapWords convention). Por exemplo, `def insere_elemento(lista, valor):` para função, ou `class NodeArvore:` para classe (apesar de em muitos casos usaremos classes auxiliares simples como `TreeNode` em CamelCase, o que é aceitável por ser uma estrutura de dados). Variáveis e parâmetros também em letras minúsculas com underscores se composto.
- **Documentação e Comentários:** Incluir docstrings nas funções principais descrevendo o que fazem, seus parâmetros e retorno. Comentários podem ser utilizados para esclarecer partes complexas dos testes ou dos stubs. Manter os comentários em português ou inglês de maneira consistente, conforme decidido (por exemplo, podemos escrever enunciados de problema em português nos comentários para facilitar o entendimento, já que é um repositório pessoal de estudos).
- **Formatação:** Garantir que o código gerado pelo agente siga formatação PEP8 quando possível – por exemplo, indentação de 4 espaços, linhas não muito longas, etc. Isso não apenas mantém o código elegante, mas também evita distrações com estilo durante a resolução dos problemas.

Ao aderir a essas convenções, o repositório permanecerá limpo e fácil de escanear. Um desenvolvedor (ou o próprio usuário futuro) deve conseguir ver a lista de arquivos e entender que desafios estão ali e o que é esperado em cada um.



## Execução dos Testes Automatizados

Uma grande vantagem desta configuração é a facilidade de rodar os testes de todos os desafios a qualquer momento. O agente deve assegurar que, após a geração de desafios e implementação pelo usuário, a execução de **todos os testes de uma vez** seja simples:



- **Comando Único:** Estando no diretório raiz do repositório, o usuário deve poder rodar `pytest` (ou `python -m pytest`) e o PyTest automaticamente **descobrirá todos os arquivos de teste** em subdiretórios e os executará[fig.io](https://fig.io/manual/pytest#:~:text=,current directory and its subdirectories). Graças ao prefixo `test_` nos nomes e à estrutura de pastas com `__init__.py`, o framework encontrará os testes recursivamente. Isso executará a suíte completa, permitindo verificar em poucos segundos se todas as soluções implementadas até então estão corretas. O uso da opção `-q` (quiet) pode suprimir parte da verbosidade, mostrando um resumo mais limpo do resultado (útil quando há muitos testes).
- **Testes Isolados:** Se o usuário quiser focar em um único desafio, ele pode executar PyTest apontando para o diretório ou arquivo daquele desafio. Por exemplo, `pytest algorithms/arvores_binarias/test_balance_bst.py` rodaria apenas os testes desse problema. Alternativamente, pode-se usar a opção `-k` de PyTest para filtrar por nome de teste. O importante é que cada conjunto de testes funcione isoladamente também.
- **Feedback Rápido:** Os testes devem ser escritos de forma eficiente para rodarem rapidamente. Evitar loops muito grandes ou entradas gigantescas que atrasem o feedback (a não ser que o objetivo seja testar desempenho, mas mesmo assim isso pode ser feito de forma controlada). Como estamos rodando localmente, podemos ter testes mais pesados do que em plataformas online (por exemplo, testar uma lista de 1 milhão de elementos), mas deve-se equilibrar para não tornar a execução dos testes lenta demais a ponto de desincentivar sua execução frequente.
- **Manter Todos os Testes Verdes:** Conforme novos desafios forem adicionados e resolvidos, é importante incorporar a execução de todos os testes nos hábitos (por exemplo, antes de commitar mudanças, rodar `pytest` geral). O agente poderia até ajudar lembrando de rodar os testes após gerar novos desafios com soluções incompletas – embora esses testes falharão até que o usuário implemente as soluções, isso garante que o ambiente de teste está corretamente configurado. Depois que o usuário escrever o código faltante e os testes passarem, o repositório volta a ficar consistente. Ferramentas de CI (Integração Contínua) podem ser configuradas no futuro para rodar a suíte de testes a cada push, embora inicialmente não seja obrigatório.

## Exemplo de Uso do Agente

Para ilustrar concretamente, vejamos um exemplo de como o agente atuaria dado um conceito específico:

 

**Entrada do agente:** `"Árvores Binárias"`

 

**Saída esperada (resumo das ações do agente):**



1. **Identificação de desafios:** O agente decide propor *três tarefas* relacionadas a árvores binárias, cobrindo diferentes aspectos:

   - *Desafio 1:* **Balanceamento de BST** – Implementar uma função `balance_bst(root)` que receba a raiz de uma árvore de busca binária (possivelmente desbalanceada) e retorne a raiz de uma árvore equivalente balanceada (minimizando a altura).
   - *Desafio 2:* **Percurso em Largura (BFS)** – Implementar uma função `nivel_ordem(root)` (ou similar) que realize o percurso em largura (nivel a nivel) de uma árvore binária e retorne uma lista de valores em ordem de nível.
   - *Desafio 3:* **Verificar BST Válida** – Implementar `is_valid_bst(root)` que verifica se uma árvore binária satisfaz as propriedades de uma BST (todos nós à esquerda < raiz < todos à direita).

2. **Geração dos arquivos para cada desafio:** O agente cria uma pasta `algorithms/arvores_binarias/` (caso não exista) e dentro dela os arquivos:

   - `balance_bst.py` contendo a definição da classe `TreeNode` e a função `balance_bst` com corpo marcado para implementar. Inclui docstring explicando a tarefa e talvez uma função auxiliar pronta (por ex., função para extrair elementos da BST em ordem e construir balanceada a partir da lista, mas deixaria essa lógica para o usuário se for o foco do desafio).
   - `test_balance_bst.py` com testes:
     - Cria BSTs desbalanceadas (ex.: uma árvore degenerada tipo lista) e verifica que após `balance_bst` a altura diminui e a inorder traversal permanece ordenada igual à original.
     - Testa casos triviais (árvore vazia, árvore com um só nó, árvore já balanceada).
     - Testa performance de balanceamento em uma árvore grande (por exemplo, inserir 10000 valores sequencialmente para formar uma BST bem desbalanceada, balancear e checar se a altura resultante ~ log2(n)). *(Este último apenas se performance for uma preocupação explícita; caso contrário, pode-se omitir testes muito custosos.)*
   - `nivel_ordem.py` com função `nivel_ordem(root)` e possivelmente usando a mesma classe `TreeNode` (definida novamente ou importada de um módulo comum). Marcações de implementação onde o usuário deve fazer uma fila e iterar pelos níveis.
   - `test_nivel_ordem.py` com testes:
     - Monta manualmente uma árvore pequena e verifica que a saída da função são os valores por nível.
     - Testa uma árvore com vários níveis, incluindo nós faltantes, etc.
     - Testa árvore nula (None) retorna lista vazia.
   - `is_valid_bst.py` com função `is_valid_bst(root)` e stub.
   - `test_is_valid_bst.py` com testes:
     - Vários cenários de árvore válida e inválida (violações sutis, e.g. um nodo numa subárvore direita que é menor que a raiz ancestral).
     - Casos de um nó, nenhum nó, etc.

   Todos esses arquivos de teste começam com o prefixo `test_` e usam `assert` para comparar resultados esperados. Os nomes dos arquivos e funções seguem o padrão snake_case. A pasta `arvores_binarias` tem um `__init__.py` (pode estar vazio) para permitir imports relativos.

3. **Execução de exemplo:** O agente poderia (opcionalmente) simular a execução dos testes usando suas soluções internas:

   - Internamente verifica que `pytest algorithms/arvores_binarias/` resultaria em falhas, já que as implementações estão incompletas, mas os erros seriam do tipo `NotImplementedError`, indicando que o ambiente está pronto para o usuário implementar.
   - Se ativado em modo de *auto-verificação*, o agente poderia inserir temporariamente as soluções completas nos arquivos stub, rodar os testes para garantir que todos passam, e então reverter os stubs para o estado incompleto. Isso confirmaria que os testes estão corretos e que, de fato, basta implementar as partes marcadas para obter sucesso.

4. **Entrega do desafio:** O agente finaliza apresentando talvez um sumário:

   - Lista os desafios criados (“1. Balanceamento de BST, 2. Percurso em Largura, 3. Validação de BST”) e orienta que o usuário implemente cada um nos arquivos gerados até que `pytest` passe completamente em verde. Poderia também mencionar dicas ou a ordem recomendada (por exemplo, começar pelo percurso BFS pois ajuda a testar visualmente a árvore para depois usar no balanceamento, etc.), mas isso é extra.

Agora, com esses arquivos no repositório, o usuário abriria seu VSCode e começaria a implementar as funções em cada arquivo, executando `pytest` para verificar. Por exemplo, implementando `balance_bst` usando uma abordagem de *in-order traversal* para obter os valores em ordem e depois construindo uma árvore balanceada recursivamente. Ao terminar cada implementação, roda-se os testes daquele arquivo (ou todos) para confirmar a correção.

 

Assim, o ambiente se comporta como um “HackerRank” personalizado: cada tarefa é definida, testes verificam automaticamente a solução, e o usuário ganha feedback imediato. Tudo isso sem precisar de internet ou plataformas externas – o foco fica totalmente no código e no entendimento dos algoritmos.



## Considerações Finais

Com essa configuração, o repositório de estudos de algoritmos atenderá às necessidades de aprofundamento teórico e prático do usuário. O agente atuará como um gerador de desafios e *parceiro de estudo*, fornecendo problemas interessantes e garantindo que cada um vem acompanhado de validação automática. Algumas vantagens adicionais dessa abordagem:



- **Cobertura de Performance:** Os testes podem ser projetados não só para verificar correção, mas também para insinuar questões de performance. Por exemplo, o agente pode incluir testes com entradas grandes e comentar algo como “este teste deve rodar em poucos segundos” – indicando ao usuário que uma solução ingênua pode não ser adequada. Isso força a reflexão sobre complexidade de algoritmos em cada desafio, exatamente o tipo de conhecimento esperado em entrevistas de especialista.
- **Modularidade:** Novos conceitos podem ser adicionados incrementalmente. Cada pasta de conceito é um módulo independente. Se no futuro quiser separar por níveis de dificuldade ou categorias (por exemplo, *estrutura de dados básicas*, *algoritmos de grafos avançados*), bastaria reorganizar ou nomear as pastas apropriadamente.
- **Extensibilidade:** Embora inicialmente focado em Python, a estrutura poderia inspirar práticas similares em outras linguagens. Também, se desejado, pode-se incluir um *driver* (código main) para ler entrada e produzir saída de cada algoritmo, facilitando experimentação manual além dos testes – mas isso é opcional e secundário, dado que os testes já fornecem os exemplos de uso.

Em conclusão, as instruções acima servem para configurar o agente de forma clara e objetiva. Ao segui-las, o agente Codex deve conseguir transformar um conceito teórico em um conjunto concreto de desafios de programação no repositório, com tudo o que é necessário para praticar (menos a parte de escrever a solução, que fica como exercício do usuário). Esse equilíbrio permite **estudo ativo** e focado: o usuário gasta tempo pensando e codando soluções, enquanto o agente cuida da geração dos problemas e validação.

## Tarefas Disponíveis

### Linked Lists

- `reverse_linked_list.py` - reverter uma lista ligada simples.
- `detect_cycle.py` - verificar presen\xc3\xa7a de ciclos em uma lista ligada.
- `merge_sorted_lists.py` - mesclar duas listas ligadas ordenadas.

### Árvores Binárias

- `balance_bst.py` - balancear uma BST desbalanceada.
- `nivel_ordem.py` - percorrer a \xc3\xa1rvore em ordem de n\xc3\xadvel.
- `is_valid_bst.py` - verificar se uma \xc3\xa1rvore \xc3\xa9 uma BST v\xc3\xa1lida.
- `search_bst.py` - buscar um valor em uma BST.

### Queues

- `simple_queue.py` - fila b\xc3\xa1sica com opera\xc3\xa7\xc3\xb5es de enfileirar e desenfileirar.
- `queue_two_stacks.py` - fila implementada com duas pilhas.
- `circular_queue.py` - fila circular de tamanho fixo.

### Stacks

- `validate_parentheses.py` - verificar se uma sequência de parênteses está balanceada.
- `min_stack.py` - pilha que retorna o valor mínimo em O(1).
- `evaluate_postfix.py` - avaliar expressões em notação pós-fixa.

