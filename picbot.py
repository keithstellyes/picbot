import discord
import asyncio
import picmgr
import random
import os

#client = discord.Client()

class PicBot(discord.Client):
    def __init__(self, token, pic_dir=picmgr.DEFAULT_PIC_DIR,
                 start_cmd='/pb<', end_cmd='>'):
        self.start_cmd = start_cmd
        self.end_cmd = end_cmd
        super(self.__class__, self).__init__()
        picmgr.init(pic_dir)
        super().run(token)
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('tags:', picmgr.tags)

    async def on_message(self, message):
        #if message.content.startswith('@pb'):
        start_cmd = self.start_cmd
        end_cmd = self.end_cmd
        if start_cmd in message.content and end_cmd in message.content:
            print('received:', message.content)
            li = message.content.index(start_cmd) + len(start_cmd)
            ri = message.content[li:].index(end_cmd) + li
            tags = message.content[li:ri].split(' ')
            print('TAGS:', tags)
            possible = None
            for tag in tags:
                if tag not in picmgr.tags:
                    msg = 'Unsupported tag: ' + tag
                    await self.respond(message, msg)
                    return
                if possible is None:
                    possible = picmgr.tag_table[tag]
                else:
                    possible += picmgr.tag_table[tag]
            if possible is None:
                await self.respond(message, 'Picking random image')
            elif len(possible) == 0:
                await self.respond(message, 'No pics with tags:' + ','.join(tags))
            else:
                fname = random.choice(possible)
                with open(fname, 'rb') as f:
                    await self.send_file(message.channel, f)
    async def respond(self, rec_msg, send_msg):
        print('[sending]', send_msg)
        await self.send_message(rec_msg.channel, send_msg)

def read_file(fname):
    f = open(fname, 'r')
    s = f.read().strip()
    f.close()
    return s

# CONFIG ME :)
# you can use the read_file(filepath) function to use the contents of a file
# note that any leading or trailing whitespace will be trimmed for your
# convenience
# supported options can be found in the constructor, or in this list:
#     token     (required)
#     pic_dir   (directory to load images from)
#     start_cmd (default: /pb<
#     end_cmd   (default: >)
# don't forget to put commans between options
PicBot(
    token=read_file('token')
)
