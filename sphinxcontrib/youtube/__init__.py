#-*- coding:utf-8 -*-
u'''
embedding youtube video to sphinx

usage:

First of all, add `sphinxcontrib-adaptive-youtube` to sphinx extension list in conf.py

.. code-block:: python

   extensions = ['sphinxcontrib-adaptive-youtube']


then use `youtube` directive.

You can specify video by video url or video id.

.. code-block:: rst

   .. youtube:: Ql9sn3aLLlI


finally, build your sphinx project.

.. code-block:: sh

   $ make html

'''

__version__ = '0.0.1'
__author__ = '@john_sane'


from . import youtube

node_visitors = youtube._NODE_VISITORS

def setup(app):

   app.add_node(youtube.youtube, **node_visitors)
   app.add_directive("youtube", youtube.YouTube)