import os
import ast
import json

def extract_imports_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read(), filename=filepath)
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
    return imports

def scan_project(root_dir):
    dependency_graph = {}

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                full_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(full_path, root_dir)
                imports = extract_imports_from_file(full_path)
                dependency_graph[rel_path] = imports

    return dependency_graph

if __name__ == "__main__":
    project_path = "sample_codebase"  # relative path to the sample code directory
    graph = scan_project(project_path)

    with open("example_output.json", "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2)

    print("Dependency graph saved to example_output.json")