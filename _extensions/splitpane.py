# -*- coding: utf-8 -*-
from docutils.parsers.rst import Directive, directives
from docutils import nodes
from string import upper

class splitpane(nodes.General, nodes.Element):
    pass

class SplitPane(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}

    def run(self):
        env = self.state.document.settings.env

        node = nodes.Element()
        node.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, node)

        panes = []
        for i, child in enumerate(node):
            pane = nodes.section('')
            pane.append(child)
            if i % 2 == 0:
                pane.set_class('col-sm-8')
            else:
                pane.set_class('col-sm-4')
                pane.set_class('examples')
            panes.append(pane)

        resultnode = splitpane()
        resultnode.extend(panes)

        return [resultnode]

def visit_splitpane_html(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='row'))

def depart_splitpane_html(self, node):
    self.body.append('</div>\n')

def visit_splitpane_latex(self, node):
    pass

def depart_splitpane_latex(self, node):
    pass

def setup(app):
    app.add_node(splitpane,
                 html=(visit_splitpane_html, depart_splitpane_html),
                 latex=(visit_splitpane_latex, depart_splitpane_latex))
    app.add_directive('split-pane', SplitPane)
