# Stubborn Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Stubborn1223




import os, sys, asyncio, time
from config import *
from database import *
from .utils import get_readable_time
from translation import *
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

botStartTime = time.time()


@Client.on_message(filters.private & filters.command(["ping", "p"]))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("Pinging....", quote=True)
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Ping 🔥!\n{time_taken_s:.3f} ms")
    return time_taken_s



@Client.on_message(filters.command(["stats", "status", "s"]) & filters.user(Config.OWNER_ID))
async def get_stats(bot, message):
    users_count, bots_count = await db.total_users_bots_count()
    total_channels = await db.total_channels()
    uptime = get_readable_time(time.time() - botStartTime)    
    start_t = time.time()
    st = await message.reply('**Processing The Details.....**')    
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await st.edit(text=f"**--Bot Status--** \n\n**⌚ Bot Uptime :** `{uptime}` \n**🐌 Current Ping :** `{time_taken_s:.3f} ms` \n**👭 Total Users :** `{users_count}` \n\n**🤖 Total Bots :** `{bots_count}` \n**✅ Forwarding :** `{temp.forwardings}` \n**🔥 Total Channel :** `{total_channels}` \n**🚫 Banned Users :** `{temp.BANNED_USERS}`")



@Client.on_message(filters.private & filters.command(["donate", "d"]))
async def donate(client, message):
	text = "<b>🥲 Thanks For Showing Interest In Donation! ❤️</b> \n\nBut I don't need any donation, fell free to use this bot. \n\n<b>"
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("🦋 Admin",url = "https://t.me/Stubborn1223"), 
        			InlineKeyboardButton("✖️ Close",callback_data = "close_btn") ]])
	await message.reply_text(text = text,reply_markup = keybord)






# Stubborn Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Stubborn1223
