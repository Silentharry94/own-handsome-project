#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/23/5:28 PM
# @Author  : Hanley
# @File    : cmdline.py
# @Desc    :
import click


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-V', '--version', is_flag=True, help='Show version and exit.')
def main(ctx, version):
    if version:
        click.echo('0.1.0')
    elif ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == '__main__':
    main()
