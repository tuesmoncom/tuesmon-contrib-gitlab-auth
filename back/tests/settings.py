# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from settings.testing import *

SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False
CELERY_ALWAYS_EAGER = True
CELERY_ENABLED = False

MEDIA_ROOT = "/tmp"

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
INSTALLED_APPS = INSTALLED_APPS + [
    "tuesmon_contrib_gitlab_auth",
]
INSTALLED_APPS = list(set(INSTALLED_APPS) - set(["tuesmon.hooks.github", "tuesmon.hooks.gitlab", "tuesmon.hooks.bitbucket"]))
