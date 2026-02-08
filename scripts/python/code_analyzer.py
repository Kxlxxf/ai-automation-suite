import ast
import os
import re
import sys

class CodeAnalyzer:
    def __init__(self, directory):
        self.directory = directory
        self.issues = []

    def analyze(self):
        for root, _, files in os.walk(self.directory):
            for filename in files:
                if filename.endswith('.py'):
                    self.check_quality(os.path.join(root, filename))
                    self.check_security(os.path.join(root, filename))
                    self.check_performance(os.path.join(root, filename))

    def check_quality(self, file_path):
        with open(file_path, 'r') as file:
            try:
                tree = ast.parse(file.read())
            except SyntaxError as e:
                self.issues.append(f'Syntax error in {file_path}: {e}')

    def check_security(self, file_path):
        with open(file_path, 'r') as file:
            contents = file.read()
            if re.search(r'\bimport\s+subprocess\b', contents):
                self.issues.append(f'Potential security risk found in {file_path}: subprocess usage')

    def check_performance(self, file_path):
        with open(file_path, 'r') as file:
            contents = file.read()
            if re.search(r'\bfor\s+.*\s+in\s+range\s*\(', contents):
                self.issues.append(f'Performance issue in {file_path}: Use of range() in loop')

    def report(self):
        if self.issues:
            print('### Code Analysis Report ###')
            for issue in self.issues:
                print(issue)
        else:
            print('No issues found.')

if __name__ == '__main__':
    directory_to_analyze = sys.argv[1] if len(sys.argv) > 1 else '.'
    analyzer = CodeAnalyzer(directory_to_analyze)
    analyzer.analyze()
    analyzer.report()