# Project 16: Modern Project Scaffolder & pyproject.toml Generator

### Overview
This project targets declarative Python packaging specifications, metadata configuration management, and robust infrastructure automation patterns. Senior Python engineers do not build development repositories manually from scratch. Instead, they use standardized templating generators to eliminate human variance, align dependencies, enforce quality constraints uniformly, and instantly establish repeatable test and integration loops.

You will engineer a structural command-line scaffolding utility that prompts an operator for metadata and functional configurations, compiles them dynamically, and systematically emits a fully functional, production-ready project directory tree. The output will feature a unified **PEP 621 `pyproject.toml` configuration**, localized testing harnesses via `pytest`, static code quality hooks via `pre-commit`, and continuous validation workflows via **GitHub Actions CI**.

---

### The Architecture Contract

Your generated project infrastructure output must strictly satisfy these modern Python standards:

#### 1. Unified PEP 621 `pyproject.toml` Architecture
Gone are the days of legacy `setup.py`, `setup.cfg`, `requirements.txt`, and separate linting configuration files. Your engine must compile a singular, clean, and centralized `pyproject.toml` mapping file:
* **The Build System Block**: Establish a standardized build ecosystem using explicit `hatchling`, `flit`, or `setuptools.build_meta` packaging declarations.
* **Metadata & Dependency Injection Matrix**: Dynamically map the target project's core dependencies inside the standard `dependencies = [...]` array list based on the user's feature choices. If `fastapi` is requested, inject the proper web frameworks. If `cli` is selected, inject interactive libraries like `click` or `typer` along with a valid executable routing entry point under `[project.scripts]`.
* **Dev Extras & Linter Settings**: Isolate developer environments within a clean `[project.optional-dependencies]` dev block (e.g., `dev = ["pytest", "pytest-cov", "ruff", "mypy"]`). Embed direct configuration segments for code formatters and typing parameters inside clean structural blocks like `[tool.ruff]` and `[tool.mypy]`.

#### 2. Declarative Quality Controls (`.pre-commit-config.yaml`)
If the user includes the `pre-commit` feature flag during initialization, your script must emit a robust `.pre-commit-config.yaml` file at the repository root. This file must map clean upstream hooks to intercept commits before they hit version history:
* Integrate `ruff-pre-commit` to handle fast syntax cleaning and import organization.
* Integrate `mirrors-mypy` to execute static type validations over your file sets before letting a commit proceed.

#### 3. Production Test Harness & Fixtures (`conftest.py`)
To ensure developers can write tests immediately after initialization, your generator must output a ready-to-use testing environment within the `tests/` directory:
* Write a standard `conftest.py` script containing common testing fixtures.
* If the user selects the `fastapi` feature flag, automatically inject pre-configured, reusable components: an asynchronous testing framework fixture (`async_client` via `httpx.AsyncClient`), a standard `test_client` via `fastapi.testclient.TestClient`, a mock database hook (`db_session`), and an extensible entity factory (`make_user`).

#### 4. Automated CI Actions Pipelines (`.github/workflows/ci.yml`)
Your scaffolder must lay down the infrastructure for immediate, automated verification by writing a declarative GitHub Actions integration workflow file:
* The build flow must trigger automatically on any `push` or `pull_request` event directed toward your `main` or `master` branches.
* Configure a standardized matrix execution pipeline: spin up a clean Ubuntu runner image (`ubuntu-latest`), check out the code base, initialize the user-specified Python version, cache virtualenv footprints, run all code style validators, and execute the test pipeline using code coverage telemetry parameters (`pytest --cov`).

---

### Technical Signposts & Hints

#### 1. Escaping Literal Template Codes inside Python Source Generation Blocks
When writing text compilation templates that produce secondary configuration files containing native syntax characters (such as double brackets `[[matrix.python-version]]` in GitHub Actions configurations or dictionary definitions in Python files), standard f-string interpolation routines will fail. 
* Remember to double your bracket characters (`{{` and `}}` or `[[` and `]]`) to treat them as literal characters inside your generation code.

#### 2. Clean Directory Trees via Pathlib Contexts
Avoid legacy string manipulations when navigating and creating directory structures. Leverage the clean, modern API of Python's built-in `pathlib.Path`:
```python
# Create recursive subdirectory locations safely
target_src_dir = root_path / "src" / project_name
target_src_dir.mkdir(parents=True, exist_ok=True)

```

---

### Constraints Checklist

* [ ] No manual file system shell operations (e.g., calling out to `os.system('mkdir ...')`). All operations must use the safe, built-in `pathlib` API.
* [ ] The generated `pyproject.toml` must be perfectly valid and ready to install immediately using the standard command `pip install -e '.[dev]'`.
* [ ] The engine must handle missing optional feature flags gracefully, producing a minimal, clean, and perfectly valid base project layout if no special extensions are selected.
* [ ] Every functional helper, file writer generator, and directory coordinator block must include explicit, valid PEP 484 type hint definitions.

```

---

### Why this works perfectly for Chapter 16:
* **The Paradigm Unification**: Forcing students to synthesize a modern, PEP 621-compliant repository layout consolidates everything they have learned about environment setup, testing patterns, and linting configurations into a single, cohesive project.
* **The Automation Epiphany**: Moving from writing business logic to writing developer tools shifts students' perspective from simple coding to professional-grade systems engineering. They realize that software development is about building predictable, automated pipelines that enforce high quality standards at every step of the lifecycle.

```