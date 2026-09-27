import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# 환경 변수 로드 (디스호스트의 환경변수 설정값을 읽어옵니다)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# 인텐트 설정 (봇이 유저들의 메시지를 읽을 수 있도록 허용)
intents = discord.Intents.default()
intents.message_content = True

# 봇 접두사 설정 (채팅창에 !안녕, !핑 처럼 접두사 뒤에 명령어를 입력합니다)
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    # 봇이 성공적으로 켜지면 디스호스트 콘솔창에 아래 문구가 뜹니다.
    print("=" * 40)
    print(f"봇이 성공적으로 로그인했습니다: {bot.user}")
    print("현재 24시간 호스팅 서버에서 작동 중입니다.")
    print("=" * 40)

@bot.command()
async def 안녕(ctx):
    # !안녕 이라고 치면 작동하는 명령어
    await ctx.send(f"안녕하세요 {ctx.author.mention}님! 24시간 호스팅으로 구동 중인 봇입니다. 🤖")

@bot.command()
async def 핑(ctx):
    # !핑 이라고 치면 작동하는 명령어 (봇의 반응 속도 확인)
    await ctx.send(f"퐁! 🏓 ({round(bot.latency * 1000)}ms)")

# 봇 실행
if TOKEN:
    bot.run(TOKEN)
else:
    print("오류: 디스호스트 환경변수 설정에서 DISCORD_TOKEN을 찾을 수 없습니다. 다시 확인해 주세요.")
