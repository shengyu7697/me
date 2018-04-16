#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# render.py
#
# Copyright (C) 2013 -  Wei-Ning Huang (AZ) <aitjcize@gmail.com>
# All Rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#


import jinja2
import math
import re
import sys
import yaml


def tagNameToClass(d, t):
    return d['tags-map'][t]


def remove_tag(text):
    return re.sub(text, '<.*>', '')


def main():
    with open('templates/profile.yml', 'r') as f:
        data = f.read()

    with open('templates/template.html', 'r') as f:
        tmpl = f.read().decode('utf8')

    env = jinja2.Environment()
    env.filters['remove_tag'] = remove_tag
    template = env.from_string(tmpl)
    args = yaml.load(data)

    with open('dist/index.html', 'w') as f:
        content = template.render(data=args, tagNameToClass=tagNameToClass,
                len=len, ceil=math.ceil)
        f.write(content.encode('utf8'))

if __name__ == '__main__':
    main()
