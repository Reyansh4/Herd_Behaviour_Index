# Contributing to Herd Behaviour Index (HBI)

Thank you for your interest in contributing. This project is released under the MIT License. By contributing, you agree that your contributions will be licensed under the same terms.

## Maintainers

Project maintainers review pull requests and issues. If you have questions about contributing or maintenance, open a [GitHub Discussion](https://github.com/your-org/your-repo/discussions) or an issue. There is no formal maintainer list; the repository owner and designated collaborators handle reviews and releases.

## How to Contribute

### Reporting issues

- Use the issue tracker for bugs, documentation errors, or feature requests.
- Describe the problem or suggestion clearly and, where relevant, include steps to reproduce or examples.

### Submitting changes (pull requests)

1. **Fork** the repository and create a branch from `main` (or the default branch).
2. **Make your changes** in logical commits with clear messages.
3. **Ensure** you do not commit:
   - API keys, tokens, or secrets
   - Proprietary or confidential data
   - Files listed in `.gitignore` (e.g. `.env`, virtual environments)
4. **Open a pull request** with a short description of what changed and why.
5. **Reference** any related issues if applicable.

Maintainers will review and may request changes. Once approved, your PR can be merged.

### Improving documentation

- Fix typos, clarify wording, or add examples in `docs/`, `methodology/`, or `case_studies/`.
- Keep tone neutral and professional.
- Submit changes via pull request as above.

### Contributing datasets

- **Synthetic or anonymized data only.** Do not submit proprietary or personally identifiable event data unless you have rights to license it under MIT.
- Acceptable: synthetic events for testing, small illustrative samples, or pointers to public datasets that work with the pipeline.
- Place sample or example data in `sample_data/` and document format and intended use in a README or in the PR description.

### Code and notebooks

- Follow existing style and structure where possible.
- Notebooks should run without requiring secrets; use `sample_data/` or documented placeholders for paths and credentials.
- New scripts or notebooks should be placed under the appropriate directory (`notebooks/`, `dashboards/`, etc.) and described in the relevant README.

### License

All contributions are made under the MIT License. By submitting a pull request, you confirm that you have the right to license your work under MIT and that you agree to the project’s [Code of Conduct](CODE_OF_CONDUCT.md).
