from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards_q import make_keyboard


router = Router()


q_season = ["весна", "лето", "осень", "зима"]
q_hobby = [
    "гулять",
    "пить чай",
    "смотреть в окно",
    "плавать",
    "ездить на велосипеде",
    "путешевствовать",
    "другое",
]
q_like = [
    "движение",
    "спорт",
    "пить горячее",
    "хочу все видеть",
    "получать информацию",
    "смотреть вокруг",
    "люблю воду",
    "другое",
]


class Choice(StatesGroup):
    season = State()
    hobby = State()
    like = State()


@router.message(Command(commands=["quest"]))
async def start(message: types.Message, state: FSMContext):
    await message.answer(
        "Какое ваше любимое время года?",
        reply_markup=make_keyboard(q_season),
    )
    await state.set_state(Choice.season)


@router.message(Choice.season, F.text.in_(q_season))
async def season(message: types.Message, state: FSMContext):
    await state.update_data(answer_season=message.text)
    await message.answer(
        "Что вам нравится делать в это время года?",
        reply_markup=make_keyboard(q_hobby),
    )
    await state.set_state(Choice.hobby)


##
@router.message(Choice.hobby, F.text.in_(q_hobby))
async def q_third(message: types.Message, state: FSMContext):
    await state.update_data(answer_hobby=message.text)
    await message.answer(
        "А что вам нравится в этом занятии?",
        reply_markup=make_keyboard(q_like),
    )
    await state.set_state(Choice.like)


@router.message(Choice.like, F.text.in_(q_like))
async def hobby(message: types.Message, state: FSMContext):
    await state.update_data(answer_like=message.text)
    data = await state.get_data()
    answers = [
        data.get("answer_season"),
        data.get("answer_hobby"),
        data.get("answer_like"),
    ]
    all_answers = ", ".join(answers)  # Combining all the answers into a single string
    await message.answer(
        f"Вот ваши ответы. ```Ответы: {all_answers}```", parse_mode="Markdown"
    )
    await message.answer(
        f"*Теперь мы всё про вас знаем, за вами уже выехали*.",
        parse_mode="Markdown",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    await state.clear()


##
@router.message(Choice.season)
async def season_incorrectly(message: types.Message):
    await message.answer(
        "Неправильно. Попробуйте ещё раз", reply_markup=make_keyboard(q_season)
    )


@router.message(Choice.hobby)
async def grade_incorrectly(message: types.Message):
    await message.answer(
        "Неправильно. Попробуйте ещё раз", reply_markup=make_keyboard(q_hobby)
    )


@router.message(Choice.like)
async def grade_incorrectly(message: types.Message):
    await message.answer(
        "Неправильно. Попробуйте ещё раз", reply_markup=make_keyboard(q_like)
    )
