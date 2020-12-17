[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://en.wikipedia.org/wiki/Open_source)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7d29dde165294d3283f92ec8f8638369)](https://www.codacy.com/gh/Squirrel-Network/nebula8/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Squirrel-Network/nebula8&amp;utm_campaign=Badge_Grade) [![Group](https://img.shields.io/badge/Group-SquirrelNetwork-blue)](https://t.me/squirrelnetwork)
# NEBULA BOT

## Getting started

- <a href="https://github.com/Squirrel-Network/nebula8/wiki/How-To-start">How to Start</a>
- <a href="https://github.com/Squirrel-Network/nebula8/wiki/Command-List">Command list of the bot</a>

# Official API
- <a href="https://github.com/Squirrel-Network/api_nebula">Go Here</a>

# Official Resources
- <a href="https://squirrel-network.online/knowhere/">Knowhere (Blacklist Search)</a>

## Project Structure

```markdown

│   config.example.py
│   main.py
│
├───core
│   │   __init__.py
│   │
│   ├───commands
│   │   │   index.py
│   │   │   __init__.py
│   │   │
│   │   ├───admin
│   │   │       ban.py
│   │   │       info_group.py
│   │   │       mute.py
│   │   │       set_lang.py
│   │   │       warn.py
│   │   │       __init__.py
│   │   │
│   │   ├───owner
│   │   │       broadcast.py
│   │   │       exit.py
│   │   │       server_info.py
│   │   │       superban.py
│   │   │       test.py
│   │   │       __init__.py
│   │   │
│   │   └───public
│   │           report.py
│   │           rules.py
│   │           source.py
│   │           start.py
│   │           __init__.py
│   │
│   ├───database
│   │   │   db_connect.py
│   │   │   __init__.py
│   │   │
│   │   └───repository
│   │           group.py
│   │           group_language.py
│   │           superban.py
│   │           user.py
│   │           __init__.py
│   │
│   ├───decorators
│   │       admin.py
│   │       delete.py
│   │       owner.py
│   │       private.py
│   │       public.py
│   │       __init__.py
│   │
│   ├───handlers
│   │       errors.py
│   │       handlers_index.py
│   │       logs.py
│   │       superban.py
│   │       welcome.py
│   │       __init__.py
│   │
│   └───utilities
│           functions.py
│           menu.py
│           message.py
│           monads.py
│           regex.py
│           strings.py
│           __init__.py
│
├───languages
│       EN.py
│       getLang.py
│       IT.py
│       __init__.py
│
└───plugins
        distrowatch.py
        google.py
        mdn_search.py
        plugin_index.py
        __init__.py
```