# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2010-2012 Fabien Potencier
    :license: MIT, see LICENSE for more details.
"""

from docutils.parsers.rst import Directive, directives
from docutils import nodes
from string import upper

class codebox(nodes.General, nodes.Element):
    pass

class CodeBox(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    formats = {
        'html':            'HTML',
        'xml':             'XML',
        'js':              'JS',
        'curl':            'CURL',
        'bash':            'CURL',
        'ruby':            'Ruby',
        'php':             'PHP',
        'yaml':            'YAML',
        'jinja':           'Twig',
        'html+jinja':      'Twig',
        'jinja+html':      'Twig',
        'php+html':        'PHP',
        'html+php':        'PHP',
        'ini':             'INI'
    }

    def run(self):
        env = self.state.document.settings.env

        node = nodes.Element()
        node.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, node)

        nav = []
        blocks = []
        for i, child in enumerate(node):
            if isinstance(child, nodes.literal_block):

                targetid = "%s" % self.formats[child['language']]
                # targetid = "code-box-%d" % env.new_serialno('code-box')
                targetnode = nodes.target('', '', ids=[targetid])

                block = nodes.section('')                
                block.append(child)                
                block.set_class('code')
                block.set_class('code-'+self.formats[child['language']])
                block.set_class('tab-pane')
                if i == 0:
                    block.set_class('active')

                para = nodes.paragraph()
                para += nodes.reference(self.formats[child['language']], self.formats[child['language']], refuri='#' + targetid)

                entry = nodes.list_item('')
                entry.append(para)
                entry.set_class('codebox-tab')
                entry.set_class('codebox-tab-'+self.formats[child['language']])

                if i == 0:
                    entry.set_class('active')

                nav.append(entry)
                blocks.append(targetnode)
                blocks.append(block)

        resultnode = codebox()
        navList = nodes.bullet_list('', *nav, ids=['myTab'])
        navList.set_class('nav')
        resultnode.append(navList)
        tabContent = nodes.section('')
        tabContent.set_class('tab-content')
        tabContent.extend(blocks)
        resultnode.append(tabContent)

        return [resultnode]

def visit_codebox_html(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='code-box'))

def depart_codebox_html(self, node):
    self.body.append('</div>\n')

def visit_codebox_latex(self, node):
    pass

def depart_codebox_latex(self, node):
    pass

def setup(app):
    app.add_node(codebox,
                 html=(visit_codebox_html, depart_codebox_html),
                 latex=(visit_codebox_latex, depart_codebox_latex))
    app.add_directive('code-box', CodeBox)
