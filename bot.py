import discord
from discord.ext import commands
from asyncio import *
import random
import time


class CONFIG:
    PREFIX = '-'



Client = commands.Bot(command_prefix=CONFIG.PREFIX)

voice_object = None


database = {}

async def MyLoop():
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101731518722118)
    colors = [0x00FF00, 0xFF0000, 0x0000FF, 0x00CECE]
    titles = ["❤", "✨", "🌟", "⚡"]
    my_embed = discord.Embed(
        title=random.choice(titles)+"بات انلاین شد",
        description="DARk!",
        colour=random.choice(colors)
    )
    my_embed.set_footer(text='Alt+F4#6685')
    my_embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/954421019806941247/954421757958320148/images_1.jpeg')
    await channel.send(embed=my_embed)
  





@Client.event
async def on_ready():
    await Client.change_presence(status=discord.Status.idle, activity=discord.Streaming(name='twitch', url='https://twitch.tv/twitch'))
    print('-_________online________-     ')
    print('            AA              ll  tttttttttttttt           ffffffffff             44         ')
    print('          AA  AA            ll        tt                 ff                   4444         ')
    print('         AA    AA           ll        tt                 ff                 444444         ')
    print('        AA      AA          ll        tt                 ff               444   44         ')
    print('       AA        AA         ll        tt                 ffffffffff     444     44         ')
    print('      AA          AA        ll        tt                 ff           444       44         ')
    print('     AAAAAAAAAAAAAAAA       ll        tt                 ff         444         44         ')
    print('    AA              AA      ll        tt         ++      ff       444           44         ')
    print('   AA                AA     ll        tt         ++      ff     $$$$$$$$$$$$$$$$$$$$$      ')
    print('  AA                  AA    ll        tt   +++++++++++++ ff                     44         ')
    print(' AA                    AA   ll        tt         ++      ff                     44         ')
    print('AA                      AA  ll        tt         ++      ff                     44         ')
    print('___________________________________________________________________________________________')



    await Client.loop.create_task(MyLoop())


def CheckUser(userid):
    userid = str(userid)
    if(userid not in database):
        database[userid] = {}

@Client.command()
async def author(ctx):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-author"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)
    mention = ctx.author.mention
    avatar = ctx.author.avatar_url
    userid = ctx.author.id
    await ctx.send(''+str(userid))
    await ctx.send(''+str(avatar))
    await ctx.send('salam'+str(mention))





@Client.command()
async def set(ctx, *, values):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-set"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)
    values = values.split()

    password = values[0]
    name = values[1]


    await ctx.send('Password : '+password+'\n'+
    'Name : '+name)

    await ctx.send('values Count : '+str(len(values)))



@Client.command()
async def status(ctx, status_type):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-status"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)
    if(status_type == 'idle'):
        # idle vaz
        await Client.change_presence(status=discord.Status.idle)
        await ctx.send(">>> "+'dark be idle taqir peyda kard')
    elif(status_type == 'dnd'):
        # do not disturd (dnd) vaz
        await ctx.send(">>> "+'dark be dnd taqir peyda kard')
        await Client.change_presence(status=discord.Status.dnd)
    else:
        # online vaz
        await ctx.send(">>> "+'dark be online taqir peyda kard')
        await Client.change_presence(status=discord.Status.online)

@Client.command()
async def setactivity(ctx, activity_type, *,activity_text):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-setactivity"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)

    if(activity_type == 'playing'):
        await Client.change_presence(activity=discord.Game(name=activity_text))
        await ctx.send(">>> "+'dark avaz shod.')


    elif(activity_type == 'streaming'):
        await Client.change_presence(activity=discord.Streaming(name=activity_text, url='https://twitch.tv/twitch'))
        await ctx.send(">>> "+'dark avaz shod.')


    elif(activity_type == 'watching'):
        await Client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity_text))
        await ctx.send(">>> "+'dark avaz shod.')


    elif(activity_type == 'listening'):
        await Client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_text))
        await ctx.send(">>> "+'dark avaz shod.')

    else:
        # unrnown command
        await ctx.send('activity na moshakhas ('+activity_type+')')


