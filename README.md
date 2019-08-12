Tuesmon contrib gitlab auth
=========================

[![Kaleidos Project](http://kaleidos.net/static/img/badge.png)](https://github.com/kaleidos "Kaleidos Project")
[![Managed with Tuesmon.com](https://img.shields.io/badge/managed%20with-TUESMON.io-709f14.svg)](https://manage.tuesmon.com/project/tuesmon/ "Managed with Tuesmon.com")

The Tuesmon plugin for gitlab authentication (Ported from official gitlab auth).

Installation
------------
### Production env

#### Tuesmon Back

In your Tuesmon back python virtualenv install the pip package `tuesmon-contrib-gitlab-auth-official` with:

```bash
  pip install tuesmon-contrib-gitlab-auth-official
```

Modify your `settings/local.py` and include the line:

```python
  INSTALLED_APPS += ["tuesmon_contrib_gitlab_auth"]

  # Get these from Admin -> Applications
  GITLAB_API_CLIENT_ID = "YOUR-GITLAB-CLIENT-ID"
  GITLAB_API_CLIENT_SECRET = "YOUR-GITLAB-CLIENT-SECRET"
  GITLAB_URL="YOUR-GITLAB-URL"
```

#### Tuesmon Front

Download in your `dist/plugins/` directory of Tuesmon front the `tuesmon-contrib-gitlab-auth` compiled code (you need subversion in your system):

```bash
  cd dist/
  mkdir -p plugins
  cd plugins
  svn export "https://github.com/tuesmoncom/tuesmon-contrib-gitlab-auth/tags/$(pip show tuesmon-contrib-gitlab-auth-official | awk '/^Version: /{print $2}')/front/dist"  "gitlab-auth"
```

Include in your `dist/conf.json` in the 'contribPlugins' list the value `"/plugins/gitlab-auth/gitlab-auth.json"`:

```json
...
    "gitLabClientId": "YOUR-GITLAB-CLIENT-ID",
    "gitLabUrl": "YOUR-GITLAB-URL",
    "contribPlugins": [
        (...)
        "/plugins/gitlab-auth/gitlab-auth.json"
    ]
...
```

### Dev env

#### Tuesmon Back

Clone the repo and

```bash
  cd tuesmon-contrib-gitlab-auth/back
  workon tuesmon
  pip install -e .
```

Modify `tuesmon-back/settings/local.py` and include the line:

```python
  INSTALLED_APPS += ["tuesmon_contrib_gitlab_auth"]

  # Get these from Admin -> Applications
  GITHUB_API_CLIENT_ID = "YOUR-GITLAB-CLIENT-ID"
  GITHUB_API_CLIENT_SECRET = "YOUR-GITLAB-CLIENT-SECRET"
  GITLAB_URL="YOUR-GITLAB-URL"

```

#### Tuesmon Front

After clone the repo link `dist` in `tuesmon-front` plugins directory:

```bash
  cd tuesmon-front/dist
  mkdir -p plugins
  cd plugins
  ln -s ../../../tuesmon-contrib-gitlab-auth/front/dist gitlab-auth
```

Include in your `dist/conf.json` in the 'contribPlugins' list the value `"/plugins/gitlab-auth/gitlab-auth.json"`:

```json
...
    "gitLabClientId": "YOUR-GITLAB-CLIENT-ID",
    "gitLabUrl": "YOUR-GITLAB-URL",
    "contribPlugins": [
        (...)
        "/plugins/gitlab-auth/gitlab-auth.json"
    ]
...
```

In the plugin source dir `tuesmon-contrib-gitlab-auth/front` run

```bash
npm install
```
and use:

- `gulp` to regenerate the source and watch for changes.
- `gulp build` to only regenerate the source.

Running tests
-------------

We only have backend tests, you have to add your `tuesmon-back` directory to the
PYTHONPATH environment variable, and run py.test, for example:

```bash
  cd back
  add2virtualenv /home/tuesmon/tuesmon-back/
  py.test
```
