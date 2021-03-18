import discord
from discord.ext import tasks
import random
import asyncio
import time

client = discord.Client()
true_n_general = 802684938381557840  #nme
testing_id = 815405498412171294  #testing
doangus = 817632403228196874  #doangus

vc_id_list = [doangus, true_n_general]  #doangus then general
#vc_id_list = [testing_id]


def filewritev(time_now, timertime):
    timefile = open('jointime.txt', "r+")
    timefile.truncate()
    timefile.writelines(str(time_now) + '\n' + str(timertime))
    timefile.close()


@client.event
async def on_ready():
    print('voice ready')


#@client.event
#async def on_message(message):
#if message.content.startswith('$fuck'):
#await message.channel.send('dwadwa')

#songlist = ['south', 'yuyu', 'iceage', 'deepboom', 'among', 'higgtheme', 'jahrant', 'sutekime', 't1', 'wee', 'zaregoto', 'penis-1h', 'xqcnme', 'hachi', 'hatersbroke', 'horsepiano', 'humor', 'pop', 'jujutsu', 'duck', 'cancun_sega', 'ecco_lal', 'cockver10', 'bg2m']
#songvolume = [0.3, 0.25, 0.1, 3, 1, 0.2, 0.6, 0.2, 0.7, 1.2, 0.2, 0.12, 0.5, 0.2, 0.3, 0.4, 0.3, 1, 0.24, 0.24, 0.34, 0.3, 0.2, 0.3] #each song needs a different volume :/

songlistwvol = {
    'south': 0.3,  #0
    'yuyu': 0.25,  #1
    'iceage': 0.1,  #2
    'deepboom': 3,  #3
    'among': 1.5,  #4
    'higgtheme': 0.42,  #5
    'jahrant': 8,  #6
    'sutekime': 0.2,  #7
    't1': 4,  #8
    'wee': 1.2,  #9
    'zaregoto': 0.2,  #10
    'penis-1h': 0.12,  #11
    'xqcnme': 0.5,  #12
    'hachi': 0.2,  #13
    'hatersbroke': 0.3,  #14
    'horsepiano': 0.7,  #15
    'humor': 0.3,  #16
    'pop': 50,  #17
    'jujutsu': 0.24,  #18
    'duck': 0.24,  #19
    'cancun_sega': 0.34,  #20
    'ecco_lal': 0.3,  #21
    'cockver10': 0.2,  #22
    'bg2m': 0.3,  #23
    'codlaugh': 0.5,  #24
    'october': 1.4,  #25
    'cockmuncher': 10,  #26
    'among2': 1.5, #27
    'bladee': 1.2 #28
}
songlist = list(songlistwvol)


@client.event
async def join(boice_channel):
    #global channel
    print(f"Got channel {boice_channel}")
    global vc
    vc = await boice_channel.connect()


@client.event
async def leave(boice_channel):
    print(f"Leaving channel {boice_channel}")
    await vc.disconnect()


@client.event
async def playsong(index):
    print('playing song')
    #songindex = random.randint(0, len(songlist) - 1)
    #songindex = 0
    song = songlist[index]
    audio = discord.FFmpegPCMAudio(source="songs/" + song + ".mp3")
    source = discord.PCMVolumeTransformer(audio)
    source.volume = songlistwvol[song]
    vc.play(source)  #this shouldprobably be await but whatever it works lol


#@tasks.loop()
#@client.event
#async def join_loop():
#global timer
#global nowtimev
#timer = random.randint(10, 54000)
#nowtimev = time.time()
#await asyncio.sleep(timer)
##await asyncio.sleep(5)
#await join(true_n_general)
#timer = random.randint(10, 54000)
#nowtimev = time.time()
#await asyncio.sleep(timer)
##await asyncio.sleep(5)
#await leave()


@tasks.loop()
@client.event
async def join_song():
    global timer
    global nowtimev
    timer = random.randint(10, 72000)  #20 hours
    nowtimev = time.time()
    await asyncio.sleep(3)
    filewritev(nowtimev, timer)
    await asyncio.sleep(timer)
    #await asyncio.sleep(3)
    songindex = random.randint(0, len(songlist) - 1)
    #songindex = 16
    for item in vc_id_list:
        channel = client.get_channel(item)
        await join(channel)
        await asyncio.sleep(0.5)
        await playsong(songindex)
        while vc.is_playing():
            await asyncio.sleep(1)
        await leave(channel)


@join_song.before_loop  #im a fucking idiot
async def before_join_song():
    await client.wait_until_ready()
    await asyncio.sleep(1)
    print('voice loop ready')


#join_loop.start()
join_song.start()
