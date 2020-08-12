import discord;
import random;
import re;
import time;
import sqlite3;

# regexs
RE_POSITIVE_INTEGER = re.compile(r"^\d*[1-9]$")
RE_START_CAT = re.compile(r'(^고[양냥]이)|(냥$)')
RE_POTATO = re.compile(r'((wedge)|(ㅇㅈ)|(외질)|(웨지)|(왜지)|(우ㅐ지)|(오ㅔ지)|(외지)|(왜쥐)|(웨쥐)|(웨쥐)|(오ㅔ쥐)|(외쥐))$')
RE_SQUIRREL = re.compile(r'^.*(다)[^0-9a-zA-Zㄱ-ㅎㅏ-ㅣ가-닣댜-힣]*\s*($|\n)')
RE_YOGURT = re.compile(r'^.*(요)[^0-9a-zA-Zㄱ-ㅎㅏ-ㅣ가-닣댜-힣]*\s*($|\n)')
RE_RAVEN = re.compile(r'^.*(가|까|깎|꺄|깍|꺅|꺆|g+a|ka|KA|GA)[^0-9a-zA-Zㄱ-ㅎㅏ-ㅣ가-닣댜-힣]*\s*($|\n)')
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

# channels
AVAILABLE_CHANNELS = ['team-강찬영', 'general']

# DB
DB_INSERT_SQL = 'INSERT INTO user(id) VALUES(?)'
DB_SELECT_ALL_SQL = 'SELECT * FROM user'
DB_SELECT_SQL = 'SELECT * FROM user WHERE id=?'
DB_DELETE_SQL = 'DELETE FROM user WHERE id=?'

DB = sqlite3.connect("DB/User.db")
cur = DB.execute('CREATE TABLE IF NOT EXISTS user (id TEXT PRIMARY KEY)')

