code-ecosystem-agent

Understanding codebases through structure, filtering, and AI agents.

📁 Project Structure

code-ecosystem-agent/
├── sample_codebase/          # Test files for parser
│   ├── main.py
│   ├── utils.py
│   └── config.py
├── task1_graph/              # Dependency graph builder
│   └── parser.py
├── task2_summary/            # LLM summarizer stub
│   └── summarizer_stub.py
├── example_output.json       # Example graph output
└── README.md

🔧 Task 1 - Dependency Graph Builder

parser.py scans Python files and builds a JSON-formatted graph of file-to-file imports.

Run:

python task1_graph/parser.py

Output:

Saves example_output.json like this:

{
  "main.py": ["utils"],
  "utils.py": [],
  "config.py": ["os"]
}

🔍 Task 2 - Summarizer Stub

A lightweight placeholder that outlines how a real LLM (like GPT-4) would be prompted.
Includes:

Context-aware prompt templates

Suggested summary format

🧠 Motivation

This project was created for the 0docs Engineering Task. It aims to show how engineering intuition and modern AI tooling can work together to help teams understand large codebases faster and more effectively.

✍️ Author

Created by Myunghwan (Ben) Lee

GitHub: @benjilee0919

📄 License

MIT (add if desired)
