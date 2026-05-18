# Project 17: Security & Cloud Quiz Lab

### Overview
This project targets state machine tracking, reactive user-interface routing, and cloud-native security principles. Real-world application developers do not simply guess how memory allocations behave or how access keys are handled; they continuously audit their systems against security standards like OWASP and AWS cloud architecture patterns.

You will engineer an analytical, interactive browser-based verification dashboard using **Streamlit**. Your application will act as a robust state engine that guides an operator through an automated assessment matrix. Upon completion, the tool transitions into a data-science reporting view—aggregating scores, evaluating skill tier bands, and compiling categorical visual metrics using **Plotly**.

---

### The Architecture Contract

Your Streamlit application must strictly satisfy these functional UI and domain-specific requirements:

#### 1. The Session State Machine Matrix
Streamlit operates on an immediate-mode execution model: any user action or widget toggle forces the entire Python file to execute from top to bottom. To prevent variable values from resetting on every render cycle, you must strictly manage tracking structures using `st.session_state`.
* Your state engine must track current indexes (`q_index`), raw cumulative score metrics (`score`), quiz completion boundaries, and an operations log list recording previous selections for subsequent statistical evaluations.

#### 2. Comprehensive Security & Cloud Question Bank
Your tool must provide an evaluation engine tracking exactly **10 highly comprehensive multiple-choice items** across these specific architectural challenges:
* **Password Hashing**: Why memory-hard options like `argon2` outclass single-flight cryptographic functions (`SHA-256`) when mitigating high-throughput GPU brute-force attacks.
* **JWT Claims & Signatures**: Evaluating token verification flows, protecting token secrets, and understanding standard claims (`iss`, `exp`, `sub`).
* **Fernet Guarantees**: Understanding symmetric authenticated encryption (using AES-128 in CBC mode with an HMAC signature) to guarantee confidentiality *and* data integrity.
* **OWASP Top 10 Defenses**: Mitigating critical attack vectors like SQL Injection, Cross-Site Scripting (XSS), and Broken Object Level Authorization (BOLA).
* **S3 Presigned URL Lifecycles**: Enforcing absolute time constraints, credential bindings, and permission limitations on temporary resource download tokens.
* **DynamoDB Key Topologies**: Designing high-performance partition keys (`PK`) and sort keys (`SK`) to prevent hot partitions and optimize querying.
* **SQS Visibility Timeouts**: Managing message processing intervals to prevent race conditions or duplicate deliveries across distributed worker nodes.
* **The `secrets` Module vs `random`**: Why standard pseudo-random number generators (PRNGs) fail security compliance and why cryptographic tasks require the operating system's true entropy sources (`secrets`).
* **Timing Attack Prevention**: Implementing fixed-duration string comparisons using `hmac.compare_digest()` to stop side-channel execution analysis.
* **KMS Key Rotation**: Evaluating internal operational patterns for cryptographic material renewal without breaking retro-active archive decryption capabilities.

#### 3. Dual Operational Core Modes
Your application dashboard must adapt dynamically via a sidebar interface state flag:
* **Practice Mode**: When users submit an entry, evaluate their choice immediately. Display a contextual explanation block using green (`st.success`) or red (`st.error`) notification frames before unlocking progression controls.
* **Quiz Mode**: Suppress mid-test feedback completely to emulate formal testing standards. Track user actions silently, proceed through the cards, and defer all validation, feedback metrics, and explanation panels to the final dashboard screen.

#### 4. Analytics Report Card & Badge Matrix
When the quiz state marks completion, swap out the main testing component view and present a rich visualization dashboard:
* **The Badge Rank Engine**: Calculate total percentage performance and assign an explicit certification title to the user:
  $$\text{Score Rating} = \begin{cases} \text{Novice} & \text{Score } < 6 \\ \text{Practitioner} & 6 \le \text{Score } \le 8 \\ \text{Expert} & \text{Score } \ge 9 \end{cases}$$
* **Plotly Data Categorization Engine**: Convert the operational tracking logs into a structural Pandas DataFrame. Aggregate metrics grouped by category, and output an active categorical distribution bar graph (`px.bar`) highlighting correct vs incorrect allocations to map precisely where the student's operational weaknesses lie.

---

### Technical Signposts & Hints

#### 1. Preventing Index Out of Bounds Mutations
When handling button-triggered state mutations, always evaluate if the updated `q_index` pointer exceeds the total length boundary of the questions array matrix before altering layout trees:
```python
# Transition safely between quiz mode states
if st.session_state.q_index >= len(QUESTIONS) - 1:
    st.session_state.quiz_complete = True
else:
    st.session_state.q_index += 1
st.rerun()

```

#### 2. Forcing Component Reruns via `st.rerun()`

When mutating state pointers inside secondary conditional blocks (like resetting the entire application lifecycle from a deep sidebar context menu), invoke `st.rerun()` immediately. This breaks the old execution loop and forces Streamlit to rebuild the view from scratch using the brand-new structural context variables.

---

### Constraints Checklist

* [ ] No utilization of local file-system caching hacks to preserve quiz state; all parameters must read and write exclusively through native `st.session_state` mappings.
* [ ] Ensure all individual input radio choices assign selection values uniquely without leaking previous question entries into subsequent question nodes.
* [ ] The final visualization layout must be highly readable and look professional; do not leave raw unformatted tables exposed to the user.
* [ ] Every concrete evaluation layout function, session state orchestrator tracker, and visualization building pipeline routine must preserve explicit PEP 484 static type definitions.

```

---

### Why this works perfectly for Chapter 17:
* **The State Isolation Epiphany**: Streamlit's structural layout forcing code to evaluate top-down on every user interaction is highly unique. Building this app helps students truly internalize the mechanics of data mutations, state persistence, and stateless UI design paradigms.
* **The Professional Security Shift**: Writing out 10 distinct, production-grade cloud security explanations forces students to stop treating security as an afterthought. It transforms security from a vague concept into a tangible, measurable set of specific software choices.

```