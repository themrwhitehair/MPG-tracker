# Several lines of code based on python-telegram-bot's github entry "Your first bot" at <https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot>

#  dependancies
from privateVariables import API_KEY, help_text
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sqlite3, logging

# connect to database
con = sqlite3.connect('tracker.db', check_same_thread=False)
cur = con.cursor()

# connect program to bot
updater = Updater(token=API_KEY, use_context=True)
disp = updater.dispatcher

# error checking module
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


# commands
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="BOT STARTED")


def help(update, context):
    if len(context.args) != 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please dont add text to the command")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)


def refill(update, context):
    if len(context.args) != 3:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please use the correct format.\nUse /help for more information.")
    else:
        if not context.args[0].isnumeric():
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please use the correct price format.\nUse /help for more information.")
        elif not context.args[1].isnumeric():
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please use the correct quantity format.\nUse /help for more information.")
        elif not context.args[2].isnumeric():
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please use the correct mileage format.\nUse /help for more information.")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Logged successfully")

            quantity = float(context.args[1])
            price = float(context.args[0])
            miles = float(context.args[2])
            mpg = miles / quantity
            msgDate= update.message.date

            cur.execute("INSERT INTO refills (id, quantity, price, miles, mpg, date) VALUES (?, ?, ?, ?, ?, ?)",
                        [update.message.chat_id, round(quantity, 2), round(price, 2), round(miles, 2), round(mpg, 2), msgDate.date()])
            con.commit()


def lastlog(update, context):
    if len(context.args) != 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please dont add text to the command")
    else:
        for row in cur.execute("SELECT * FROM refills WHERE id = (?) ORDER BY rowid DESC LIMIT 1", [update.message.chat_id]):
            context.bot.send_message(chat_id=update.effective_chat.id, text=
                                     "Price: $" + str(row[2]) + ", Gallons: " + str(row[1]) + ", Miles: " + str(row[3]) + ", MPG: " + str(round(row[4], 2)) + ", Date: " + str(row[5]) + " UTC")

def log(update, context):
    if len(context.args) != 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please dont add text to the command")
    else:
        userLog = cur.execute("SELECT * FROM refills WHERE id = (?) ORDER BY rowid DESC", [update.message.chat_id])
        for row in userLog:
            context.bot.send_message(chat_id=update.effective_chat.id, text=
                                     "Price: $" + str(row[2]) + ", Gallons: " + str(row[1]) + ", Miles: " + str(row[3]) + ", MPG: " + str(round(row[4], 2)) + ", Date: " + str(row[5]) + " UTC")

def mpg(update, context):
    totalMPG = cur.execute("SELECT AVG(mpg) FROM refills WHERE id = (?)", [update.message.chat_id])
    for row in totalMPG:
        context.bot.send_message(chat_id=update.effective_chat.id, text="In total youve gotten about " + str(round(row[0], 2)) + " miles per gallon")

def currentmpg(update, context):
    if len(context.args) != 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please dont add text to the command")
    else:
        recentMPG = cur.execute("SELECT AVG(mpg) FROM refills ORDER BY rowid DESC LIMIT 1")
        for row in recentMPG:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Lately you've been getting about " + str(round(row[0], 2)) + " miles per gallon")

def spent(update, context):
    if len(context.args) > 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Check out /help for correct use")
    elif len(context.args) == 1:
        if len(context.args[0]) != 4 or not context.args[0].isnumeric():
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please use the /help command for instructions on how to use this command")
        else:
            total = 0
            spentObj = cur.execute("SELECT price, date FROM refills WHERE id = (?)", [update.message.chat_id])
            for row in spentObj:
                if context.args[0] in row[1]:
                    total += row[0]
            context.bot.send_message(chat_id=update.effective_chat.id, text= "You have spent $" + str(round(total, 2)) + " in this year." )
    else:
        spentObj = cur.execute("SELECT SUM(price) FROM refills WHERE id = (?)", [update.message.chat_id])
        for row in spentObj:
            context.bot.send_message(chat_id=update.effective_chat.id, text= "You have spent, in total, $" + str(round(row[0], 2)) + " on fuel.")

def delete(update, context):
    if len(context.args) == 1:
        if context.args[0] == "ALL":
            cur.execute("DELETE FROM refills WHERE id = (?)", [update.message.chat_id])
            context.bot.send_message(chat_id=update.effective_chat.id, text="All user logs deleted")
            con.commit()
    elif len(context.args) != 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please dont add incorrect text to the command")
    
    else:
        to_be_deleted = cur.execute("SELECT rowid FROM refills WHERE id = (?) ORDER BY rowid DESC LIMIT 1", [update.message.chat_id])
        for row in to_be_deleted:
            cur.execute("DELETE FROM refills WHERE rowid = (?)", [row[0]])
            con.commit()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Last log deleted")




# messages
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please use one of the listed commands :)")


# command handlers
start_handler = CommandHandler('start', start)
disp.add_handler(start_handler)

help_handler = CommandHandler('help', help)
disp.add_handler(help_handler)

refill_handler = CommandHandler('refill', refill)
disp.add_handler(refill_handler)

lastlog_handler = CommandHandler('lastlog', lastlog)
disp.add_handler(lastlog_handler)

log_handler = CommandHandler('log', log)
disp.add_handler(log_handler)

mpg_handler = CommandHandler('mpg', mpg)
disp.add_handler(mpg_handler)

currentmpg_handler = CommandHandler('currentmpg', currentmpg)
disp.add_handler(currentmpg_handler)

spent_handler = CommandHandler('spent', spent)
disp.add_handler(spent_handler)

delete_handler = CommandHandler('delete', delete)
disp.add_handler(delete_handler)


# message handlers
# must come after all other handlers
unknownMsg_handler = MessageHandler(Filters.all, unknown)
disp.add_handler(unknownMsg_handler)


updater.start_polling()
