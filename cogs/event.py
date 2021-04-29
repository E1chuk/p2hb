import discord
from discord.ext import commands, menus
from datetime import datetime, timedelta
from helpers.pagination import AsyncListPageSource
from helpers import checks, helper
import asyncio
import math
from data import models

import random


class Event(commands.Cog):
    """Events"""

    def __init__(self, bot):
        self.bot = bot

    @checks.has_started()
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.command()
    async def eventcollect(self, ctx):
        """Bot Verification Event"""
        member = await self.bot.mongo.fetch_member_info(ctx.author)
        if member.has_collected:
            return await ctx.send("You've already collected the bonus!")
        
        await self.bot.mongo.update_member(ctx.author, {"$inc": {"balance": 500}, "$set": {"has_collected": True}})
        embed = discord.Embed(title = "Here, have some free money", description="You have been given 500 tokens. If you would like to add the bot to your own server, use https://invite.p2hb.me/")
        
        await ctx.send(f"> <@!{ctx.author.id}>", embed=embed)

def setup(bot):
    bot.add_cog(Event(bot))