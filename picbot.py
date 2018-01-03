import discord
import asyncio
import picmgr
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('tags:', picmgr.tags)

@client.event
async def on_message(message):
    #if message.content.startswith('@pb'):
    if '/pb<' in message.content and '>' in message.content:
        print('received:', message.content)
        li = message.content.index('/pb<') + len('/pb<')
        ri = message.content[li:].index('>') + li
        tags = message.content[li:ri].split(' ')
        print('TAGS:', tags)
        possible = None
        for tag in tags:
            if tag not in picmgr.tags:
                msg = 'Unsupported tag: ' + tag
                print(msg)
                await client.send_message(message.channel, msg)
            if possible is None:
                possible = picmgr.tag_table[tag]
            else:
                possible += picmgr.tag_table[tag]
        if possible is None:
            print('Randonm pic')
            await client.send_message(message.channel, 'Picking a pic of any tag')
        elif len(possible) == 0:
            msg = 'No pics with tags:' ','.join(tags)
            print(msg)
            await client.send_message(message.channel, msg)
        else:
            fname = random.choice(possible)
            with open(os.path.join('pics', fname), 'rb') as f:
                await client.send_file(message.channel, f)

        #print('sending message')
        #await client.send_message(message.channel, 'You talkin to me?')
        #with open('pepe.jpg', 'rb') as f:
        #    await client.send_file(message.channel, f)

client.run(open('token','r').read().strip())
