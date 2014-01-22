### Installation

You need Python 2.7 to build the site.

As root, try:

```bash
pip install sphinx==1.2
```

if that doesn't work, do:

```bash
easy_install sphinx==1.2
```

Then, from the root of the repo, run

```bash
make html
```

To run a server for viewing the generated files, do:

```bash
cd _build/html
python -m SimpleHTTPServer
```
