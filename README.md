# Highspeed Flow Calculator

> **AE339 — High-Speed Aerodynamics | IIT Bombay**

## 📌 Overview

The **Highspeed Flow Calculator** is designed to provide flow parameters for common high-speed compressible-flow problems.

The calculator covers three scenarios:

| Flow Scenario | Description |
|---|---|
| **Isentropic Flow** | Calculation of flow parameters for isentropic compressible flow |
| **Normal Shock** | Calculation of flow parameters across a normal shock |
| **Oblique Shock** | Calculation of flow parameters across an oblique shock |

The underlying theory and formulae used by the calculator are documented in the accompanying project report. The complete implementation is written in **Python**.

---

## 📂 Project Structure

```text
.
├── dist/
│   └── FlowCalculator.exe
│
├── src/
│   ├── flowCalculator.py
│   └── main.py
│
└── Report.pdf
```

### `dist/`

Contains the executable:

```text
FlowCalculator.exe
```

Run the executable from a terminal to use the calculator without directly running the Python source code.

### `src/`

Contains the Python source code:

- **`flowCalculator.py`** — Contains the `calculator` class and the underlying calculation logic.
- **`main.py`** — Contains the user interface through which the calculator is operated.

### `Report.pdf`

Contains the final project report, including the underlying theory and formulae used by the calculator.

---

## 🚀 Running the Calculator

### Using the executable

The easiest way to use the calculator is to run:

```text
dist/FlowCalculator.exe
```

Alternatively, navigate to the `dist` directory in a terminal and run:

```bash
FlowCalculator.exe
```

### Running from source

The source implementation is located in the `src` directory.

```bash
python src/main.py
```

---