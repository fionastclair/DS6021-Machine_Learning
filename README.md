# DS 6021 — Class Repository

Welcome to DS6021 for Fall 2026! 

This repository will complement our Canvas page and will be a place to access course materials and homework solutions. 

It includes a Python environment suitable for use in this class, as well as worked in class examples, and homework solutions. It will also include data that will be used in the course. It will be updated frequently so get comfortable with `git pull`! Additional content (e.g. lecture slides, complementary informatoin) may be added throughout the semester. In addition to Python setup files, please pay attention to the following folders: 

```
notebooks/              In-class examples (These will updated frequently!)
homework/               Homework
    instructions.md         Instructions for how to complete and turn in your homework
    solutions/              This folder will contain homework solutions after they have been graded. 
data/                   Datasets you will need to run in-class examples, as well as homework. 
```

## Repository Access + Updates

Please ensure that you have [git](https://git-scm.com/) installed on your machine, and a [github](www.github.com) account. Both are free! 

To clone this repository, please execute the commands below. 

```sh
git clone https://github.com/mfriedel/DS6021_F26.git
cd DS6021_F26
```

I will be making changes throughout the semester, adding and updating files. To access these changes, you simply execute either `git fetch` or `git merge`. More information can be found in the [Git documentation for getting changes from a remote repository.](https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository) 

Your feedback is welcomed! If you spot an error or would like to make a contribution, please submit a [pull request](https://docs.github.com/en/pull-requests/reference/pull-requests). 


## Python Environment Setup

Environment management is a critical part of using Python. My goal is to be as flexible as possible and allow you to use the package manager you are familiar with, while still being able to easily create an enviornment that generates repeatible results. I personally use uv, but either pip or conda work well if you prefer those. 

Pick **one** of the three below. All three install identical package versions. 


### Option 1 — uv

[Install uv](https://docs.astral.sh/uv/getting-started/installation/), then:

```sh
uv sync
```

### Option 2 — pip

Requires Python 3.12 or newer.

```sh
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Option 3 — conda

```sh
conda env create -f environment.yml
conda activate ds6021
```

## Using the environment

**VSCode.** Open the DS6021_F25 folder. VSCode should pick up `.venv` automatically. 
If it doesn't, hit `Ctrl/Cmd+Shift+P` → *Python: Select Interpreter* → choose the one
under `.venv`. Open any notebook and pick the same interpreter as the kernel.

**Jupyter Lab / Notebook.**

```sh
source .venv/bin/activate        # or: conda activate ds6021
jupyter lab
```

Note that you can also run Jupyter notebooks directly from within VSCode. 

## Notes and Resources 

While none of these are required, they are additional materials to help you get a grounding in the tech stack we use. 

* Helpful overview of [Managing Development Environments](https://uvads.github.io/managing-environments/)
* [UVA Data Science Technical Orientation Materials](https://github.com/UVADS/orientation-technical)
* All of you should be taking Understanding Uncertainty with either Sarah or Terry this semester. As part of the orientation, [this diagram](https://github.com/ds4e/scratchpad/blob/main/software.png) was shared and discussed when they gave a class overview. I will use a similar approach in this class, so if you are able to get set up with VSCode for that course, you should be in great shape here as well. 
* If you use VSCode, I recommend installing the [UVA Data Science Core Extension Pack](https://marketplace.visualstudio.com/items?itemName=uva-school-of-data-science.sds-vscode). 
---


