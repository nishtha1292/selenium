# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from .firefox.webdriver import WebDriver as Firefox  # noqa
from .firefox.firefox_profile import FirefoxProfile  # noqa
from .firefox.options import Options as FirefoxOptions  # noqa
from .chrome.webdriver import WebDriver as Chrome  # noqa
from .chrome.options import Options as ChromeOptions  # noqa
from .ie.webdriver import WebDriver as Ie  # noqa
from .ie.options import Options as IeOptions  # noqa
from .edge.webdriver import WebDriver as Edge  # noqa
from .edge.webdriver import WebDriver as ChromiumEdge  # noqa
from .edge.options import Options as EdgeOptions  # noqa
from .safari.webdriver import WebDriver as Safari  # noqa
from .webkitgtk.webdriver import WebDriver as WebKitGTK  # noqa
from .webkitgtk.options import Options as WebKitGTKOptions  # noqa
from .wpewebkit.webdriver import WebDriver as WPEWebKit  # noqa
from .wpewebkit.options import Options as WPEWebKitOptions  # noqa
from .remote.webdriver import WebDriver as Remote  # noqa
from .common.desired_capabilities import DesiredCapabilities  # noqa
from .common.action_chains import ActionChains  # noqa
from .common.proxy import Proxy  # noqa
from .common.keys import Keys  # noqa

__version__ = '4.2.0'

# We need an explicit __all__ because the above won't otherwise be exported.
__all__ = [
    "Firefox",
    "FirefoxProfile",
    "FirefoxOptions",
    "Chrome",
    "ChromeOptions",
    "Ie",
    "IeOptions",
    "Edge",
    "ChromiumEdge",
    "EdgeOptions",
    "Opera",
    "Safari",
    "WebKitGTK",
    "WebKitGTKOptions",
    "WPEWebKit",
    "WPEWebKitOptions",
    "Remote",
    "DesiredCapabilities",
    "ActionChains",
    "Proxy",
    "Keys",
]
