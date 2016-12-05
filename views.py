# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from pprint import pprint

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import Context
from django.template import Template
from django.template.loader import render_to_string
from django.template.loader_tags import BlockContext


def print_blocks(self, name):
    pprint(dict(self.blocks))
    print('-'*10)
    try:
        return self.blocks[name][-1]
    except IndexError:
        return None
if BlockContext.get_block != print_blocks:
    BlockContext.get_block = print_blocks

def nodes():
    level5 = {'title': 'test5', 'children':[]}
    level4 = {'title': 'test4', 'children':[level5]}
    level6 = {'title': 'test6', 'children':[]}
    level3 = {'title': 'test3', 'children':[level6]}
    level2 = {'title': 'test2', 'children': [level3, level4]}
    level1 = {'title': 'test', 'children': [level2]}
    return [level1]



def sniplate_widget(request):
    t = Template("""
    {% load sniplates %}
    {% load_widgets snippy="sniplate.html" %}
    {% widget 'snippy:list' nodes=nodes %}
    """).render(Context({
        'nodes': nodes,
    }))
    return HttpResponse(t)


def include(request):
    t = render_to_string("include_root.html", {
        'nodes': nodes,
    })
    return HttpResponse(t)


def root(request):
    t = Template("""<ul>
    <li><a href="{{include}}">Include</a></li>
    <li><a href="{{sniplate}}">Sniplate (widget)</a></li>
    </ul>""").render(Context({
        'include': reverse('include'),
        'sniplate': reverse('sniplate_widget'),
    }))
    return HttpResponse(t)
