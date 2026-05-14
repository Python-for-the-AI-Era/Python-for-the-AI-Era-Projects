# Project 00: Environment Auditor

### Technical Signposts
To complete this project, you will need to explore these specific Python tools:

1. **Venv Detection**: Compare `sys.prefix` and `sys.base_prefix`. If they differ, a virtual environment is active.
2. **Metadata**: Use `importlib.metadata.version("package-name")` to find what is installed.
3. **Spec Checking**: Use `importlib.util.find_spec("package-name")` to see if a package exists without importing it.
4. **Table Formatting**: Use f-string alignment. Example: `f"{name:<15}"` aligns text to the left with 15 spaces.
5. **Version Logic**: Since we aren't using third-party tools, try converting version strings into tuples for comparison: 
   `tuple(map(int, "3.12.1".split('.')))`