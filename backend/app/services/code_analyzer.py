import ast


class CodeAnalyzer:

    def analyze_code(self, source_code):

        issues = []

        # 1. Empty code check
        if not source_code.strip():
            return {
                "status": "Failed",
                "total_issues": 1,
                "issues": ["Source code is empty"]
            }

        # 2. Syntax error check
        try:
            ast.parse(source_code)
        except SyntaxError as error:
            issues.append(
                f"Syntax Error at line {error.lineno}: {error.msg}"
            )

        # 3. Line length check
        lines = source_code.splitlines()

        for line_number, line in enumerate(lines, start=1):
            if len(line) > 100:
                issues.append(
                    f"Line {line_number}: Line exceeds 100 characters"
                )

        # 4. TODO / FIXME check
        for line_number, line in enumerate(lines, start=1):
            if "TODO" in line or "FIXME" in line:
                issues.append(
                    f"Line {line_number}: TODO/FIXME comment found"
                )

        # 5. Debug print check
        for line_number, line in enumerate(lines, start=1):
            if "print(" in line:
                issues.append(
                    f"Line {line_number}: Debug print statement found"
                )

        return {
            "status": "Completed",
            "total_issues": len(issues),
            "issues": issues
        }