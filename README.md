-----

# 🌳 Code Combiner

A powerful command-line tool that scans a project directory and combines all its files into a single, beautifully formatted Markdown file, complete with a clickable project tree. Perfect for sharing projects, creating documentation, or using with large language models.

## ✨ Features

  * **All-in-One File**: Merges an entire project's source code into one self-contained Markdown file.
  * **Clickable Project Tree**: Automatically generates an interactive file tree at the top of the document for easy navigation between code sections.
  * **Smart Syntax Highlighting**: Detects file types and applies the correct Markdown language identifier for proper syntax highlighting.
  * **Emoji Icons**: Uses file-type specific emojis in the project tree for a clean and intuitive visual overview.
  * **Custom Exclusions**: Easily ignore common directories (`node_modules`, `.git`) and specify your own files or folders to exclude.
  * **Zero Dependencies**: A single Python script that runs without any external libraries.

-----

## 🚀 Installation

To use `converter.py` as a command-line tool from anywhere on your system, follow these steps:

1.  **Make the script executable:**
    Open your terminal and run the following command to grant execute permissions to the script.

    ```bash
    chmod +x converter.py
    ```

2.  **Move it to your PATH:**
    Move the script to a directory that is part of your system's `PATH`. A common choice is `/usr/local/bin`.

    ```bash
    sudo mv converter.py /usr/local/bin/combine
    ```

    *Note: By renaming it to `combine`, you can now call the script with this shorter command.*

Now you can run the script from any directory\!

-----

## Usage

The script is easy to use. The first argument is always the target directory, followed by any files or folders you wish to exclude.

### Basic Command

To combine a project located in the `my-app` directory, run:

```bash
combine ./my-app
```

This will create a file named `my-app-all.md` in your current directory.

### Excluding Files and Folders

You can provide additional arguments to exclude specific files or folders. Each exclusion should be prefixed with a `-`.

  * **Exclude a folder:** To ignore the `dist` folder:
    ```bash
    combine ./my-app -dist
    ```
  * **Exclude a file:** To ignore a specific configuration file:
    ```bash
    combine ./my-app -config.local.js
    ```
  * **Exclude by path:** To ignore a file within a specific folder:
    ```bash
    combine ./my-app -src/legacy/old-code.js
    ```
  * **Multiple Exclusions:**
    ```bash
    combine ./my-app -dist -build -src/assets/temp.png
    ```

-----

## 🔧 Configuration

You can customize the script's default behavior by editing the configuration constants at the top of the file.

  * `DEFAULT_EXCLUDES`: A set of file and folder names that are always excluded. You can add more to this list, such as `.env` or `coverage`.
  * `LANG_MAP`: A dictionary that maps file extensions to Markdown language identifiers for syntax highlighting. You can add new mappings here.
  * `EMOJI_MAP`: A dictionary that maps file extensions and types to the emojis used in the project tree. Feel free to customize them\!

-----

## 📝 Sample Output

Here is a small example of what the generated Markdown file looks like:

```markdown
# Combined Code for `sample-project`

### Project Structure

<pre>.
├── 📄 .gitignore
├── 🐍 main.py
└── 🌐 public/
    ├── 🎨 style.css
    └── 💻 script.js
</pre>

---
---

<h2 id="gitignore"><code>.gitignore</code></h2>

```

node\_modules
dist
.env

````

---

<h2 id="mainpy"><code>main.py</code></h2>

```python
def hello_world():
    print("Hello, world!")

if __name__ == "__main__":
    hello_world()
````

-----

```

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
```
