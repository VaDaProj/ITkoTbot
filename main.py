#Bot for Telegram
import telekot  #For work with Telegram API

TOKEN = '437251145:AAHzr29iHTjFgNnMqIiJ7AAqJlnpljQLTKc'  #Token of the telegram bot


def main():
    bot = telekot.Telekot(TOKEN)








if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
