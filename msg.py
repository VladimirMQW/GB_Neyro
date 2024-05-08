############### Сообщения
from aiogram import Router, types, F

router = Router()


@router.message(F.text)
# @dp.message(F.text)
async def msg(message: types.Message):
    if (
        "привет" in message.text.lower()
    ):  # ["привет", "здаров", "здравствуй", "здравствуйте"]
        await message.reply("И тебе привет!")
    elif "как дела" in message.text.lower():
        await message.reply("Норм, а у тебя?")
    elif "хорошо" in message.text.lower():
        await message.reply("Ну и отлично!")
    elif "пока" in message.text.lower():
        await message.reply("И вам не хворать!")
    else:
        await message.reply("Не понимаю тебя...")
