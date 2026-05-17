# Project 14: Live Chart Builder

### Overview
This project targets architectural encapsulation, code generation patterns, and empirical UI engineering. True backend developers do not view plotting libraries as personal lifestyle preferences. Instead, they classify them objectively based on their operational output capabilities: static pixel buffers for publications (**Matplotlib**), high-level automated statistical charts (**Seaborn**), or rich client-side runtime canvas graphics (**Plotly**).

You will engineer a diagnostic command-line visualization workbench using the **Bridge and Factory Software Design Patterns**. Your tool will ingest data shapes, dispatch rendering profiles, and act as a meta-compiler—printing valid, production-ready visualization scripts immediately upon completion.

---

### The Architecture Contract

Your implementation must strictly satisfy these cross-platform engine layout directives:

#### 1. Matplotlib Structural Engineering Requirements
When running via the explicit `matplotlib` engine flag:
* Never utilize the implicit global state-machine layers (`plt.bar()`). You must enforce strict object-oriented sub-plot canvas configurations:
  ```python
  fig, ax = plt.subplots(figsize=(10, 6))
  

```

* All generated files must preserve publication-grade clarity parameters, outputting to a target path labeled `output.png` carrying a minimum resolution constraint metric of **300 DPI** (`plt.savefig('output.png', dpi=300, bbox_inches='tight')`).

#### 2. Seaborn Declarative Themes

When rendering via the high-level statistical `seaborn` matrix engine:

* The emitted script code telemetry must encapsulate global theme context controls explicitly before triggering any plotting actions:
```python
sns.set_theme(style="darkgrid", palette="muted")


```



```
* Ensure that structural axis components are cleanly labeled utilizing the source dataframe columns automatically.

#### 3. Plotly Dark Mode Runtime Assets
When executing interactive graphics via the web-native `plotly` engine:
* Data elements must render inside responsive browser-ready configurations. Emitted telemetry scripts must include configuration definitions tracking dark theme modes (`template='plotly_dark'`).
* The engine must write its structures to a client-side layout block (`output.html`) and programmatically command the local environment loop to spawn the dashboard directly inside an active browser window using Python's native `import webbrowser` stack.

#### 4. Matrix Evaluation Dashboard (`--compare`)
If the operator executes the workspace passing the `--compare` boolean flag:
* Your script must run all three concrete engines sequentially over the target parameters.
* Assemble a single dashboard document (`comparison_report.html`) arranging the outputs into a three-column interface framework. 
* Each column must present the graphic element positioned above a markdown/code container exposing the exact snippet used to compile that specific asset block.

---

### Technical Signposts & Hints

#### 1. Elegant String Escaping for Dynamic File Templates
When compiling code blocks containing raw strings that must read structural input references literally (e.g., parsing a hardcoded file string like `pd.read_csv('sales.csv')`), ensure your generator template blocks isolate string literals from your active script context components using alternative inner-bracket configurations:
```python
# Escaping quotation tokens cleanly inside interpolation structures
telemetry_block = f"""
import pandas as pd
df = pd.read_csv("{args.file}")
"""

```

#### 2. The Correlation Matrix Isolation Check

When handling a request for a `heatmap` type rendering execution, your engine must automatically calculate a numerical covariance cross-section directly over numeric features beforehand. Ensure your telemetry maps this operational sequence accurately:

```python
# Code telemetry structure generation for structural matrix inputs
matrix_snippet = """
corr_matrix = df.select_dtypes(include=['number']).corr()
"""

```

---

### Constraints Checklist

* [ ] No structural cross-contamination: The `MatplotlibEngine` class wrapper must never import `plotly`, and vice-versa.
* [ ] All code components output to the stdout terminal must be valid, copy-pasteable blocks ready to run as independent Python scripts.
* [ ] The engine must handle parsing clean data strings safely if a column mapping context features white-spaces or non-standard characters.
* [ ] Every functional method signature, interface declaration, and dispatch hook must carry explicit, compile-checked PEP 484 type annotations.

```

---

### Why this works perfectly for Chapter 14:
* **The Paradigm Demystification**: Forcing students to build code telemetry strings for both state-based (`matplotlib`) and declarative vector-mapping engines (`plotly`/`seaborn`) gives them an intuitive mental model of Python visualization architectures.
* **tooling-First Mindset**: The `--compare` matrix dashboard shifts their perspective away from viewing visualization as an interactive Jupyter Notebook task. Instead, it positions visualization as a scalable, automated engine capable of serving data infrastructure apps.

```