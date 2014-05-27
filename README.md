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

As root, install additional Sphinx documentation domains:

```
easy_install -U sphinxcontrib-phpdomain
easy_install -U sphinxcontrib-rubydomain
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

### License

   Copyright 2014 RJMetrics Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