@Client.command()
async def s(ctx):
    colors = [0x00FF00, 0xFF0000, 0x0000FF, 0x00CECE]
    titles = ["دو سال دیگه", "75", "60", "35"]
    my_embed = discord.Embed(
        title=random.choice(titles)+"embed titel",
        description="embed text",
        colour=random.choice(colors)
    )
    my_embed.set_footer(text='footer text')
    my_embed.set_thumbnail(url='https://th.bing.com/th/id/R.da42c05924341904aa6d43b6e6bf233d?rik=digxOBHvZvee%2bQ&riu=http%3a%2f%2firandeganib.ir%2fwp-content%2fuploads%2f2020%2f07%2f%D8%B9%DA%A9%D8%B3-%D8%B6%D8%B1%D8%A8%D8%A7%D9%86-%D9%82%D9%84%D8%A8-16-768x512.jpg&ehk=cWPn2FyksXnIReoOYP75O6y1I7%2f7OsMG5GvoL3iIMOM%3d&risl=&pid=ImgRaw&r=0')
    my_embed.set_image(url='https://th.bing.com/th/id/R.da42c05924341904aa6d43b6e6bf233d?rik=digxOBHvZvee%2bQ&riu=http%3a%2f%2firandeganib.ir%2fwp-content%2fuploads%2f2020%2f07%2f%D8%B9%DA%A9%D8%B3-%D8%B6%D8%B1%D8%A8%D8%A7%D9%86-%D9%82%D9%84%D8%A8-16-768x512.jpg&ehk=cWPn2FyksXnIReoOYP75O6y1I7%2f7OsMG5GvoL3iIMOM%3d&risl=&pid=ImgRaw&r=0')
    await ctx.send(embed=my_embed)

@Client.command(aliases=['clear', 'pak'])
@commands.has_permissions(administrator=True)

async def pak_sazi(ctx, count='10'):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-pak"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)
    count = int(count)
    await ctx.channel.purge(limit=count+1)
    await ctx.send(">>> "+str(count)+'Massage pak shod')



@Client.command()
async def add(ctx, datakey, *, datavalue):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-add"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)
    CheckUser(ctx.message.author.id)
    global database
    database[str(ctx.message.author.id)][str(datakey)] = str(datavalue)
    await ctx.send(str(datakey)+' was savad redis database')

@Client.command()
async def get(ctx, datakey):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-get"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)
    CheckUser(ctx.message.author.id)
    if( datakey in database[str(ctx.message.author.id)] ):
        await ctx.send(str(datakey)+' : '+str(database[str(ctx.message.author.id)][str(datakey)]))
    else:
        await ctx.send(str(datakey)+' not found in redis database')


@Client.command()
async def remove(ctx, datakey):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-remove"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)
    CheckUser(ctx.message.author.id)
    global database
    if( datakey in database):
        del database[str(ctx.message.author.id)][str(datakey)]
        await ctx.send(str(datakey)+' was removed from databaes')
    else:
        await ctx.send(str(datakey)+' not found in redis databaes')

@Client.command(aliases=['p1', '.play1'])
async def join(ctx):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    global voice_object
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention

    my_channel = ctx.message.author.voice.channel
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(my_channel)
    else:
    
        voice_object = await my_channel.connect()
        my_embed = discord.Embed(
            title="M بیزینس M",
            description="سپهر خلسه"+'\n'+str(mention),
            colour=0x00CECE
        )
        my_embed.set_footer(text='موزیک')
        my_embed.set_thumbnail(url=avatar)
        my_embed.set_image(url='https://th.bing.com/th/id/R.3539a4db2820ef87d4039121780d26dd?rik=uyYj5cRkDLOWlw&pid=ImgRaw&r=0')
        await ctx.send(embed=my_embed)
        await ctx.send(">>> "+'جوین ویس شد درحال پخش')
        await channel.send(">>> "+'-p1'+'\n'+'از این کامنت استفاده شد'+'\n'+str(mention))
        voice_object.play(discord.FFmpegPCMAudio('1.mp3'))

    



@Client.command(aliases=['p2', '.play2'])
async def join2(ctx):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    global voice_object
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention

    my_channel = ctx.message.author.voice.channel
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(my_channel)
    else:
    
        voice_object = await my_channel.connect()
        my_embed = discord.Embed(
            title="M الو بابی M",
            description="سپهر خلسه"+'\n'+str(mention),
            colour=0x00CECE
        )
        my_embed.set_footer(text='موزیک')
        my_embed.set_thumbnail(url=avatar)
        my_embed.set_image(url='https://th.bing.com/th/id/R.3539a4db2820ef87d4039121780d26dd?rik=uyYj5cRkDLOWlw&pid=ImgRaw&r=0')
        await ctx.send(embed=my_embed)
        await ctx.send(">>> "+'جوین ویس شد درحال پخش')
        await channel.send(">>> "+'-p2'+'\n'+'از این کامنت استفاده شد'+'\n'+str(mention))
        voice_object.play(discord.FFmpegPCMAudio('2.mp3'))

    


