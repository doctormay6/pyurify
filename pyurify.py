def pyurify(script, imported=None):
    """
    Description:
        Expand import statements recursively until all dependencies have become local

    Inputs:
        script (Str): python script for which to find and expand all import statements
        imported (None, list): when called recursively, keeps track of already expanded imports

    Outputs:
        purePython (Str): original python script with all import statements expanded to be included locally
    """
    if imported is None:
        imported = []  # intentionally made mutable for recursion (don't want to mutate default arg value)
    purePython = ""
    for line in script.split("\n"):
        if line.strip()[:7] == "import " or (line.strip()[:5] == "from " and "import " in line):
            # expand import statement
            expanded = expandImport(line, imported)
            # recursively pyurify expanded code
            expanded = pyurify(expanded, imported)
            # match indent in case import was in a non-standard place
            expanded = matchIndent(expanded, line)
            purePython += expanded + "\n"
        else:
            purePython += line + "\n"
    return purePython


def expandImport(importStatement, imported):
    """Fetch the code for the import and return all of it"""
    # TODO: parse import statement and extract module name

    # TODO: if import is already in 'imported' arg (code exists in purePython already), return "\n"

    # TODO: import module into current namespace

    # TODO: use module's __file__ attribute to fetch source code

    # TODO: account for sub-imports -- ex. from datetime import datetime

    # TODO: account for dependent/helper functions -- pre-built symbol table vs on-demand scan?

    # TODO: return all dependency code
    return "foo\n"  # TODO: implement


def matchIndent(expandedCode, line):
    """Format expanded code to match the indentation of the line it is replacing"""
    if line[:4] == "    ":
        indent = "    "
    elif line[0] == "\t":
        indent = "\t"
    else:
        return expandedCode
    formatted = ""
    for line in expandedCode.split("\n"):
        if "from " in line:
            formatted += indent * line.index("from ")
        else:
            formatted += indent * line.index("import ")
        formatted += line + "\n"
    return formatted
