---
title: Installation
---

# 🛠 Installation

## 1. 📥 Download or clone the repository

[TIP] Skip this step, if you're going to install the package directly from **PyPi** or **GitHub** repository.

```sh
mkdir -pv ~/workspaces/projects
cd ~/workspaces/projects

# HTTPS:
git clone https://github.com/bybatkhuu/module-python-template.git
# Or SSH (development):
git clone git@github.com:bybatkhuu/module-python-template.git

cd module-python-template
```

Alternatively, download the source from the [releases](https://github.com/bybatkhuu/module-python-template/releases) page and extract it into your projects directory.

### 2. 📦 Install the package

[NOTE] Choose one of the following methods to install the package **[A ~ F]**:

**OPTION A.** [**RECOMMENDED**] Install from **PyPi**:

```sh
# Install from staging TestPyPi:
pip install -i https://test.pypi.org/simple -U my-module01

# Or install from production PyPi:
# pip install -U my-module01
```

**OPTION B.** Install latest version directly from **GitHub** repository:

```sh
pip install git+https://github.com/bybatkhuu/module-python-template.git
```

**OPTION C.** Install from the downloaded **source code**:

```sh
# Install directly from the source code:
pip install .

# Or install with editable mode:
pip install -e .
```

**OPTION D.** Install for **DEVELOPMENT** environment:

```sh
pip install -e .[dev]

# Install pre-commit hooks:
pre-commit install
```

**OPTION E.** Install from **pre-built release** files:

1. Download **`.whl`** or **`.tar.gz`** file from [**releases**](https://github.com/bybatkhuu/module-python-template/releases)
2. Install with pip:

```sh
# Install from .whl file:
pip install ./my_module01-[VERSION]-py3-none-any.whl

# Or install from .tar.gz file:
pip install ./my_module01-[VERSION].tar.gz
```

**OPTION F.** Copy the **module** into the project directory (for **testing**):

```sh
# Install python dependencies:
pip install -r ./requirements.txt

# Copy the module source code into the project:
cp -r ./src/my_module01 [PROJECT_DIR]
# For example:
cp -r ./src/my_module01 /some/path/project/
```
