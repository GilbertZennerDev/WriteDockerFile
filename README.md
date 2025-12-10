# 🐳 WriteDockerfile

**A lightweight Python Command-Line Utility (CLI) to quickly generate a basic, runnable Dockerfile based on your input files and preferred base image.**

This tool is designed to save time by automating the creation of the boilerplate `FROM`, `WORKDIR`, `COPY`, and `CMD` instructions needed to containerize a simple application setup.

## 🚀 Quick Start

### Prerequisites

  * Python 3.x
  * A running shell environment (bash, zsh, PowerShell, etc.)

### 1\. Clone the Repository

```bash
git clone https://github.com/GilbertZennerDev/WriteDockerFile.git
cd WriteDockerFile
```

### 2\. Prepare Entrypoint

Ensure you have a basic executable script named `entry.sh` (or create one) in the same directory. This script will be the final execution command inside your container.

**Example `entry.sh`:**

```bash
#!/bin/bash
# Execute your main application file (e.g., a Python script)
echo "Starting application..."
python3 main.py
```

### 3\. Run the Script

Execute the `WriteDockerFile.py` script and pass your desired files and base image using the specified flags.

## ⚙️ Usage

The script uses a simple flag structure:

| Flag | Purpose | Example Value | Notes |
| :--- | :--- | :--- | :--- |
| `-f` | Specify a **file to copy** into the image. | `main.py` | Can be used multiple times. |
| `-from` | Specify the **base image** for the `FROM` instruction. | `node:18-alpine` | Optional. If omitted, defaults to `python:3.12-slim`. |
| `-condition` | *(Currently ignored)* | `test_mode` | Reserved for future conditional logic. |

### Example 1: Using the Default Base Image

To create a Dockerfile that copies `main.py` and `requirements.txt`, using the default base image (`python:3.12-slim`):

```bash
python3 WriteDockerFile.py -f main.py -f requirements.txt
```

**Output `Dockerfile` Content:**

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY main.py /app/
COPY requirements.txt /app/
COPY entry.sh /app/
CMD ["sh", "entry.sh"]
```

### Example 2: Specifying a Custom Base Image

To use a specific Node.js base image and copy a single `index.js` file:

```bash
python3 WriteDockerFile.py -from node:20-alpine -f index.js
```

**Output `Dockerfile` Content:**

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY index.js /app/
COPY entry.sh /app/
CMD ["sh", "entry.sh"]
```

## 🛠️ Generated Dockerfile Structure

The generated Dockerfile follows this fixed structure:

1.  **`FROM`**: Sets the base image (default or specified).
2.  **`WORKDIR /app`**: Creates and sets the working directory.
3.  **`COPY <file>`**: Copies all files specified by `-f` into `/app/`.
4.  **`COPY entry.sh /app/`**: Always copies the mandatory entrypoint script.
5.  **`CMD ["sh", "entry.sh"]`**: Sets the default execution command for the container.

## 📜 Project Code Overview

The script is highly modular for easy understanding:

  * **`getStuff(ac, av, symbol)`**: Core parser that extracts arguments following a specific `symbol` (e.g., `-f`, `-from`).
  * **`FROM(src)`**: Generates the `FROM` instruction, applying the `python:3.12-slim` default if `src` is empty.
  * **`COPYFILES(files)`**: Iterates over a list of files and generates the corresponding `COPY` instructions.
  * **`composeDockerFile(...)`**: Assembles all generated instructions into the final Dockerfile content string.
  * **`writeDockerFile(content)`**: Writes the final string to a file named `Dockerfile`.

## 🤝 Contribution

Feel free to open an issue or submit a pull request if you have suggestions for new features, such as:

  * Adding support for `EXPOSE` or `RUN` instructions.
  * Implementing conditional logic using the `-condition` flag.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

By the way, to unlock the full functionality of all Apps, enable [Gemini Apps Activity](https://myactivity.google.com/product/gemini).
