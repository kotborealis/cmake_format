from pathlib import Path
import collections

def yaml_odict_handler(dumper, value):
  """
  Represent ordered dictionaries as yaml maps.
  """
  return dumper.represent_mapping(u'tag:yaml.org,2002:map', value)


def yaml_register_odict(dumper):
  """
  Register an order dictionary handler with the given yaml dumper
  """
  dumper.add_representer(collections.OrderedDict, yaml_odict_handler)


def detect_line_endings(infile_content):
  windows_count = infile_content.count('\r\n')
  unix_count = infile_content.count('\n') - windows_count
  if windows_count > unix_count:
    return 'windows'

  return 'unix'


def collect_directory(directory):
  files = []

  # recurse over all *.cmake files
  for path in Path(directory).rglob('*.cmake'):
    files.append(str(path))

  # recurse over all CMakeLists.txt files
  for path in Path(directory).rglob('CMakeLists.txt'):
    files.append(str(path))

  return files