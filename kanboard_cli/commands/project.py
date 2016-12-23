# The MIT License (MIT)
#
# Copyright (c) 2016 Frederic Guillot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from cliff import lister
from cliff import show


class ShowProject(show.ShowOne):
    """Show project details"""

    def get_parser(self, prog_name):
        parser = super(ShowProject, self).get_parser(prog_name)
        parser.add_argument(
            'project',
            metavar='<project_id>',
            help='Project ID',
        )
        return parser

    def take_action(self, parsed_args):
        project = self.app.client.get_project_by_id(project_id=parsed_args.project)

        if not project:
            raise RuntimeError('Project not found')

        return self._format_project(project)

    @staticmethod
    def _format_project(project):
        columns = ('ID', 'Name', 'Description', 'Board URL')
        data = (project['id'], project['name'], project['description'], project['url']['board'])
        return columns, data


class ListProject(lister.Lister):
    """List projects that belongs to the connected user"""

    def take_action(self, parsed_args):
