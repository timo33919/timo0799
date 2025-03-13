import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 你的 Telegram Bot Token
TELEGRAM_TOKEN = '7733478738:AAECSymmaZa1hWuVFYgQdqbMAfvXWPI3KGY'

# GitHub 仓库信息
GITHUB_REPO_OWNER = 'timo33919'
GITHUB_REPO_NAME = 'timo0799'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
print(GITHUB_TOKEN,'git_token')

async def trigger_github_action(task: str):
    """
    触发 GitHub Actions 工作流
    """
    url = f'https://api.github.com/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/actions/workflows/auto_deploy.yml/dispatches'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'ref': 'main',  # 触发的主分支
        'inputs': {
            'task': task  # 传递任务标识符
        }
    }
    response = requests.post(url, json=data, headers=headers)
    return response.status_code

async def dep1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    处理 /dep1 命令
    """
    status_code = await trigger_github_action('dep1')
    if status_code == 204:
        if update.message is None:

            return
        await update.message.reply_text('GitHub Action dep1 triggered successfully!')
    else:
        await update.message.reply_text('Failed to trigger GitHub Action dep1.')

async def dep2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    处理 /dep2 命令
    """
    status_code = await trigger_github_action('dep2')
    if status_code == 204:
        if update.message is None:

            return
        await update.message.reply_text('GitHub Action dep2 triggered successfully!')
    else:
        await update.message.reply_text('Failed to trigger GitHub Action dep2.')

def main():
    """
    启动 Bot
    """
    # 创建 Application 实例
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # 添加命令处理器
    application.add_handler(CommandHandler("dep1", dep1))
    application.add_handler(CommandHandler("dep2", dep2))

    # 启动 Bot
    application.run_polling()

if __name__ == '__main__':
    # import asyncio

    # 使用 asyncio.run() 运行 main()
    # asyncio.run(main())
    main()
