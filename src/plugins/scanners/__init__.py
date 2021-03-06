#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
 #the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This file contains, in execution order, a list of the available
scanners that Kibble has.
"""

import importlib

# Define, in order of priority, all scanner plugins we have
__all__ = [
    'git-sync',     # This needs to precede other VCS scanners!
    'git-census',
    'git-sloc',
    'git-evolution',
    'jira',
    'ponymail',
    'ponymail-tone',
    'pipermail',
    'github-issues',
    'bugzilla',
    'gerrit'
    ]

# Import each plugin into a hash called 'scanners'
scanners = {}

for p in __all__:
    scanner = importlib.import_module("plugins.scanners.%s" % p)
    scanners[p] = scanner
    # This should ideally be pprint, meh
    print("[core]: Loaded plugins/scanners/%s v/%s (%s)" % (p, scanner.version, scanner.title))

def enumerate():
    """ Returns the scanners as a dictionary, sorted by run-order """
    for p in __all__:
        yield (p, scanners[p])

