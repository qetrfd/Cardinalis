# Cardinalis

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux-lightgrey)
![AI](https://img.shields.io/badge/AI-Local%20Assistant-purple)

**Cardinalis** is a modular AI desktop assistant designed to interact with and control a computer through voice commands and intelligent agents.

The goal of the project is to create a **fully local personal assistant** capable of helping with computer tasks, automation, and system interaction without relying on cloud services. Cardinalis combines voice interaction, agent-based task execution, contextual memory, and system utilities into a unified architecture.

The system is built with scalability in mind, allowing new tools, agents, and features to be added without modifying the core system.


⚠️ Important:
This repository represents a very early alpha version of Cardinalis. The project is still under heavy development and the architecture, features, and modules may change significantly as the system evolves.

---

# Demo Concept

Cardinalis is designed to function similarly to a local operating assistant.

Example interactions:

```
"Oye Cardinalis, abre el navegador"
"Cardinalis, sube el volumen"
"Cardinalis, abre mi carpeta de proyectos"
```

The assistant processes the voice command, routes it through the core system, activates the correct agent, and executes the action.

---

# Architecture

The system is built around a modular structure that separates responsibilities between voice processing, agents, and system utilities.

```
User
 │
 ▼
Voice System
 │
 ▼
Core Engine
 │
 ├── Agents
 │      ├── System Agent
 │      ├── File Agent
 │      └── Utility Agent
 │
 ├── Tools
 │
 └── Memory System
 │
 ▼
System Execution
```

This architecture makes the system flexible and easy to extend with additional capabilities.

---

# Features

* Voice-based computer interaction
* Modular agent architecture
* Local voice synthesis
* Context and memory system
* Desktop graphical interface
* Automation tools
* Extensible design for new AI capabilities

---

# Project Structure

```
Cardinalis
├── agents/        # AI agents responsible for tasks
├── core/          # Core orchestration logic
├── memory/        # Context and memory management
├── tools/         # System utilities and automation
├── ui/            # Graphical interface
├── voice/         # Speech processing system
├── voices/        # Voice synthesis models
├── main.py        # Application entry point
└── .gitignore
```

---

# Installation

Clone the repository:

```
git clone https://github.com/qetrfd/Cardinalis.git
cd Cardinalis
```

Create a virtual environment:

```
python -m venv .venv
```

Activate the environment.

Mac/Linux:

```
source .venv/bin/activate
```

Windows:

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Running the Assistant

Start the assistant:

```
python main.py
```

---

# Technologies

Cardinalis integrates several technologies to build a local AI assistant.

* Python
* PyTorch
* ONNX Runtime
* PySide6
* Speech recognition libraries
* Local voice synthesis models

---

# Roadmap

Planned improvements and features include:

* Wake-word detection ("Oye Cardinalis")
* Expanded system automation
* Improved voice interaction
* Enhanced memory and context system
* Plugin-based tool system
* Multi-agent task orchestration

---

# Project Vision

The long-term vision of Cardinalis is to build a powerful **local AI operating assistant** capable of controlling and assisting with daily computer tasks while maintaining user privacy and flexibility.

---

# License

This project is intended for educational and experimental purposes.