@Client.command(aliases=['p3', '.play3'])
async def join3(ctx):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    global voice_object
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention

    my_channel = ctx.message.author.voice.channel
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(my_channel)
    else:
    
        voice_object = await my_channel.connect()
        my_embed = discord.Embed(
            title="M  115   M",
            description="سپهر خلسه"+'\n'+str(mention),
            colour=0x00CECE
        )
        my_embed.set_footer(text='موزیک')
        my_embed.set_thumbnail(url=avatar)
        my_embed.set_image(url='https://th.bing.com/th/id/R.3539a4db2820ef87d4039121780d26dd?rik=uyYj5cRkDLOWlw&pid=ImgRaw&r=0')
        await ctx.send(embed=my_embed)
        await ctx.send(">>> "+'جوین ویس شد درحال پخش')
        await channel.send(">>> "+'-p3'+'\n'+'از این کامنت استفاده شد'+'\n'+str(mention))
        voice_object.play(discord.FFmpegPCMAudio('3.mp3'))






@Client.command(aliases=['dis', 'stop'])

async def disconnect(ctx):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-dis"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)
    voice = discord.utils.get(Client.voice_clients, guild=ctx.guild)
    await voice.disconnect()
    await ctx.send(">>> "+'ویس را ترک کرد')
    






@Client.command()
async def spam(ctx):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-spam"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)
    while True:
        await ctx.send(">>> "+'spam HA HA HA HA')
        time.sleep(0.2)
        async def stop(cxs):
            stop


@Client.command(aliases=['senmordan', 'sen'])
async def ss(ctx):
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    colors = [0x00FF00, 0xFF0000, 0x0000FF, 0x00CECE]
    titles = ["دو سال دیگه", "در سن 75", "در سن 60", "در سن 35", "در سن 44", "در سن 99",]
    my_embed = discord.Embed(
        title=random.choice(titles)+"   میمیرید  ",
        description="اگه دلیل مرگ میخای👇",
        colour=random.choice(colors)
    )
    my_embed.set_thumbnail(url=avatar)
    await ctx.send(embed=my_embed)
    await ctx.send(">>> "+'-dalilmordan')

@Client.command(aliases=['dalil mordan', 'dalilmordan'])
async def sss(ctx):
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    colors = [0x00FF00, 0xFF0000, 0x0000FF, 0x00CECE]
    titles = ["جق زدن بیش از اندازه", "فوش دادن به زنت", "از اسکلی", "در جماعت زیاد کس شعر میگفتی", "ریدن", "زیر شدن توست ال اف چهار", "کون دادن"]
    my_embed = discord.Embed(
        title=random.choice(titles)+"  دلیل مردن  ",
        description="حلا فهمیدی"+str(mention),
        colour=random.choice(colors)
    )
    my_embed.set_thumbnail(url=avatar)

    await ctx.send(embed=my_embed)

@Client.command(aliases=['dark'])
async def dark_help(ctx):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954101584621633636)
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention
    my_embed = discord.Embed(
        title="-dark"+'\n'+"از این کامنت استفاده شد",
        description="id:  "+'\n'+str(mention),
    )
    my_embed.set_thumbnail(url=avatar)
    
    await channel.send(embed=my_embed)
    await ctx.send(">>> "+'حتما قبل کامنت از این | - | استفاده کنید ')
    await ctx.send(">>> "+'-pak (تعداد ) | برا پاک سازی پیام استفاده میشه')
    await ctx.send(">>> "+'-send  | برای ارسال پیام به سارند بات | باید پیام شما بدون خط فاصله باشد')
    await ctx.send(">>> "+'_______________________________________________________________________________')
    await ctx.send(">>> "+'-senmordan   | تاریخ مرگ شما رو حدث میزند')
    await ctx.send(">>> "+'-dalilmordan | دلیل مردن شما رو حدث میزنه')

@Client.command()
async def send(ctx, values):
    server = Client.get_guild(953613216850784256)
    channel = server.get_channel(954133583155568651)
    values = values.split()
    avatar = ctx.author.avatar_url
    mention = ctx.author.mention

    text = values[0]

    my_embed = discord.Embed(
        title='messege:'+text,
        description=(mention),
        colour=0xFF0000
    )
    my_embed.set_thumbnail(url=avatar)

    await channel.send(embed=my_embed)
    await ctx.send(">>> "+'پیام ارسال شد')


    
    




@Client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(">>> "+'کامنت اشتباه است')



    
Client.run('OTUyNTAwNjI5MTQwNTY2MDY2.Yi27Vg.3xa8jGWU4edPsOyQp5fMnhTQOvI')
