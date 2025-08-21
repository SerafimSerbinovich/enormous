# LLM Telegram Bot

A modern Telegram bot with Large Language Model (LLM) integration, built with FastAPI and aiogram. This project provides both a Telegram bot interface and a REST API for AI-powered conversations.

## Features

- 🤖 **Telegram Bot Interface**: Interactive chat with AI through Telegram
- 🌐 **REST API**: HTTP endpoints for LLM integration
- 🧠 **OpenAI Integration**: Powered by GPT models (configurable)
- ⚡ **FastAPI Backend**: High-performance async web framework
- 🔄 **State Management**: Conversation state handling with FSM
- 🛡️ **Error Handling**: Robust error management and user feedback

## Project Structure

```
llm/
├── config.py              # Configuration settings
├── main.py                # Application entry point
├── requirements.txt       # Python dependencies
└── core/
    ├── bot/
    │   ├── bot.py         # Telegram bot handlers
    │   └── states.py      # Bot state definitions
    ├── model/
    │   └── model.py       # LLM integration
    └── web/
        └── routers.py     # FastAPI routes
```

## Prerequisites

- Python 3.8+
- Telegram Bot Token
- OpenAI API Key (or compatible LLM provider)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd llm
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   # Telegram Bot Configuration
   BOT_TOKEN=your_telegram_bot_token
   ADMIN_IDS=123456789,987654321
   WEBHOOK_URL=https://your-domain.com
   WEBHOOK_PATH=/webhook
   LOG_LEVEL=INFO

   # LLM Configuration
   LLM_MODEL=gpt-4o-mini
   LLM_API_KEY=your_openai_api_key
   LLM_API_BASE=https://api.openai.com/v1
   LLM_API_VERSION=2024-02-15
   LLM_API_TYPE=openai
   ```

4. **Update configuration**
   Modify `config.py` to match your environment variables or use the default values.

## Usage

### Running the Application

Start the application with:
```bash
python main.py
```

This will start both the Telegram bot and the FastAPI web server.

### Telegram Bot Commands

- `/start` - Initialize the bot and get welcome message
- `/help` - Display available commands
- `/prompt` - Start a conversation with the AI
- `/cancel` - Cancel current operation

### Web API Endpoints

The application provides a REST API for LLM interactions:

- **POST** `/llm/` - Send a prompt to the LLM
  - Body: `content: string`
  - Returns: AI response as text

Example:
```bash
curl -X POST "http://localhost:8000/llm/" \
     -H "Content-Type: application/json" \
     -d '{"content": "Hello, how are you?"}'
```

## Configuration

### Bot Configuration

- `token`: Your Telegram bot token from @BotFather
- `admin_ids`: List of admin user IDs
- `webhook_url`: Webhook URL for production deployment
- `webhook_path`: Webhook path endpoint
- `log_level`: Logging level (DEBUG, INFO, WARNING, ERROR)

### LLM Configuration

- `model`: LLM model name (e.g., "gpt-4o-mini")
- `api_key`: Your OpenAI API key
- `api_base`: API base URL
- `api_version`: API version
- `api_type`: API type (openai, azure, etc.)

## Dependencies

Key dependencies include:
- `fastapi`: Web framework
- `aiogram`: Telegram bot framework
- `openai`: OpenAI API client
- `uvicorn`: ASGI server
- `python-dotenv`: Environment variable management

See `requirements.txt` for complete dependency list.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions:
- Create an issue in the repository
- Check the configuration and environment setup
- Ensure all dependencies are properly installed
