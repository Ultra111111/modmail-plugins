import asyncio
import copy

import dateutil
import discord
from discord.ext import commands


class Transfer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        @commands.has_roles('Supporter', 'Admin', 'Moderator', 'Owner')
        async def pm(self, ctx, args, message):
            
            channel = message.channel.id
            pmcategory = 860459735089020948

            await ctx.channel.edit(category=pmcategory)
            await message.channel.send(':white_check_mark: Success.')

        @commands.command()
        @commands.has_roles('Supporter', 'Admin', 'Moderator', 'Owner')
        async def app(self, ctx, args, message):

            channel = message.channel.id
            appcategory = 860513858459140106

            await ctx.channel.edit(category=appcategory)
            await message.channel.send(':white_check_mark: Success.')

        @commands.command()
        @commands.has_roles('Supporter', 'Admin', 'Moderator', 'Owner')
        async def prem(self, ctx, args, message):

            channel = message.channel.id
            premcategory = 860460179480379392

            await ctx.channel.edit(category=premcategory)
            await message.channel.send(':white_check_mark: Success.')

        @commands.command()
        @commands.has_roles('Supporter', 'Admin', 'Moderator', 'Owner')
        async def admin(self, ctx, args, message):

            channel = message.channel.id
            admincategory = 860535498328899624

            await ctx.channel.edit(category=admincategory)
            await message.channel.send(':white_check_mark: Success.')

        @commands.command()
        @commands.has_roles('Supporter', 'Admin', 'Moderator', 'Owner')
        async def others(self, ctx, args, message):

            channel = message.channel.id
            others = 860460677739315230

            await ctx.channel.edit(category=others)
            await message.channel.send(':white_check_mark: Success.')

def setup(bot):
    bot.add_cog(Transfer(bot))
