# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import pkgutil


def test_load_foo_txt():
  contents = pkgutil.get_data(__name__, 'foo.txt')
  assert contents == 'foo'
