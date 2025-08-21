from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

import config
from core.bot.states import BotStates
from core.model.model import llm

bot = Bot(token=config.bot.token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "Hello! 👋 I'm your tg bot.\n"
        "Use /help to get command list.\n"
        "Use /prompt to start a conversation with AI."
    )


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/prompt - Start a conversation with AI\n"
        "/cancel - Cancel current operation"
    )


@dp.message(Command("prompt"))
async def prompt_command(message: Message, state: FSMContext):
    await state.set_state(BotStates.waiting_for_prompt)
    await message.answer(
        "Please enter your prompt/question for the AI:"
    )


@dp.message(Command("cancel"))
async def cancel_command(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Nothing to cancel.")
        return
    
    await state.clear()
    await message.answer("Operation cancelled.")


@dp.message(StateFilter(BotStates.waiting_for_prompt))
async def handle_prompt(message: Message, state: FSMContext):
    user_prompt = message.text
    
    await state.set_state(BotStates.processing_prompt)
    await message.answer("Processing your prompt... Please wait.")
    
    try:
        response = llm.get_llm_response(user_prompt)
        
        await message.answer(f"AI Response:\n\n{response}")
        
        await state.set_state(BotStates.waiting_for_prompt)
        await message.answer("Enter another prompt or use /cancel to stop:")
        
    except Exception as e:
        await message.answer(f"Error processing your prompt: {str(e)}")
        await state.set_state(BotStates.waiting_for_prompt)
        await message.answer("Please try again or use /cancel to stop:")


@dp.message(StateFilter(BotStates.processing_prompt))
async def handle_processing_state(message: Message):
    await message.answer("Please wait, I'm still processing your previous request...")


@dp.message()
async def handle_any_message(message: Message, state: FSMContext):
    current_state = await state.get_state()
    
    if current_state is None:
        await message.answer(
            "Hello! Use /prompt to start a conversation with AI or /help to see available commands."
        )
    else:
        if message.text.startswith('/'):
            await message.answer("Please complete your current operation first or use /cancel to stop.")
        else:
            await message.answer("Please wait for the current operation to complete.")