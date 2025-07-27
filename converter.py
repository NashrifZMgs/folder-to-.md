#!/usr/bin/env python3
import os
import sys
from collections.abc import Mapping

# --- CONFIGURATION ---
DEFAULT_EXCLUDES = {
    "node_modules", ".git", "dist", "build",
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
    ".DS_Store", "__pycache__"
}

LANG_MAP = {
    "js": "javascript", "jsx": "javascript", "ts": "typescript", "tsx": "typescript",
    "py": "python", "sh": "bash", "md": "markdown", "json": "json", "html": "html",
    "css": "css", "scss": "scss", "java": "java", "kt": "kotlin", "go": "go",
    "rs": "rust", "c": "c", "h": "c", "cpp": "cpp", "hpp": "cpp", "rb": "ruby",
    "php": "php", "swift": "swift", "sql": "sql", "xml": "xml", "yaml": "yaml", "yml": "yaml",
}

EMOJI_MAP = {
    "py": "🐍", "js": "💻", "ts": "💻", "jsx": "💻", "tsx": "💻", "json": "📦",
    "md": "📝", "sh": "🐚", "html": "🌐", "css": "🎨", "scss": "🎨", "java": "☕",
    "kt": "🤖", "rs": "🦀", "go": "🐹", "rb": "💎", "php": "🐘", "swift": "🐦",
    "gitignore": "🚫", "dockerfile": "🐳", "lock": "🔒",
    "default_file": "📄", "default_folder": "📁"
}

# --- HELPER FUNCTIONS ---

def show_help():
    """Prints the user-friendly help message."""
    help_text = """
┌───────────────────────────────────────────────────────────────────────────┐
│                      Code Combiner Script Help                            │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│ OVERVIEW:                                                                 │
│   This script scans a project folder and combines all of its code into a  │
│   single, beautifully formatted Markdown file (.md) for easy sharing.     │
│   The output includes a clickable file tree at the top.                   │
│                                                                           │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│ HOW TO USE:                                                               │
│   convert <directory> [-exclude_1] [-exclude_2] ...                       │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
"""
    print(help_text)

def get_emoji(name):
    """Get a file/folder emoji."""
    if "." not in name:
        return EMOJI_MAP["default_folder"]
    ext = name.split('.')[-1].lower()
    return EMOJI_MAP.get(ext, EMOJI_MAP["default_file"])

def generate_anchor(path):
    """Creates a GitHub-compatible anchor link from a path."""
    # This now receives the full, unique path, ensuring a unique anchor.
    return "".join(c for c in path if c.isalnum()).lower()

def generate_tree(file_paths):
    """Generates a clickable, tree-like table of contents using HTML for reliability."""
    tree = {}
    # Build a tree, but for files, store the full path as the value.
    for path in file_paths:
        parts = path.split(os.sep)
        current_level = tree
        for i, part in enumerate(parts):
            if i == len(parts) - 1:  # This is the file part
                current_level[part] = path
            else:  # This is a directory part
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]

    def build_tree_string(subtree, prefix=""):
        lines = []
        # Sort keys to ensure consistent order, especially for mixed files/dirs
        keys = sorted(subtree.keys(), key=lambda k: (isinstance(subtree[k], dict), k))
        for i, key in enumerate(keys):
            is_last = i == (len(keys) - 1)
            connector = "└── " if is_last else "├── "
            
            value = subtree[key]
            if isinstance(value, str):  # It's a file, value is the full path
                full_path = value
                anchor = generate_anchor(full_path)
                lines.append(f'{prefix}{connector}{get_emoji(key)} <a href="#{anchor}"><code>{key}</code></a>')
            else:  # It's a directory, value is a dictionary
                lines.append(f"{prefix}{connector}{get_emoji(key)} {key}/")
                extension = "    " if is_last else "│   "
                lines.extend(build_tree_string(value, prefix + extension))
        return lines

    tree_lines = build_tree_string(tree)
    # Wrap the entire output in <pre> tags to preserve formatting.
    return f'<pre>.\n' + '\n'.join(tree_lines) + '</pre>'


def get_language_from_extension(filename):
    """Gets the Markdown language identifier from a file's extension."""
    ext = filename.split('.')[-1].lower()
    return LANG_MAP.get(ext, "")

# --- MAIN LOGIC ---

def process_project(target_dir, output_file, user_exclusions):
    """Gathers files, generates the tree, and writes the final Markdown file."""
    
    # --- PASS 1: Collect all valid file paths ---
    included_files = []
    exclude_names = {item for item in user_exclusions if "/" not in item}
    exclude_paths = {item for item in user_exclusions if "/" in item}
    all_exclude_names = DEFAULT_EXCLUDES.union(exclude_names)

    for root, dirs, files in os.walk(target_dir, topdown=True):
        dirs[:] = [d for d in dirs if d not in all_exclude_names]
        for d in list(dirs):
            relative_dir_path = os.path.relpath(os.path.join(root, d), target_dir)
            if relative_dir_path in exclude_paths:
                dirs.remove(d)

        for filename in files:
            if filename in all_exclude_names:
                continue
            file_path = os.path.join(root, filename)
            relative_file_path = os.path.relpath(file_path, target_dir)
            if relative_file_path in exclude_paths:
                continue
            included_files.append(relative_file_path)
    
    included_files.sort()

    # --- PASS 2: Write the output file ---
    try:
        with open(output_file, 'w', encoding='utf-8') as md_file:
            # Write header
            md_file.write(f"# Combined Code for `{os.path.basename(target_dir)}`\n\n")
            
            # Write Table of Contents
            md_file.write("### Project Structure\n\n")
            tree_string = generate_tree(included_files)
            md_file.write(f"{tree_string}\n\n---\n---\n\n")

            # Write file contents
            for relative_path in included_files:
                full_path = os.path.join(target_dir, relative_path)
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    lang = get_language_from_extension(relative_path)
                    # Use the same anchor generation for the header destination
                    anchor = generate_anchor(relative_path)
                    
                    # Add the custom anchor ID to the header
                    md_file.write(f'<h2 id="{anchor}"><code>{relative_path}</code></h2>\n\n')
                    md_file.write(f"```{lang}\n")
                    md_file.write(content)
                    md_file.write("\n```\n\n---\n\n")
                        
                except Exception as e:
                    print(f"Warning: Could not read file {full_path}: {e}", file=sys.stderr)

        print(f"Successfully created {output_file}")

    except IOError as e:
        print(f"Error: Could not write to output file {output_file}: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Manually parses command-line arguments."""
    args = sys.argv[1:]

    if not args or args[0] in ['-h', '--help', '-help']:
        show_help()
        sys.exit(0)

    target_directory = args[0]
    if target_directory.startswith('-'):
        print(f"Error: The first argument must be the target directory.", file=sys.stderr)
        sys.exit(1)
        
    if not os.path.isdir(target_directory):
        print(f"Error: Directory not found at '{target_directory}'", file=sys.stderr)
        sys.exit(1)

    user_exclusions = {item.lstrip('-') for item in args[1:]}
    target_directory = target_directory.rstrip('/')
    output_filename = f"{os.path.basename(target_directory)}-all.md"

    process_project(target_directory, output_filename, user_exclusions)

if __name__ == "__main__":
    main()
