import os
import sys
from argparse import ArgumentParser, RawTextHelpFormatter

import jinja2
from livereload import Server

import file_utils

TEMPLATES = 'templates/'
ASSETS = 'assets/'
ROOT = 'live_website/'


def collect_assets():
    file_utils.force_copy_folder(ASSETS, os.path.join(ROOT, ASSETS))


def render_template(environment, name):
    rendered_template = environment.get_template(name).render()
    destination_path = os.path.join(ROOT, name)
    file_utils.dump_html_to_file(rendered_template, destination_path)


def render_templates():
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES)
    )
    render_template(environment, 'index.html')
    render_template(environment, 'orders.html')


def parse_args(argv):
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        'action',
        choices=('runserver', 'reset'),
        help='runserver -- start livereload server\n'
             'reset -- remove all generated files and generate them again'
    )
    return parser.parse_args(argv)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    if args.action == 'reset':
        file_utils.delete_contents_of_folder(ROOT)
        collect_assets()
        render_templates()
    if args.action == 'runserver':
        server = Server()
        server.watch(TEMPLATES, render_templates)
        server.watch(ASSETS, collect_assets)
        server.serve(root=ROOT)
