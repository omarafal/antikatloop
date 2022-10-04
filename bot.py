import discord, asyncio, random
from discord.ext import commands

# TOKEN, GUILD ID, CHANNEL ID AND USER ID HAVE BEEN STORED IN EXTERNAL FILES FOR SECURITY AND PRIVACY REASONS :)

# get token from text file
f1 = open("token.txt", "r")
token = f1.readline()
f1.close()

# get server ID from text file
f2 = open("guild_id.txt", "r")
guild_id = int(f2.readline())
f2.close()

# get user ID from text file
f3 = open("user_id.txt", "r")
user_id = int(f3.readline())
f3.close()

# get channel ID from text file
f4 = open("user_id.txt", "r")
channel_id = int(f4.readline())
f4.close()

client = commands.Bot(intents=discord.Intents.all(), command_prefix="--")

@client.event
async def on_ready():
    print("Bot is on")


@client.command(aliases=["naughty"])
@commands.cooldown(1, 60*3, commands.BucketType.guild)
async def noty(ctx):
    """
    Function takes in context and grabs the user ID along with the channel ID to move the user to said channel
    Also for fun: send a random string from three in chat whenever this command is used
    """
    member = client.get_guild(guild_id).get_member(user_id)

    # check if user is in a voice channel
    if(member.voice == None):
        await ctx.send("Hoa m4 f channel asln")
        return None

    channel = client.get_channel(channel_id)
    await member.move_to(channel)
    num = random.randint(0, 2)

    if num == 0:
        await ctx.send(f"Are we being naughty again {member.name}? ")
    elif num == 1:
        await ctx.send(f"Ke5a ba2a")
    elif num == 2:
        await ctx.send(f"Noty noty {member.name}")

@client.command()
async def slap(ctx):
    """
    Function that takes in context that grabs the user ID and mutes him for seven seconds
    """

    member = client.get_guild(guild_id).get_member(user_id)

    # check if user is in a voice channel
    if member.voice == None:
        await ctx.send("Katloop is hiding from voicechat")
        return None

    await member.edit(mute=True)
    await ctx.send("The slap was so hard he is literally speachless")
    await asyncio.sleep(7)
    await member.edit(mute=False)

client.run(token=token)