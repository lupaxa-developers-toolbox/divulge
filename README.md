<p align="center">
  <a href="https://github.com/lupaxa-developers-toolbox">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/organisations/developers-toolbox/readme-logo.png" alt="Developers Toolbox" />
  </a>
</p>

<h1 align="center">divulge</h1>

Opinionated console messaging helper for Python — coloured, prefixed
`info` / `success` / `warning` / `error` / `system` lines.

## Install

```bash
pip install lupaxa-divulge
```

Requires Python 3.10+.

## Usage

```python
import lupaxa.divulge as divulge

divulge.info("Server starting")
divulge.success("Operation completed")
divulge.warning("Disk usage high")
divulge.error("Connection failed")
divulge.system("Starting backup job")

divulge.Divulge("done").success()
divulge.divulge({"id": 1}).warning()
```

Turn colours or prefixes off for the process:

```python
divulge.configure(use_colours=False, use_prefixes=False)
```

Bold is off by default. Enable it for one call or for the process:

```python
divulge.info("this line is bold", use_bold=True)
divulge.configure(use_bold=True)
```

A walkthrough of the API is in `demo.py`:

```bash
python demo.py
```

## Documentation

Site pages live in `mkdocs/` and publish to
<https://divulge.thelupaxaproject.org/>.

```bash
make init
make python-install-dev
make mkdocs-serve
```

<a href="https://github.com/the-lupaxa-project">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/components/footer-for-child-orgs.svg" alt="The Lupaxa Project Footer" width="100%" />
</a>
