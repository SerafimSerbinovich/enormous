from aiogram.fsm.state import State, StatesGroup


class BotStates(StatesGroup):
    waiting_for_prompt = State()
    processing_prompt = State()
