mport discord
import random
from discord.ext import commands
import praw

reddit = praw.Reddit(client_id="client_id",
                     client_secret="client_secret",
                     username="username",
                     password="password",
                     user_agent="pythonpraw")

token = open("token.txt","r").readline()

client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name="-help | Getting the best memes for you!"))
    print('Logged In!')
    print('------------')


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="Here are the commands!", colour=discord.Colour.gold())
    embed.add_field(name="-meme", value="sends a meme from the subreddit `r/memes`")
    embed.add_field(name="-meme `subreddit`", value="Sends a meme from a subreddit of your choice")
    await ctx.author.send(embed=embed)





@client.command()
async def meme(ctx, subred="memes"):
    subreddit = reddit.subreddit(subred)
    all_subs = []
    top = subreddit.top(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url
    comment = random_sub.num_comments
    like = random_sub.score
    embed = discord.Embed(title=name,
                          colour=discord.Colour.gold())

    embed.set_image(url=url)
    embed.set_footer(text=f"👍 {like} upvotes | 💬 {comment} comments")
    await ctx.send(embed=embed)



client.run(token)
