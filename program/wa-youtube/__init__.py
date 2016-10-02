#    Copyright 2014-2016 ARM Limited
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

from wlauto import AndroidUxPerfWorkload, Parameter
from wlauto.exceptions import WorkloadError


class Youtube(AndroidUxPerfWorkload):

    name = 'youtube'
    package = 'com.google.android.youtube'
    min_apk_version = '11.19.56'
    max_apk_version = None  # works with latest (11.33.58) at time of publishing this
    activity = ''
    description = '''
    A workload to perform standard productivity tasks within YouTube.

    The workload plays a video from the app, determined by the ``video_source`` parameter.
    While the video is playing, a some common actions are done such as video seeking, pausing
    playback and navigating the comments section.

    Test description:
    The ``video_source`` parameter determines where the video to be played will be found
    in the app. Possible values are ``search``, ``home``, ``my_videos``, and ``trending``.
    -A. search - Goes to the search view, does a search for the given term, and plays the
        first video in the results. The parameter ``search_term`` must also be provided
        in the agenda for this to work. This is the default mode.
    -B. home - Scrolls down once on the app's home page to avoid ads (if present, would be
        first video), then select and plays the video that appears at the top of the list.
    -C. my_videos - Goes to the 'My Videos' section of the user's account page and plays a
        video from there. The user must have at least one uploaded video for this to work.
    -D. trending - Goes to the 'Trending Videos' section of the app, and plays the first
        video in the trending videos list.

    For the selected video source, the following test steps are performed:
    1.  Navigate to the general app settings page to disable autoplay. This improves test
        stability and predictability by preventing screen transition to load a new video
        while in the middle of the test.
    2.  Select the video from the source specified above, and dismiss any potential embedded
        advert that may pop-up before the actual video.
    3.  Let the video play for a few seconds, pause it, then resume.
    4.  Expand the info card that shows video metadata, then collapse it again.
    5.  Scroll down to the end of related videos and comments under the info card, and then
        back up to the start. A maximum of 5 swipe actions is performed in either direction.
    '''

    parameters = [
        Parameter('video_source', kind=str, default='search',
                  allowed_values=['home', 'my_videos', 'search', 'trending'],
                  description='''
                  Determines where to play the video from. This can either be from the
                  YouTube home, my videos section, trending videos or found in search.
                  '''),
        Parameter('search_term', kind=str,
                  default='Big Buck Bunny 60fps 4K - Official Blender Foundation Short Film',
                  description='''
                  The search term to use when ``video_source`` is set to ``search``. Ignored otherwise.
                  '''),
    ]

    view = [
        package + '/com.google.android.apps.youtube.app.WatchWhileActivity',
        package + '/com.google.android.apps.youtube.app.honeycomb.SettingsActivity',
    ]

    requires_network = True

    def __init__(self, device, **kwargs):
        super(Youtube, self).__init__(device, **kwargs)
        self.run_timeout = 300

    def validate(self):
        if self.video_source == 'search' and not self.search_term:
            raise WorkloadError("Param 'search_term' must be specified when video source is 'search'")

        self.uiauto_params['package'] = self.package
        self.uiauto_params['video_source'] = self.video_source
        self.uiauto_params['search_term'] = self.search_term.replace(' ', '0space0')
