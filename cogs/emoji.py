import emoji


class Emoji:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if message.server.id == '356226185224519682':
            print(message.content)
            detected = False
            for c in message.content:
                if not c in emoji.UNICODE_EMOJI and not c in (' ', '\n'):
                    detected = True

            print(detected)

            if detected:
                print('NON-EMOJI DETECTED')
                await self.bot.delete_message(message)

def setup(bot):
    bot.add_cog(Emoji(bot))
