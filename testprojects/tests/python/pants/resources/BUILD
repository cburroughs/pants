# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_tests(
  name = 'resource_target',
  sources = ['test_resources.py'],
  resource_targets=[
    ':resources',
  ],
)

resources(
  name='resources',
  sources=['foo.txt'],
)
