import discord
import random
import asyncio
from enum import Enum

class GameState(Enum):
    idle = 0
    play = 1

game_state = GameState.idle
ready_user_list = []

# 참여
async def Ready(self, message):
    if game_state == GameState.idle and message.author not in ready_user_list:
        ready_user_list.append(message.author)
        await message.channel.send(message.author.name + " 참여되었습니다.")

# 참여 취소
async def Unready(self, message):
    if game_state == GameState.idle and message.author in ready_user_list:
        ready_user_list.remove(message.author)
        await message.channel.send(message.author.name + " 참여가 취소되었습니다.")

# 참여 리스트
async def ShowReadyList(self, message):
    if game_state == GameState.idle:
        embed = discord.Embed(
            title = '현재 369를 준비중인 유저 목록',
            color = 0x00ff50
        )
        
        i = 0
        for member in ready_user_list:
            i = i + 1
            embed.add_field(name = '{0}.'.format(i) ,value = member.name , inline = False)
        await message.channel.send(embed = embed)

# 본게임
async def Start(self, message):
    global game_state
    # 권한 및 상태 테스트
    if game_state != GameState.idle or message.author not in ready_user_list:
        return
    # 플레이어 리스트를 받아오고 참여 리스트 초기화 및 참여 불가 설정
    player_list = ready_user_list[:]
    ready_user_list.clear()
    game_state = GameState.play
    game_channel = message.channel
    
    await message.channel.send("369 게임을 시작하겠습니다.")
    
    # 순서를 만들어보자
    random.shuffle(player_list)
    send_buffer = ""
    for i in player_list:
        send_buffer += " -> "+ str(i) 
    await message.channel.send("순서는 "+send_buffer[3:]+" 입니다")
        
    # 플레이어 입력받는거
    current = 1
    timeout = 15.0
    while True:
        current_player = player_list[(current - 1) % len(player_list)]

        # 제한시간내에 입력 받기
        try:
            msg = await self.wait_for('message', timeout=timeout, check= lambda message: (not message.author.bot) and message.channel == game_channel and message.author in player_list) # message.author == current_player and 
        except asyncio.TimeoutError:
            await message.channel.send(current_player.name + "이/가 제 시간에 대답하지 않았습니다.")
            break

        # 순서 체크
        if current_player != msg.author:
            await message.channel.send(msg.author.name + " Boom!") 
            break

        # 대답 체크
        temp_str_current = str(current)
        if temp_str_current.find('3') == -1 and temp_str_current.find('6') == -1 and temp_str_current.find('9') == -1:
            # 현재 숫자가 369를 포함하지 않을때
            if not (msg.content.isdigit() and msg.content.find('3') == -1 and msg.content.find('6') == -1 and msg.content.find('9') == -1):
                await message.channel.send(msg.author.name + " Boom!")
                break
        else:
            # 포함 할때
            if msg.content not in ["짝", "작", "쨕", "쟉", "쨖", "쟊", "짞", "쟊"]:
                await message.channel.send(msg.author.name + " Boom!")
                break

        # 정답, 다음 턴으로
        current += 1
        timeout = max(timeout - 2, 2)
        await message.channel.send("다음 턴입니다. {0}초 이내에 답하십시오.".format(timeout))
        
    # 게임 초기화
    game_state = GameState.idle