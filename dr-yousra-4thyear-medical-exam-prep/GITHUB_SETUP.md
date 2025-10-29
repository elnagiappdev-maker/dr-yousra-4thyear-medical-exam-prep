# GitHub Setup Guide

This guide explains how to set up and manage the Medical Exam Prep Streamlit project on GitHub.

## Initial Setup

### 1. Create a GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository:
   - **Repository name**: `med_exam_prep_streamlit`
   - **Description**: "4th Year Medical Exam Prep - Interactive Streamlit Application with 123 Questions"
   - **Visibility**: Public (to allow others to use and contribute)
   - **Initialize with**: None (we'll push existing code)

### 2. Connect Local Repository to GitHub

```bash
cd /path/to/med_exam_prep_streamlit

# Add remote origin
git remote add origin https://github.com/yourusername/med_exam_prep_streamlit.git

# Rename branch to main (if on master)
git branch -M main

# Push to GitHub
git push -u origin main
```

### 3. Verify Setup

```bash
git remote -v
# Should show:
# origin  https://github.com/yourusername/med_exam_prep_streamlit.git (fetch)
# origin  https://github.com/yourusername/med_exam_prep_streamlit.git (push)
```

---

## Repository Structure

```
med_exam_prep_streamlit/
├── .github/
│   └── workflows/           # CI/CD workflows
├── .gitignore              # Git ignore rules
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── app.py                  # Main Streamlit application
├── questions_database.json # Question data
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── README.md               # Project documentation
├── DEPLOYMENT.md           # Deployment guide
├── GITHUB_SETUP.md         # This file
└── LICENSE                 # License file
```

---

## GitHub Features to Enable

### 1. Enable GitHub Pages (Optional)

For hosting documentation:

1. Go to **Settings** → **Pages**
2. Select **main** branch and **/root** folder
3. Click **Save**

Your documentation will be available at: `https://yourusername.github.io/med_exam_prep_streamlit/`

### 2. Add Topics

Go to **Settings** → **Topics** and add:
- `streamlit`
- `medical-education`
- `exam-preparation`
- `medical-questions`
- `python`

### 3. Enable Discussions

Go to **Settings** → **Features** and enable:
- **Discussions** - for community discussions
- **Sponsorships** - if you want to accept donations

### 4. Set Up Branch Protection

Go to **Settings** → **Branches** → **Add rule**:
- Branch name pattern: `main`
- Require pull request reviews before merging
- Require status checks to pass

---

## Continuous Integration/Deployment

### GitHub Actions Workflow

Create `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Check syntax
      run: python -m py_compile app.py
    
    - name: Validate JSON
      run: python -c "import json; json.load(open('questions_database.json'))"
```

### Streamlit Cloud Deployment

Streamlit Cloud automatically deploys from GitHub:

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Select your repository
4. Set main file to `app.py`
5. Click "Deploy"

---

## Contributing Guidelines

Create `CONTRIBUTING.md`:

```markdown
# Contributing

We welcome contributions! Here's how you can help:

## Types of Contributions

- **Questions**: Add new medical questions
- **Fixes**: Correct errors in existing questions
- **Features**: Suggest or implement new features
- **Documentation**: Improve documentation

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit with clear messages (`git commit -am 'Add new feature'`)
5. Push to your fork (`git push origin feature/your-feature`)
6. Create a Pull Request

## Code Style

- Follow PEP 8 for Python code
- Use descriptive variable names
- Add comments for complex logic
- Update documentation as needed

## Questions Format

When adding questions, ensure:
- All fields are complete
- Explanations are clear and educational
- Options are realistic and challenging
- Content is medically accurate
```

---

## Issue Templates

Create `.github/ISSUE_TEMPLATE/bug_report.md`:

```markdown
---
name: Bug Report
about: Report a bug to help us improve
---

## Description
Brief description of the bug

## Steps to Reproduce
1. 
2. 
3. 

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Screenshots
If applicable

## Environment
- OS: 
- Python version: 
- Streamlit version: 

## Additional Context
Any other relevant information
```

---

## Release Management

### Semantic Versioning

Use semantic versioning (MAJOR.MINOR.PATCH):
- MAJOR: Breaking changes
- MINOR: New features
- PATCH: Bug fixes

### Creating Releases

1. Update version in `app.py` and `README.md`
2. Commit changes
3. Create a tag: `git tag -a v1.0.0 -m "Release version 1.0.0"`
4. Push tag: `git push origin v1.0.0`
5. Go to GitHub → **Releases** → **Create release**
6. Add release notes and publish

---

## Collaboration

### Code Review

- All PRs require at least one review
- Use GitHub's review features
- Discuss changes in comments
- Approve or request changes

### Project Management

Use GitHub Projects to track:
- Features in development
- Bugs to fix
- Questions to add
- Documentation updates

---

## Documentation

### README Sections

Your README should include:
- Project description
- Features
- Installation instructions
- Usage guide
- Contributing guidelines
- License information
- Credits

### Additional Documentation

- `DEPLOYMENT.md` - Deployment instructions
- `CONTRIBUTING.md` - Contribution guidelines
- `CODE_OF_CONDUCT.md` - Community guidelines
- `SECURITY.md` - Security policy

---

## License

Add a LICENSE file (MIT License recommended):

```
MIT License

Copyright (c) 2025 Medical Exam Prep Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## Badges

Add badges to your README:

```markdown
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![License](https://img.shields.io/badge/License-MIT-green)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/med_exam_prep_streamlit)](https://github.com/yourusername/med_exam_prep_streamlit)
```

---

## Community

### Engagement

- Respond to issues and PRs promptly
- Thank contributors
- Share updates in Discussions
- Celebrate milestones

### Promotion

- Share on social media
- Write blog posts
- Present at conferences
- Collaborate with other projects

---

## Maintenance Checklist

- [ ] Update dependencies monthly
- [ ] Review and respond to issues
- [ ] Merge pull requests
- [ ] Update documentation
- [ ] Release new versions
- [ ] Monitor GitHub Insights
- [ ] Engage with community

---

## Useful GitHub Links

- [GitHub Docs](https://docs.github.com)
- [GitHub CLI](https://cli.github.com)
- [GitHub Actions](https://github.com/features/actions)
- [GitHub Discussions](https://docs.github.com/en/discussions)

---

## Support

For questions about GitHub setup, refer to:
- [GitHub Getting Started](https://docs.github.com/en/get-started)
- [GitHub Guides](https://guides.github.com)
- [GitHub Community](https://github.community)

---

**Last Updated**: October 2025
