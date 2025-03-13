# pip install python-telegram-bot requests

import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 你的 Telegram Bot Token
TELEGRAM_TOKEN = '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'

# GitHub 仓库信息
GITHUB_REPO_OWNER = 'timo33919'
GITHUB_REPO_NAME = 'timo0799'
GITHUB_TOKEN = "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"


def trigger_github_action(task: str):
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

def dep1(update: Update, context: CallbackContext):
    status_code = trigger_github_action('dep1')
    if status_code == 204:

        update.message.reply_text('GitHub Action dep1 triggered successfully!')
    else:
        if update.message is None:
            print('not message')
            return
        update.message.reply_text('Failed to trigger GitHub Action dep1.')

def dep2(update: Update, context: CallbackContext):
    status_code = trigger_github_action('dep2')
    if status_code == 204:

        update.message.reply_text('GitHub Action dep2 triggered successfully!')
    else:
        # if update.message is None:
        #     print('dep2 not message')
        #     return
        update.message.reply_text('Failed to trigger GitHub Action dep2.')


def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("dep1", dep1))
    dispatcher.add_handler(CommandHandler("dep2", dep2))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
