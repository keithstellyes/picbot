# picbot
A discord bot that uploads a random picture that has certain tags

# Using

The bot is used ina channel by the command

`/pb<tag1>` or `/pb<tag1 tag2>` etc... Also, it can be embedded in a message
Like so:

`im out peace \pb<peace>` will cause the picbot to send a random image with
the tag 'peace'`

# Set up:

Launch `picbot.py` with Python 3, putting your token in a file simply called `token` in the main directory. 

# adding images
To add an image, add an image to the `pics/` directory, hyphens separate tags. You can add a number at the very end, this number must be at the end, however, as everything after will be ignored. Examples:

A `.jpg` with "cool" and "bob" as tags:

Some ways it can be done are:

`pics/cool-bob.jpg`

`pics/bob-cool.jpg`

`pics/bob-cool-234354.jpg`

However, these will not work:

`pics/bob-324-cool.jpg`

The above will simply yield `bob` as a tag, but not `cool`

`pics/bob-cool42.jpg`

The above will yield `bob` and `cool42` as tags.

# Nice-to-haves

* Directory structure for `pics/` to improve organizations

* `tag-aliases` text file to allow aliasing of tags

* Images uploaded by users with proper privliges in a Discord channel

* Actual customization and parameters of the discord bot (Probably do PHP-style  configs where the config is Python source code itself)
