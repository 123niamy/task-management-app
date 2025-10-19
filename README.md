SDLC Summary: Task Management App
This project was built following the Software Development Life Cycle (SDLC) to ensure clarity, structure, and maintainability.

 SDLC Phases Completed
Phase	Description
Requirement	Defined functional and non-functional goals for a CLI-based task manager
Design	Created modular files: task.py, manager.py, main.py, storage.py
Implementation	Developed core logic, CLI interface, and persistent storage using JSON
Testing	Added unit tests (test_task.py, test_manager.py) and GitHub Actions
Deployment	Made app runnable locally with clear instructions in README.md
Maintenance	Documented long-term support plan in maintenance.md

 Project Overview
A simple command-line task manager built in Python. Users can add, list, and complete tasks with persistent storage and automated testing.

Features
Add, list, and mark tasks as complete

Persistent storage using JSON

Modular architecture

Unit testing with unittest

CI/CD with GitHub Actions

 How to Run
bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
python main.py
 Run Tests
bash
python test_task.py
python test_manager.py
