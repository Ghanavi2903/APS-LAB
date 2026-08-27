# APS Lab — Lab Assignments

This repository contains lab assignments, exercises, example code, and supporting resources for the APS Lab course.

> Course: APS Lab

## Repository purpose

This repo holds the lab assignments you will complete during the APS Lab course. Each lab includes instructions, starter code, and any data or scripts required to run the exercises.

## Repository layout

- labs/              — individual lab directories (one folder per lab, named like `lab-01`, `lab-02`, ...)
  - lab-01/          — README.md with instructions, starter code, tests, and submission guide
  - lab-02/
  - ...
- solutions/         — reference solutions (use only when allowed by instructor)
- scripts/           — utility scripts to build, run, or test labs
- data/              — sample datasets used by labs
- docs/              — course notes, rubrics, and supplemental documentation
- README.md          — this file

Note: If any of the above folders don't exist yet, create them and add a README or example files for each lab.

## How to use

1. Clone the repository

```bash
git clone https://github.com/Ghanavi2903/APS-LAB.git
cd APS-LAB
```

2. Open the lab directory you are working on, e.g. `labs/lab-01`, and follow the lab README for instructions.

3. For Python-based labs, we recommend creating a virtual environment and installing dependencies:

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\\Scripts\\activate  # Windows
pip install -r requirements.txt  # if the lab provides one
```

4. Run the lab's main script or test harness as described in the lab's README, e.g.: `python labs/lab-01/main.py` or `bash scripts/run_lab.sh lab-01`.

## Submissions

Follow the submission instructions in each lab's README. Common workflows:

- Create a branch for your work: `git checkout -b lab-01-yourname`
- Commit changes and push to your fork or to the course repo if instructed: `git push origin lab-01-yourname`
- Open a Pull Request with the lab number and your name in the title.

Include the following in your submission where required:
- Completed source files
- Any generated outputs required by the lab (e.g., figures, logs)
- A short writeup in `REPORT.md` explaining your approach and findings

## Testing and grading

Where available, labs may include automated tests. Run them as described in each lab's README, for example:

```bash
pytest labs/lab-01/tests
```

Grading rubrics and deadlines are stored in `docs/` when provided.

## Recommended tools and languages

The APS Lab uses common tools and languages depending on the assignment. Typical stack includes:

- Python 3.8+ (numpy, pandas, matplotlib, pytest)
- C/C++ (gcc/clang, make)
- Bash / Shell scripts

Add a `requirements.txt` or project-specific environment file inside each lab folder when dependencies are required.

## Contribution and academic integrity

- Follow the academic integrity rules provided by the instructor.
- Collaborate only to the extent allowed by the course guidelines. When in doubt, ask the instructor or TA.
- If you share solutions or content in `solutions/`, clearly mark them and follow the course policy for solution release.

## License

If the course requires a license, create a `LICENSE` file. Otherwise, this repository has no license by default.

## Contact

Maintainer: Ghanavi2903

If you'd like the README to include additional sections (detailed lab index, badges, CI setup, or a contributing guide), tell me what to include and I'll update it.