import ast


class ForbiddenFunctionsFinder(ast.NodeVisitor):
    forbidden = ['map', 'filter']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.issues = []

    def visit_Call(self, node):
        if not isinstance(node.func, ast.Name):
            return

        if node.func.id in self.forbidden:
            msg = "PCK01 Please don't use {}()".format(node.func.id)
            self.issues.append((node.lineno, node.col_offset, msg))


class PickyChecker(object):
    options = None
    name = 'picky-checker'
    version = '0.1'

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        parser = ForbiddenFunctionsFinder()
        parser.visit(self.tree)

        for lineno, column, msg in parser.issues:
            yield (lineno, column, msg, PickyChecker)
