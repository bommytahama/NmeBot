#bot for our private discord NME (Noose Maniacs)
#join here: https://discord.com/invite/mjxC8M2 <3
#i am terry davis

#2 DO:
#random "mmmmmmm"
#weather?
#kitty meow

import keep_alive
from discord.ext import tasks
import asyncio
import random
from PIL import Image, ImageFont, ImageDraw
import discord
import os
import time
import joinboice
#import namiping

exec(open("joinboice.py").read())
exec(open("namiping.py").read())

#light blue: (135, 206, 250)
#pink: (255, 192, 203)
#dark(?) pink: (219, 112, 147)

client = discord.Client()
#target_channel_id = 815405711726084156 #testing server
target_channel_id = 815084936985706506  #noose maniacs server
general_id = 725245718750822411  #t_n general chat

msg = ''
wordsfile = open('20k_words.txt', 'r')
wordlist = []
for line in wordsfile:
    stripped_line = line.strip()
    wordlist.append(stripped_line)
wordsfile.close()


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    #print(str(time.gmtime()))
    #print(time.gmtime())
    #message_channel = client.get_channel(725245718750822411) #nme general
    #await message_channel.send('hi higg')
    #await client.get_channel(802684938381557840).connect()
    #message_channel = client.get_channel(725245718750822411)


@client.event
async def on_message(message):
    #if message.author == client.user:
    #  return
    def time_left(input_nowtime, input_waitime):
        nowtsec = time.time()
        elapsed = nowtsec - input_nowtime
        timeleft = input_waitime - elapsed
        return str(int(timeleft))

    def filereadtimes(filename_):
        timefile = open(filename_, 'r')
        linelist = timefile.readlines()
        #ini_string[:-(len(sstring))]
        nowtimev1 = linelist[0]
        timer = float(linelist[1])
        timefile.close()
        nowtime = float(nowtimev1[:-(2)])
        return [nowtime, timer]

    def read_return_time(file_name):
        l = filereadtimes(file_name)
        r = time_left(l[0], l[1])
        return r

    def ping_pong(input_message):
        return_message = 'pong' + input_message[4:] + ' :ping_pong:'
        if 'jah' in input_message:
            return return_message
        banned_1 = ['', ' ']
        banned_2 = ['c', 's']
        banned_3 = ['i', 'ee', 'ea']
        banned_4 = ['c', 'k', 'ck']
        banned_5 = ['a', 'ah', 'u', 'uh']
        for word1 in banned_1:
            for word2 in banned_2:
                for word3 in banned_3:
                    for word4 in banned_4:
                        for word5 in banned_5:
                            fullword = word1 + word2 + word3 + word4 + word5
                            if fullword in input_message:
                                return_message = 'shut up higg'
                                return return_message
        #for word in banned_words:
        #if message.content.startswith('ping' + word):
        #return_message = 'fuck you higg'
        return return_message

    async def send_message(input_message, output):
        await input_message.channel.send(output)

    async def join_channel(input_message):
        await join_song_com(input_message.author.voice.channel.id,
                            input_message.content[len('$joinvoice '):])

    command_dict = {
        '$words': send_message,  #str(len(wordlist))
        '$timeleftcheadle': send_message,  #time_left(tsecc, wtimec)
        '$voicetimer': send_message,  #read_return_time('jointime.txt')
        'ping': send_message,  #ping_pong(str(message.content))
        '$lensonglist': send_message,  #len(joinboice.songlist)
        '$joinvoice':
        join_channel,  #message.author.voice.channel.id, message.content[11:]
        '$namitime': send_message  #read_return_time('namitime.txt')
    }

    command_namelist = list(command_dict)

    command_arglist = [
        [message, str(len(wordlist)) + ' words'],
        [message, time_left(tsecc, wtimec) + ' seconds'],
        [message, read_return_time('jointime.txt') + ' seconds'],
        [message, ping_pong(str(message.content))],
        [message, str(len(joinboice.songlist)) + ' songs'], message,
        [message, read_return_time('namitime.txt') + ' seconds']
    ]

    for command in command_namelist:
        if message.content.startswith(command):
            #print('test')
            command_args = command_arglist[command_namelist.index(command)]
            try:
                await command_dict[command](command_args[0], command_args[1])
            except:
                await command_dict[command](command_args)
            return
    #def voice_time():
    #    timefile = open('jointime.txt', 'r')
    #    linelist = timefile.readlines()
    #    #ini_string[:-(len(sstring))]
    #    nowtimev1 = linelist[0]
    #    timer = float(linelist[1])
    #    timefile.close()
    #    nowtimev = float(nowtimev1[:-(2)])
    #    nowtsecv = time.time()
    #    elapsedv = nowtsecv - nowtimev
    #    timeleftv = timer - elapsedv
    #    await message.channel.send(str(int(timeleftv)) + ' seconds')
    ##if message.content == 'ping' or message.content == 'ping :ping_pong:':
    ##await message.channel.send('pong :ping_pong:')
    #if message.content.startswith('ping'):
    #    #banned_words = [
    #        #'cica', 'seecuh', 'seecah', 'sicuh', 'sicah',
    #        #' cica', ' seecuh', ' seecah', ' sicuh',
    #       # ' sicah', 'seaca', 'sica', ' seaca', ' sica',
    #        #'sicah', ' sicah', 'sicuh', ' sicuh',
    #    #]
    #    return_message = 'pong' + message.content[4:] + ' :ping_pong:'
    #    banned_1 = ['', ' ']
    #    banned_2 = ['c', 's']
    #    banned_3 = ['i', 'ee', 'ea']
    #    banned_4 = ['c', 'k', 'ck']
    #    banned_5 = ['a', 'ah', 'u', 'uh']
    #    for word1 in banned_1:
    #      for word2 in banned_2:
    #        for word3 in banned_3:
    #          for word4 in banned_4:
    #            for word5 in banned_5:
    #              fullword = word1 + word2 + word3 + word4 + word5
    #              if 'jah' in message.content:
    #                break
    #              elif fullword in message.content:
    #                return_message = 'fuck you higg'
    #    #for word in banned_words:
    #        #if message.content.startswith('ping' + word):
    #            #return_message = 'fuck you higg'
    #    await message.channel.send(return_message)
    #    print('ponged')
    #if message.content.startswith('$lensonglist'):
    #    await message.channel.send(len(joinboice.songlist))
    #if message.content.startswith('$joinvoice'):
    #    await join_song_com(message.author.voice.channel.id,
    #                        message.content[11:])
    #    #print(str(message.author.voice.channel.id))
    #if message.content.startswith('$namitime'):
    #    timefilen = open('namitime.txt', 'r')
    #    linelist = timefilen.readlines()
    #    #ini_string[:-(len(sstring))]
    #    nowtimen1 = linelist[0]
    #    timern = float(linelist[1])
    #    timefilen.close()
    #    nowtimen = float(nowtimen1[:-(2)])
    #    nowtsecn = time.time()
    #    elapsedn = nowtsecn - nowtimen
    #    ntime_left = timern - elapsedn
    #    await message.channel.send(str(int(ntime_left)) + ' seconds left')


