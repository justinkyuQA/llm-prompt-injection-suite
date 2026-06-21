# LLM Prompt Injection Suite

A modular toolkit for evaluating prompt injection vulnerabilities, adversarial behaviors, and instruction bypass techniques in Large Language Models (LLMs).

---

# Screenshots

## Batch Evaluation

![Batch Evaluation](screenshots/01-batch-evaluation.jpg)

## Project Structure

![Project Structure](screenshots/02-project-structure.jpg)

## Attack Library

![Attack Library](screenshots/03-attack-library.jpg)

## Attack Datasets and Results

![Attack Datasets and Results](screenshots/04-attack-datasets-and-results.jpg)

## Scoring Engine Output

![Scoring Engine Output](screenshots/05-scoring-engine-output.jpg)

---

# Overview

The LLM Prompt Injection Suite is a research-oriented project focused on testing the resilience and safety boundaries of modern AI systems.

This toolkit is designed to help researchers, developers, and security practitioners:

- Evaluate prompt injection resistance
- Analyze jailbreak effectiveness
- Test instruction hierarchy handling
- Measure safety policy robustness
- Build datasets for adversarial AI testing
- Automate evaluation workflows

The project is intended for defensive security research, model evaluation, and AI alignment experimentation.

---

# Features

## Current Features

- Prompt injection testing
- Batch evaluation runner
- Direct injection datasets
- Instruction override datasets
- Prompt leakage datasets
- Roleplay attack datasets
- JSON result generation
- Injection success scoring
- Modular Python structure
- Screenshot documentation

## Planned Features

- Automated fuzzing engine
- Payload mutation system
- Advanced scoring metrics
- Multi-model comparison
- Local LLM integration
- Docker deployment support
- Reporting dashboard
- JSON/CSV export support

---

# Project Structure

\`\`\`
llm-prompt-injection-suite/
├── prompts/
├── results/
├── screenshots/
├── src/
├── README.md
├── RELEASE.md
└── LICENSE
\`\`\`

---

# Installation

\`\`\`bash
git clone https://github.com/justinkyuQA/llm-prompt-injection-suite.git

cd llm-prompt-injection-suite

pip install -r requirements.txt
\`\`\`

---

# Usage

Run the batch evaluation suite:

\`\`\`bash
python src/run_all.py
\`\`\`

Run the evaluator manually:

\`\`\`bash
python src/evaluator.py --dataset prompts/direct_injection.txt
\`\`\`

---

# Research Goals

This project explores:

- Adversarial prompting
- Prompt injection vectors
- Instruction override attacks
- Context poisoning
- Prompt leakage
- Evaluation methodologies for AI systems

---

# Ethical Use

This repository is intended strictly for:

- Defensive security research
- Educational purposes
- AI safety evaluation
- Authorized testing environments

Users are responsible for complying with all applicable laws, platform policies, and responsible disclosure practices.

---

# Roadmap

## v1.0

- Prompt injection datasets
- Batch evaluation framework
- JSON result generation
- Screenshot documentation
- Public release

## v1.1

- Mutation engine
- Expanded attack corpus
- Enhanced scoring metrics

## v2.0

- Multi-model evaluation
- Local LLM integration
- Automated fuzzing workflows

---

# Technologies

- Python
- Git
- GitHub
- Linux
- Termux
- AI Safety Research
- LLM Evaluation Techniques

---

# Contributing

Contributions, ideas, and research discussions are welcome.

---

# License

MIT License
