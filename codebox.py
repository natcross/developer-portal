import inspect
import os
import re
import subprocess

from docutils import nodes
from docutils.parsers.rst import directives

class codeboxDirective(Directive):
    """
    reStructuredText directive to show code listings with google-code-prettify
    """

    has_content = True

    def run(self):
        self.assert_has_content()
        text = '<pre class="prettyprint">%s</pre>' % self.content
        return [nodes.raw('', text, format='html')]

def setup(app):
    setup.app = app
    setup.confdir = app.confdir

    app.add_directive(
        'codebox', codeboxDirective)