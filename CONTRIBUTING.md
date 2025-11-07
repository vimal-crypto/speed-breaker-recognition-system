# Contributing to Speed Breaker Recognition System

Thank you for considering contributing to this project! We welcome contributions from the community.

## How to Contribute

### Reporting Issues

If you find a bug or have a feature request:

1. Check if the issue already exists in the [Issues](https://github.com/vimal-crypto/speed-breaker-recognition-system/issues) section
2. If not, create a new issue with a clear title and description
3. Include steps to reproduce (for bugs) or use cases (for features)
4. Add relevant labels

### Pull Requests

We follow the standard GitHub workflow:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/vimal-crypto/speed-breaker-recognition-system.git
   cd speed-breaker-recognition-system
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Write clean, readable code
   - Follow Python PEP 8 style guidelines
   - Add comments where necessary
   - Update documentation if needed

4. **Test Your Changes**
   ```bash
   python -m pytest tests/
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Submit a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear description of changes

### Code Style Guidelines

- Use meaningful variable and function names
- Follow PEP 8 conventions
- Maximum line length: 100 characters
- Use docstrings for functions and classes
- Add type hints where applicable

### Commit Message Guidelines

Use conventional commit messages:

- `Add:` for new features
- `Fix:` for bug fixes
- `Update:` for changes to existing features
- `Remove:` for deleted code
- `Docs:` for documentation changes
- `Refactor:` for code refactoring

### Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the best outcome for the project
- Show empathy towards other contributors

## Questions?

Feel free to open an issue for any questions or reach out to the maintainers.

Thank you for contributing! 🚀