async def cheadlewotd():
    filename = 'dc_pics/' + str(random.randint(1, 50)) + '.jpg'
    my_image = Image.open(filename)
    with Image.open(filename) as image:
        width, height = image.size
    top_size = width * 0.083
    bot_size = width * 0.17
    top_font = ImageFont.truetype('impact.ttf', int(top_size))
    bottom_font = ImageFont.truetype('impact.ttf', int(bot_size))
    random_word = wordlist[random.randint(0, len(wordlist) - 1)]
    top_text = "Don Cheadle word of the day"
    bottom_text = random_word
    image_edit = ImageDraw.Draw(my_image)
    image_edit.text((width * 0.027, 5),
                    top_text, (135, 206, 250),
                    font=top_font)
    image_edit.text((int(width * (0.5 - (0.038 * len(bottom_text)))),
                     int(height - (bot_size * 1.3))),
                    bottom_text, (135, 206, 250),
                    font=bottom_font)
    my_image.save("result.jpg")
    message_channel = client.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send(file=discord.File('result.jpg'))
    print('cheadle sent')


@tasks.loop()
@client.event
async def timer_shit_fuck():
    global tsecc
    tsecc = time.time()
    t = time.gmtime()
    send_time_l = 7  #am #l = local
    send_time = send_time_l + 7
    global wtimec
    if send_time >= 24:
        send_time -= 24
    if t.tm_hour == send_time and t.tm_min == 0:
        print('1')
        print('sending cheadle...')
        await cheadlewotd()
    elif t.tm_hour < send_time:
        print('2')
        wtimec = ((60 * 60) * ((send_time - 1) - t.tm_hour)) + (
            (60) * (59 - t.tm_min)) + (60 - t.tm_sec)
        #print(str(wtime))
        await asyncio.sleep(wtimec)
        print('sending cheadle...')
        await cheadlewotd()
    elif t.tm_hour >= send_time:
        print('3')
        wtime1 = ((60 * 60) *
                  (23 - t.tm_hour)) + ((60) *
                                       (59 - t.tm_min)) + (60 - t.tm_sec)
        wtime2 = send_time * 60 * 60
        wtimec = wtime1 + wtime2
        await asyncio.sleep(wtimec)
        print('sending cheadle...')
        await cheadlewotd()
    await asyncio.sleep(240)


@timer_shit_fuck.before_loop
async def before_timer_shit_fuck():
    await client.wait_until_ready()
    await asyncio.sleep(1)


#@jahtimer.before_loop
#async def before_timer_jahtimer():
#await client.wait_until_ready()
#await asyncio.sleep(1)

#----------------------------------------------------------------------------------------
#------------------------------------$joinvoice------------------------------------------
#----------------------------------------------------------------------------------------

#true_n_general = 802684938381557840  #nme
#testing_id = 815405498412171294  #testing
#doangus = 817632403228196874  #doangus

#vc_id_list = [doangus, true_n_general] #doangus then general
#vc_id_list = [testing_id]

songlistwvol = joinboice.songlistwvol
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
    print('playing ' + songlist[index])
    #songindex = random.randint(0, len(songlist) - 1)
    #songindex = 0
    song = songlist[index]
    audio = discord.FFmpegPCMAudio(source="songs/" + song + ".mp3")
    source = discord.PCMVolumeTransformer(audio)
    source.volume = songlistwvol[song]
    vc.play(source)


@client.event
async def join_song_com(channel_id, index):
    thing = True
    try:
        float(index)
    except ValueError:
        thing = False
    if thing == False:
        songindex = random.randint(0, len(songlist) - 1)
    elif int(index) in range(0, len(songlist) - 1) == False:
        songindex = random.randint(0, len(songlist) - 1)
    else:
        songindex = int(index)
    #songindex = 25
    channel = client.get_channel(channel_id)
    await join(channel)
    await asyncio.sleep(0.5)
    await playsong(songindex)
    while vc.is_playing():
        await asyncio.sleep(1)
    await leave(channel)


timer_shit_fuck.start()  #this sucks
#fuck repl.it
#jahtimer.start()

keep_alive.keep_alive()

client.run(os.getenv('TOKEN'))
