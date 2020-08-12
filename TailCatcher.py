import discord
import re
import random

# regexs
RE_START_CAT = re.compile(r'(^고[양냥]이)|(냥$)')
RE_POTATO = re.compile(r'((wedge)|(ㅇㅈ)|(외질)|(웨지)|(왜지)|(우ㅐ지)|(오ㅔ지)|(외지)|(왜쥐)|(웨쥐)|(웨쥐)|(오ㅔ쥐)|(외쥐))$')
RE_SQUIRREL = re.compile(r'^.*(다)[^0-9a-zA-Zㄱ-ㅎㅏ-ㅣ가-닣댜-힣]*\s*($|\n)')
RE_YOGURT = re.compile(r'^.*(요)[^0-9a-zA-Zㄱ-ㅎㅏ-ㅣ가-닣댜-힣]*\s*($|\n)')
RE_RAVEN = re.compile(r'^.*((가|까|깎|꺄|깍|꺅|꺆|g+a|ka|KA|GA)[^0-9a-zA-Zㄱ-ㅎㅏ-ㅣ가-닣댜-힣]*\s*)($|\n)')
RE_FOOD = re.compile(r'^.*((배고파)|(뭐\s*먹지)|(ㅂㄱㅍ))[^0-9a-zA-Zㄱ-ㅎㅏ-ㅣ가-닣댜-힣]*\s*($|\n)')
RE_SAD = re.compile(r'^.*((ㅜ)|(ㅠ)|(T))+\s*($|\n)')

# files
POTATO_FILES = ['Files/potato.jpg']
SQUIRREL_FILES = ['Files/Squirrel1.jpg', 'Files/Squirrel3.jpg', 'Files/Squirrel4.jpg', 'Files/Squirrel5.jpg']
YOGURT_FILES = ['Files/yogurt.jpg']
RAVEN_FILES = ['Files/raven.jpg', 'Files/raven2.jpg']
FOOD_FILES = ['Files/dbe.jpg']
SAD_FILES = ['Files/rupy_sad.jpg']

# string list
FOOD_LIST = ["햄버거", "치킨", "찜닭", "떡볶이", "바나나", "물먹어 돼지야"]

async def Catch(self, message):
    await on_potato(self, message)
    await on_cat(self, message)
    await on_squirrel(self, message)
    await on_yogurt(self, message)
    await on_raven(self, message)
    await on_food(self, message)
    await on_rupy_sad(self, message)

async def on_potato(self, message):
    if RE_POTATO.match(message.content):
        #await message.channel.send("여러분의 성원에 힘입어 감자가 모두 동이 났습니다. 감사합니다.")
        #return
        if random.randrange(100) < 85:
            await message.channel.send("감자")
        else:
            await message.channel.send(file=discord.File(random.choice(POTATO_FILES)))
            
async def on_cat(self, message):
    if RE_START_CAT.match(message.content):
        embed = discord.Embed(title = 'What The Cat?', descripiton = '왈왈', color = 0x00ff50)
        urlBase = 'https://loremflickr.com/320/240?lock='
        plusnum = random.randrange(1,20000)
        url2 = urlBase + str(plusnum)
        embed.set_image(url = url2)
        await message.channel.send(embed=embed)

async def on_squirrel(self, message):
    if RE_SQUIRREL.match(message.content):
        if random.randrange(100) < 85:
            await message.channel.send(random.choice(["람쥐", "람쥐썬더"]))
        else:
            await message.channel.send(file=discord.File(random.choice(SQUIRREL_FILES)))

async def on_yogurt(self, message):
    if RE_YOGURT.match(message.content):
        if random.randrange(100) < 85:
            await message.channel.send(random.choice(["구르트", "플레"]))
        else:
            await message.channel.send(file=discord.File(random.choice(YOGURT_FILES)))

async def on_raven(self, message):
    if RE_RAVEN.match(message.content):
        if random.randrange(100) < 85: 
            await message.channel.send(random.choice(["마귀", "막까막", "악까악"]))
        else:
            await message.channel.send(file=discord.File(random.choice(RAVEN_FILES)))

async def on_food(self, message):
    if RE_FOOD.match(message.content):
        if random.randrange(100) < 85: 
            await message.channel.send(random.choice(FOOD_LIST))
        else:
            await message.channel.send(file=discord.File(random.choice(FOOD_FILES)))

async def on_rupy_sad(self, message):
    if RE_SAD.match(message.content):
        await message.channel.send(file=discord.File(random.choice(SAD_FILES)))