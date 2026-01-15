# Copilot / AI Agent Instructions

Purpose: Short, actionable guidance for AI edits in this small educational Python project.

- **Big picture:** This repository contains a set of small example modules (ex0–ex6) that progressively demonstrate Python OOP concepts: introductory script (`ex0/ft_garden_intro.py`), simple data classes (`ex1/ft_garden_data.py`), object behavior (`ex2/ft_plant_growth.py`), class-level state (`ex3/ft_plant_factory.py`), encapsulation and accessors (`ex4/ft_garden_security.py`), inheritance and polymorphism (`ex5/ft_plant_types.py`), and a manager/analytics module combining patterns (`ex6/ft_garden_analytics.py`). Treat these files as lightweight demos rather than a production service.

- **Primary goals for edits:**
  - Preserve the didactic, example-driven style (print-based demos and `if __name__ == "__main__"` blocks).
  - Keep public APIs and class/method names stable (e.g., `Flower`, `SecurePlant`, `GardenManager`, `add_to_garden`, `get_*`, `set_*`).
  - Use existing idioms: simple type hints, explicit getter/setter methods, double-underscore private attributes for encapsulation.

- **Patterns & conventions to follow:**
  - Module names follow `ft_*` convention. Keep that pattern for new example scripts.
  - Methods use `get_` / `set_` prefixes rather than properties; prefer preserving that unless migrating consistently across the repo.
  - Double-underscore attributes (e.g., `__height`, `__age_b`) are used to signal privacy — do not modify their names unless refactoring deliberately.
  - Demo code runs under `if __name__ == "__main__"` and prints to stdout; tests or interactive examples should follow the same pattern.

- **How to run examples / debugging:**
  - Run any example directly: `python3 ex6/ft_garden_analytics.py` (or the desired `exN/` file). Shebangs indicate Python 3.10 but any modern Python 3.x should work.
  - For quick checks, run a single function or class in REPL or a short script that imports the target module.

- **Integration & data flow notes:**
  - `ex6/ft_garden_analytics.py` composes the other patterns: `GardenManager` stores `SecurePlant`-derived instances in a dictionary (`__garden_content`) and uses `GardenStats` to summarize and score gardens.
  - `GardenManager.create_garden_network(owner_list)` returns multiple managers — use this when testing multi-owner behaviors.

- **Concrete examples the agent can use or suggest:**
  - Add a plant to a garden (from `ex6`):
    - `alice = GardenManager('Alice')`
    - `alice.add_to_garden(FloweringPlant('Rose', 25, 15, 'red', 'blooming'))`
  - Inspect plant info: call `alice.garden_info()` or `alice.stats.garden_evolution()`.

- **When editing code:**
  - Small, local fixes are preferred (typo fixes, docstring clarifications, adding type hints). Larger refactors (e.g., replacing getters with `@property`) must be applied consistently across modules and explained in the PR body.
  - Preserve existing printed output format where possible (these scripts are used as visible examples/tests).

- **Files to reference when making changes:**
  - Examples: [ex0/ft_garden_intro.py](ex0/ft_garden_intro.py), [ex1/ft_garden_data.py](ex1/ft_garden_data.py), [ex6/ft_garden_analytics.py](ex6/ft_garden_analytics.py).

- **PR guidance for humans reviewing AI edits:**
  - Verify that public class and method names are unchanged unless the PR documents a consistent refactor.
  - Run the modified example script(s) to ensure printed output remains educational and deterministic.

If any of these sections are unclear or you'd like a different emphasis (for example, converting demos to tests or adding a CI workflow), tell me which area to expand and I'll update this file.
