from fileinput import filename
import discord
from distutils.cmd import Command
from discord.ext import commands
import os,shutil
from google_images_download import google_images_download
import random


class image_cog(commands.Cog):
    def __init__(self, bot):
        
        self.bot = bot
        self.download_folder = 'downloads'
        
        self.keywords = 'cool'
        
        self.response = google_images_download.googleimagesdownload()
        self.arguments = {
            "keywords" : self.keywords,
            "limit" : 20,
            "size" : "medium",
            "no_directory" : True
        }
        
        self.image_names = []
        self.update_images()
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Online")
        
    def update_images(self):
        for filname in os.listdir(self.download_folder):
            self.image_names.append(os.path.join(self.download_folder, filename))
    def clear_folder(self):
        for filename in os.listdir(self.download_folder):
            file_path = os.path.join(self.download_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print("Failed to delete %s. Reason %s" %(file_path,e))
      
    
    @commands.command(name="search", help="searches for a message on google")
    async def search(self, ctx, *args):
        
        self.clear_folder()
        # ctx.send('searching...')
        
        self.arguments['keywords'] = " ".join(args)
        self.response.download(self.arguments)
        
        self.update_images()
        ctx.send("search complete")
    
    @commands.command(name = "pingg")
    async def pingg(self,ctx):
        await ctx.send("Pong")
        
    @commands.command(name = "clear")
    async def clear(self,ctx):
        self.clear_folder()
        await ctx.send("cleared")
        
    @commands.command()
    async def bring(self, ctx):
        img = self.image_names[random.randrange(0, len(self.image_names)-1)]
        await ctx.send('enjoy..!', file = discord.File(img))
   
async def setup(bot):
    await bot.add_cog(image_cog(bot))
