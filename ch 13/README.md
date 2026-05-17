# Project 13: Prompt Engineering Lab

### Overview
This project targets cognitive software engineering and structural LLM meta-programming. True AI engineers do not copy-paste text prompts manually inside standard browser portals; they treat prompts as modular, programmatic assets that are dynamically composed, verified, and orchestrated through clean software layers. 

You will design an interactive terminal lab utility that maps five core LLM operational strategies (**Basic**, **Few-Shot**, **Chain-of-Thought**, **Retrieval-Augmented Generation**, and **Autonomous ReAct Agents**). Your application must track its internal configuration structures, outputting the exact, runnable **LangChain Expression Language (LCEL)** pipeline code alongside its execution telemetry.

---

### The Architecture Contract

Your implementation must strictly satisfy these declarative AI framework guidelines:

#### 1. Functional Composition via LCEL Pipes (`|`)
Do not construct legacy, imperative orchestration wrappers to call your language models. Your generated code output blocks must leverage LangChain's modern, functional pipe composition framework (`|`). This treats prompts, models, vector stores, and output parsers as independent, immutable code pieces wrapped inside standard unified execution blocks (`Runnable` modules):
```python
# The standard structural LCEL paradigm
chain = preprocessing_dictionary | prompt_template | language_model | output_parser

```

#### 2. Few-Shot Isolation and Structural Externalization

Never hardcode few-shot dynamic context data arrays inside your core Python script files.

* **The Rule**: You must store your example key-value maps inside a structured, externalized tracking document named `prompt_examples.yaml`.
* Your script must programmatically load this asset, transform the entries into structured input dictionaries, and compile them into a unified execution string using LangChain's `FewShotChatMessagePromptTemplate` blueprint.

#### 3. Strict Boundary Parsing ( tags)

When evaluating deep logical reasoning pipelines through **Chain-of-Thought (CoT)** mechanisms, language models need space to trace hidden paths before answering.

* Instruct the agent to think step-by-step inside the system prompt and enforce an absolute output bounding tag constraint format (e.g., `<answer>FINAL_RESULT</answer>`).
* Your emitted code must implement a custom Python class extending `BaseOutputParser` that utilizes regex patterns to target, capture, and return *only* the string payload enclosed inside the raw answer tag markers, discarding the messy tracking thoughts.

#### 4. Deterministic RAG Data Flows

Your RAG mode implementation must build an automated file loading system:

* Slice textual information components using the `RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)`.
* Ingest information layers through local embedding calculations using vector collections via `Chroma` or `Faiss`.
* Configure your search criteria explicitly to leverage **Maximal Marginal Relevance (`search_type='mmr'`)** with settings set to `k=4` and `fetch_k=20`. This ensures high information diversity among retrieved text chunks, filtering out repetitive blocks before they overwhelm the context window.

---

### Technical Signposts & Hints

#### 1. Formatting Nested Braces in Code-Generation Templates

When writing string interpolation blocks that generate secondary Python file structures, standard Python f-strings can break or throw parsing errors if they encounter native JSON blocks or dictionary brackets (like `{'context': ...}`).

* To escape structural programmatic curly braces safely inside an f-string template, double the character tokens: use `{{` to output `{`, and `}}` to output `}`.

#### 2. Agent Trace Debugging Logs

When testing your autonomous ReAct agent loop configuration, link standard routing tools (such as local directory search and calculators) into an operational `AgentExecutor`. To capture and print the detailed loop thought traces to the terminal screen, ensure you set the debugging telemetry options directly within your instantiation calls:

```python
# Enable clear console thinking metrics
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

```

---

### Constraints Checklist

* [ ] No raw string concatenations for prompt assemblies; all prompt entities must instantiate safely via formal `langchain_core.prompts` classes.
* [ ] The generated RAG block code must handle empty text parameters gracefully without raising downstream exceptions.
* [ ] All code output segments must use modern OpenAI chat interface models (`ChatOpenAI`) rather than legacy text completion wrappers.
* [ ] Every component method, prompt compiler constructor, and utility processing function must maintain explicit PEP 484 static type definitions.

```

---

### Why this works perfectly for Chapter 13:
* **The Modularization Realization**: Forcing students to manage prompts as code objects strips away the illusion of "magic text", showing them that prompts can be unit tested, modularized, and version controlled exactly like database schemas.
* **The LCEL Paradigm Shift**: Writing code that outputs functional LCEL strings teaches them how to design clean, composable data-flow architectures. They learn that a modern LLM application is essentially a functional pipe network—where data streams through loaders, gets enriched by context vectors, transforms via prompts, and parses down to strict structural outputs.

```