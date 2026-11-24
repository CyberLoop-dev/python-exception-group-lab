<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:101827,100:0f766e&height=170&section=header&text=Python%20Exception%20Group%20Lab&fontSize=32&fontColor=ffffff&animation=fadeIn" width="100%" alt="Waving header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&pause=900&color=14B8A6&center=true&vCenter=true&width=760&lines=Learn+ExceptionGroup+and+except*;See+independent+failures+handled+by+type" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/python-exception-group-lab)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/python-exception-group-lab)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/python-exception-group-lab?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/python-exception-group-lab)
<img src="assets/mark.svg" width="112" alt="Exception group illustration"/>
</div>

## 🧭 Overview
A dependency-free Python 3.11+ CLI demonstrating how an <code>ExceptionGroup</code> is split into matching subgroups by separate <code>except*</code> clauses.

## ✨ Features
- 🧩 Raise one group containing several exception types.
- 🎯 Handle ValueError, TypeError, and OSError separately.
- 📦 Inspect the subgroup received by each handler.
- 🧪 Run deterministic standard-library tests.

## 🎬 Demo
No hosted demo is provided. Run the CLI locally to see each handler receive only its matching exception types.

## ⚡ Quick Start
Requires Python 3.11+. No third-party packages are needed.

~~~bash
python exception_group_lab.py
python exception_group_lab.py --json
python -m unittest test_exception_group_lab
~~~

## 🧰 Tech Stack
- Python 3.11+
- Built-in <code>ExceptionGroup</code> and <code>except*</code>
- Standard library and <code>pyproject.toml</code> metadata

## 🗂️ Folder Structure
~~~text
python-exception-group-lab/
├── exception_group_lab.py
├── test_exception_group_lab.py
├── pyproject.toml
├── assets/mark.svg
├── .gitignore
├── LICENSE
└── README.md
~~~

## 🗺️ Roadmap
- [x] Multiple exception types in one group
- [x] Separate except* handlers
- [ ] Add nested ExceptionGroup examples

## 🤝 Contributing
Issues and focused pull requests are welcome. Keep examples deterministic and compatible with Python 3.11+.

## 📄 License
MIT License. See [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:101827&height=100&section=footer" width="100%" alt="Waving footer"/></div>
