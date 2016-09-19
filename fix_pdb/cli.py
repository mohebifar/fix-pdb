#!/usr/bin/env python
import click
import os

from els_atn import fix_els_atn


@click.group()
@click.option('--path', type=click.Path(readable=True, exists=True), required=False, default='.')
def cli(path):
    cli.path = path


@cli.command()
def els_atn():
    read_path(cli.path, fix_els_atn)


def read_path(path, fn):
    if os.path.isdir(path):
        for filename in os.listdir(path):
            output = fn(filename)

            if isinstance(output, basestring):
                click.echo(output)
    else:
        output = fn(path)
        if isinstance(output, basestring):
            click.echo(output)


if __name__ == '__main__':
    cli()
