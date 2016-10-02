#    Copyright 2013-2015 ARM Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# pylint: disable=E1101

from wlauto import UiAutomatorWorkload, Parameter
from wlauto.utils.types import range_dict


class Cameracapture(UiAutomatorWorkload):

    name = 'cameracapture'
    description = """
    Uses in-built Android camera app to take photos.

    """
    package = 'com.google.android.gallery3d'
    activity = 'com.android.camera.CameraActivity'

    api_packages = range_dict()
    api_packages[1] = 'com.google.android.gallery3d'
    api_packages[23] = 'com.google.android.GoogleCamera'

    parameters = [
        Parameter('no_of_captures', kind=int, default=5,
                  description='Number of photos to be taken.'),
        Parameter('time_between_captures', kind=int, default=5,
                  description='Time, in seconds, between two consecutive camera clicks.'),
    ]

    def initialize(self, context):
        api = self.device.get_sdk_version()
        self.uiauto_params['no_of_captures'] = self.no_of_captures
        self.uiauto_params['time_between_captures'] = self.time_between_captures
        self.uiauto_params['api_level'] = api
        self.package = self.api_packages[api]
        version = self.device.get_installed_package_version(self.package)
        version = version.replace(' ', '_')
        self.uiauto_params['version'] = version

    def setup(self, context):
        super(Cameracapture, self).setup(context)
        self.device.execute('am start -n {}/{}'.format(self.package, self.activity))

    def teardown(self, context):
        self.device.execute('am force-stop {}'.format(self.package))
        super(Cameracapture, self).teardown(context)
