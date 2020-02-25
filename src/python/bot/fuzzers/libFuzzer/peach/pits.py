# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Dictionary to keep track of pit information."""

from system import environment
import os


def get_path(grammar):
  # If the target has no grammar, do not use this strategy.

  if not grammar:
    return None

  pit_dir = os.path.join(environment.get_platform_resources_directory(),
                         'peach', 'pits')
  pit_path = os.path.join(pit_dir, grammar + '.xml')

  if not os.path.exists(pit_path):
    logs.log_error('Peach Mutator is being used with the grammar named ' +
                   grammar + ' that does not have a corresponding pit.')
    return None

  return pit_path