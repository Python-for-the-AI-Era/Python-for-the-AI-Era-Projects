# Project 12: ML Selector & Code Generator

### Overview
This project targets meta-programming and automated machine learning (AutoML) architecture patterns. True machine learning engineers do not re-write boilerplate pipeline orchestration code by hand for every unique project. Instead, they build robust software templates that evaluate data profiles—such as row volumes, dimensional features, and class representation metrics—to algorithmically compile complete, runnable, and highly optimized modeling files.

Your tool will analyze a given data constraint profile through the CLI and generate a fully functional, syntax-valid Python script (`solution_lgb.py`) containing data pipelines, hyperparameter search spaces, explainability blocks, and a deep learning alternative.

---

### The Architecture Contract

Your generated target code output must strictly fulfill these structural criteria:

#### 1. Data-Driven Algorithm Selection Engine
Your script must implement an inference ruleset to analyze dataset configurations:
* If data footprint volumes exceed 10,000 rows with mixed data types and the `--imbalanced true` constraint flag is set, your tool must dynamically recommend **LightGBM** as the core model.
* The system output log must state an explicit structural justification, print out the chosen Cross-Validation strategy (`StratifiedKFold`), and map target metric footprints accurately (e.g., scoring via `ROC-AUC` + `PR-AUC` rather than raw accuracy metrics).

#### 2. Fully Automated Data Preprocessing Pipelines
The emitted script must wrap data preprocessing inside an explicit scikit-learn `ColumnTransformer`. 
* You must generate distinct, partitioned pipeline execution tracks: standard scaling (`StandardScaler`) mapping across numerical feature targets, and structural encoding (`OneHotEncoder(handle_unknown='ignore')`) handling categorical string dimensions cleanly.

#### 3. Advanced Automated Tuning (`Optuna`)
The generated optimization block must inject a complete `optuna` search study setup.
* **The Constraints**: The code must define a search space tracking exactly **8 individual hyperparameters** simultaneously (including `learning_rate`, `num_leaves`, `max_depth`, and `min_child_samples`).
* To prevent computing resource waste on unpromising parameters, configure the study engine utilizing an explicit `optuna.pruners.MedianPruner()` strategy running over 100 trials.

#### 4. Post-Hoc Model Explainability (`SHAP`)
A black-box model is unviable in an enterprise deployment. The script must generate a comprehensive diagnostic section using `SHAP` (SHapley Additive exPlanations):
* Instantiate a `shap.TreeExplainer` specifically targeted to parse your trained LightGBM model tree.
* Inject procedural calls to render both global feature attribution distributions (`shap.summary_plot` / beeswarm format) and localized instance deductions (`shap.plots.waterfall`).

#### 5. Native Alternative Deep Learning Topology (`PyTorch`)
As a robust alternative framework option, your code-generator must write a complete, standalone `PyTorch` model architecture block at the tail end of the generated file:
* Build a standard, flexible subclass extending `nn.Module` containing a minimum of **3 deep linear layers** complete with activation functions (`nn.ReLU`) and dropout normalization paths.
* Generate a complete, operational training loop incorporating an internal custom tabular `Dataset` structural data loader container map matching your exact feature input size inputs.

---

### Technical Signposts & Hints

#### 1. Managing Text Blocks via Multi-line Python Docstrings
To effectively generate valid Python source files without messy nested string concatenation expressions, utilize Python's multi-line raw docstring declaration tokens (`'''`). Ensure that internal parameter replacements use clean, modern `.format()` expressions or explicit f-string token tags:
```python
# Conceptual layout of source code generation template engine
generated_code = f'''
def train_model(X, y):
    model = lgb.LGBMClassifier(scale_pos_weight={calculated_ratio})
    model.fit(X, y)
    return model
'''

```

#### 2. Resolving the Class Imbalance Scale Factor

When a dataset contains a high class imbalance, standard cross-entropy or binary log-loss functions can fail. Your generator tool must look at the `--imbalanced true` parameter input flag and pass an automated tuning calculation strategy to the generated LightGBM keyword parameters directly:

```python
# Balance weight ratios scale calculation parameter insertion rule
scale_pos_weight = total_negative_samples / total_positive_samples

```

---

### Constraints Checklist

* [ ] The output file (`solution_lgb.py`) must be completely runnable out-of-the-box using mock datasets without throwing structural python `SyntaxError` issues.
* [ ] The generated scikit-learn pipeline structure must explicitly handle early stopping metrics gracefully without leaking test validation folds.
* [ ] The generated PyTorch alternative block must explicitly check for hardware availability, defaulting parameters to use GPU acceleration contexts (`cuda` or `mps`) if native drivers exist on the host platform.
* [ ] No hardcoded column totals; structural size values inside the `ColumnTransformer`, `SHAP` array lengths, and `PyTorch` network input parameters must dynamically match the input `--features` count supplied to the CLI tool.

```

---

### Why this works perfectly for Chapter 12:
* **The Code-as-Data Transition**: Forcing students to write a script that generates *another script* helps them move past viewing code as a static file, and instead see it as a dynamic engine they can manipulate.
* **The Multi-Framework Reality**: Seeing a Scikit-Learn pipeline, a LightGBM booster, an Optuna optimizer, a SHAP explorer, and a PyTorch neural network laid out side-by-side in a single file solidifies how different machine learning tools cooperate within a production environment.

```