class MyClient(discord.Client):
    async def on_message(self, message):
        ### Validation
        if message.author == self.user: # 자기 메세지 반응 안함
            return
        
        if len(AVAILABLE_CHANNELS) > 0 and message.channel.name not in AVAILABLE_CHANNELS: # 채널 검증
            return

        await self.on_potato(message)
        await self.on_cat(message)
        await self.on_squirrel(message)
        await self.on_yogurt(message)
        await self.on_raven(message)
        await self.on_food(message)
        await self.on_rupy_sad(message)
        
        ### Feature
        if message.content.startswith('['):
            message.content = message.content[1:]
            await self.on_command(message)
            return
    
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

    async def on_command(self, message):
        if message.content == '모든멤버': # JARAM ONLINE의 모든 사람들을 출력함
            send_buffer = ""
            count = 0
            for a in self.get_all_members():
                send_buffer += str(a) + "\n"
                count+=1
            embed = discord.Embed(title="모든 멤버", description=send_buffer, color=0x00ff50)
            embed.set_author(name="JARAM MEMBERS")
            embed.set_footer(text = "총 멤버 수는 " + str(count) + "입니다.")
            embed.set_thumbnail(url="https://cafeskthumb-phinf.pstatic.net/MjAxOTAzMTdfMTAw/MDAxNTUyODMwMzc5ODg0.ICcTo_Y5cpYlHj44AZQiPNGbtMAsMMuCdGxrnGDBn0Ug.RnscC7n3LcEZE4iKAZ9t5FvMpR1Brsct4yibkaMYuQQg.PNG.whsqkaak/ICT-Jaram.png?type=w1080")
            await message.channel.send(embed=embed)
            return
            
        if message.content[0:3] == '사다리':
            right_message = message.content.split()[1:]
            membercount = len(right_message)
            send_buffer = ""
            map_height = int(membercount*1.5)
            map_weight = membercount * 2 - 1
            map = [['　' for col in range(map_weight)] for row in range(map_height)]
            
            
            for i in range(0, map_weight, 2):
                for j in range(0, map_height):
                    map[j][i] = '│'

            for i in range(0, map_weight-2, 2):
                for j in range(0, map_height):
                    if map[j][i - 1] != '─' and random.randrange(100) > 66:
                        map[j][i] = '├'
                        map[j][i + 1] = '─'
                        map[j][i + 2] = '┤' 
                    else:
                        map[j][i+1] ='　'

            #2차원배열->사다리str
            for i in range(0, map_height):
                for j in range(0, map_weight):
                    send_buffer += map[i][j]
                send_buffer += '\n'
            await message.channel.send('     '.join(right_message))
            # 여기서 보내고 메세지를 msg에 저장되어있음
            msg = await message.channel.send(send_buffer)
            #time.sleep(0.5)
            # goal list(1이 당첨) 
            goal = ["0"] * membercount  
            goal[random.randint(0, membercount-1)] = "1"
            await message.channel.send("　" + '      '.join(goal)) #  
            # 인원출력
            
            # right_message에 인원목록 들어있음 list형식
            pos = 0
            for i in range(0,map_weight,2):
                player = str(right_message[int(i/2)])
                for j in range(map_height):
                    # 1. 현재 위치
                    pos = i + j * membercount * 2
                    # 2. 출력하기
                    await msg.edit(content = send_buffer[:pos] + '●' + send_buffer[pos+1:])
                    # 3. 슬립
                    time.sleep(0.5)
                    # 4. 좌우 체크 및 이동
                    mov_dir = 0
                    # 4.1 좌측 체크
                    if send_buffer[pos] == '┤': 
                        mov_dir = -1
                    # 4.2 우측 체크
                    if send_buffer[pos] == '├':
                        mov_dir = 1
                    # 4.3 이동
                    if mov_dir != 0:
                        for k in range(2):
                            i += mov_dir
                            pos = i + j * membercount * 2
                            await msg.edit(content = send_buffer[:pos] + '●' + send_buffer[pos+1:])
                            time.sleep(0.5)
                # 5. 한 사람씩 당첨
                if goal[int(i/2)] == '1':
                    await message.channel.send(player + " 당첨")
            await message.channel.send("사다리 종료")
            return


        if message.content.isdigit():
            send_buffer = "```" + str(int(message.content)**2)+ "```"
            await message.channel.send(send_buffer)
            return


        if message.content == '멤버':
            send_buffer = "" # 캐싱
            count=0

            cur.execute(DB_SELECT_ALL_SQL)
            rows = cur.fetchall()
            for i in rows:
                count +=1
                send_buffer += "Potato addict" + str(count) + " : " + str(self.get_user(int(i[0]))) + "\n"
            embed = discord.Embed(title="Potato addicts", description=send_buffer, color=0x00ff50)
            embed.set_author(name="Those who love potato wedges")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/723859914090479656/742914673137025105/jaram_photo.jpg")
            await message.channel.send(embed = embed) # 보내기(느림)
            return


        if message.content.startswith('멤버추가'): # .startswith : !멤버추가 로 시작하는 message는 모두 받음
            realtemp = message.content.split(" ")
            realtemp2 = realtemp[1]
            DB.execute(DB_INSERT_SQL, (int(realtemp2),))
            DB.commit()
            await message.channel.send('멤버 추가 완료')
            return
            
        if message.content.startswith('멤버제거'):
            realtemp = message.content.split(" ")
            realtemp2 = realtemp[1]
            DB.execute(DB_DELETE_SQL, (int(realtemp2),))
            DB.commit()
            await message.channel.send('멤버 제거 완료')
            return


        if message.content.startswith('뽑기'): # 뽑기 작동해여
            i=0
            temp = message.content.split(" ")
            

            if not RE_POSITIVE_INTEGER.match(temp[1]): # 뽑기 인원 validation
                await message.channel.send('뽑힌 인원은 1 이상의 정수가 되어야합니다.')
                return
                
            await message.channel.send('쿵짝짝 뽑기를 진행하겠습니다. 쿵짝짝')

            WinningNum = int(temp[1])
            nameList = temp[2:]
            indexList = []
            
            while i<3:
                await message.channel.send("...\n")
                time.sleep(1)
                i+=1
                
            samplelist = random.sample(nameList,WinningNum)
            tempstr2 = ""
            count = 0
            for i in samplelist:
                count += 1
                tempstr2 += "%15s" % str(count) + " : 당첨인원 : " + i + "\n"
            embed = discord.Embed(title="당첨!", description=tempstr2, color=0x00ff50)
            embed.set_author(name="뽑기")
            await message.channel.send(embed = embed) # 보내기(느림)
            return
        
        #
        


        if message.content.startswith("명령어"):
            embed = discord.Embed(
                title = 'Command List',
                color = 0x00ff50
            )
            embed.add_field(name = '[명령어',value = ': 명령어는 명령어에요^^7' ,inline = False)
            embed.add_field(name = '[모든멤버' , value = ': 서버의 모든 사람을 출력합니다.', inline = False)
            embed.add_field(name = '[멤버',value = ': 감자(?)를 좋아하는 사람들을 출력합니다.' ,inline = False)
            embed.add_field(name = '[멤버추가', value = ': 감자를 좋아하는 사람을 추가합니다.' ,inline = True)
            embed.add_field(name = '[멤버제거', value = ': 감자 멤버에서 추방합니다.' ,inline = True)
            embed.add_field(name = '[뽑기', value = ': 사용법 : [뽑기 인원수 이름 이름 이름 ...' ,inline = False)
            embed.add_field(name = '[사다리', value = ': 사용법 : [사다리 이름 이름 사다리를 출력합니다.',inline = False)
            embed.add_field(name = '숫자', value = ': 숫자를 입력하시면, 제곱을 해줍니다.',inline = False)
            embed.add_field(name = '고양이',value = ': 고양이!!!!!!!!!!!!!!!!!!!!!!!' ,inline = False)
            embed.add_field(name = '람쥐썬더', value = '채팅 메시지 끝을 \'다\'로 끝내보세요. :D',inline = False)
            embed.add_field(name = '구르트아줌마요구르트주세요', value = '채팅 메시지 끝을 \'요\'로 끝내보세요. :D',inline = False)
            embed.add_field(name = '악까악', value = '채팅 메시지 끝을 \'까\'로 끝내보세요. :D',inline = False)
            embed.add_field(name = '울지마 루피가 위로해줄게', value = '우시면 루피가 같이 울어줍니다. :D',inline = False)
            embed.set_thumbnail(url="https://cafeskthumb-phinf.pstatic.net/MjAxOTAzMTdfMTAw/MDAxNTUyODMwMzc5ODg0.ICcTo_Y5cpYlHj44AZQiPNGbtMAsMMuCdGxrnGDBn0Ug.RnscC7n3LcEZE4iKAZ9t5FvMpR1Brsct4yibkaMYuQQg.PNG.whsqkaak/ICT-Jaram.png?type=w1080")
            await message.channel.send(embed = embed)
            return



# 실행 순서 (터미널)
# 1. 저장 ( ☆ ctrl + s )
# 2. 실행 (터미널 누르고 ctrl + c 누른 뒤 -> python main.py)

# self.
client = MyClient() # 생성
client.run('NzQyNTY5MzM4MTk5OTk4NDc0.XzIBlg.DbAHj1SYzSElj9mKpx-nTQVkh_c') # 토큰을 이용하여 활성화?