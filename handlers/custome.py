from chatbot import chatbot
from emoji import emojize

class CusotmeHandlers:

    def __init__(self):
        self.aimlBot = chatbot.ChatBot()

    def josh(self, update, context):
        update.message.reply_text(emojize("High Sir :sunglasses:!! \nVery High!!", use_aliases=True))

    def alarm(self, context):
        """Send the alarm message."""
        job = context.job
        context.bot.send_message(job.context, text='Beep!')

    def setTimer(self, update, context):
        """Add a job to the queue."""
        chat_id = update.message.chat_id
        try:
            due = int(context.args[0])
            if due < 0:
                update.message.reply_text('Sorry we can not go back to future!')
                return

            if 'job' in context.chat_data:
                old_job = context.chat_data['job']
                old_job.schedule_removal()
            new_job = context.job_queue.run_once(self.alarm, due, context=chat_id)
            context.chat_data['job'] = new_job

            update.message.reply_text('Timer successfully set!')

        except (IndexError, ValueError):
            update.message.reply_text('Usage: /set <seconds>')

    def unsetTimer(self, update, context):
        """Remove the job if the user changed their mind."""
        if 'job' not in context.chat_data:
            update.message.reply_text('You have no active timer')
            return

        job = context.chat_data['job']
        job.schedule_removal()
        del context.chat_data['job']

        update.message.reply_text('Timer successfully unset!')

    def default(self, update, context):
        update.message.reply_text(self.aimlBot.getResponseFromBot(update.message.text))
