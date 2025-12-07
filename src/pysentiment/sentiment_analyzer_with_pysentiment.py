from pysentimiento import create_analyzer 

class Animo:
    def __init__(self, emoji, feeling):
        self.emoji = emoji
        self.feeling = feeling
    
    def __repr__(self):
        return f"Animo(emoji={self.emoji}, feeling={self.feeling})"
    
def get_encouraged(input_text, *, sensibility):
    analyzer = create_analyzer(task="sentiment", lang="es")
    result = analyzer.predict(input_text)
    polarity = result.probas[result.output]
    friendly_threshold = sensibility
    hostile_threshold = -sensibility
    
    if result.output == "POS":
        return Animo(emoji='😀', feeling=polarity)
    elif result.output == "NEG":
        return Animo(emoji='😡', feeling=polarity)
    else:
        return Animo(emoji='😐', feeling=polarity)
    
def bot_init():
    print("Bot: introduce algun texto y realizare un analisis de sentimientos sobre el.")
    
    while True:
        input_user = input("Tu: ")
        animo = get_encouraged(input_user, sensibility=0.3)
        print(f"Bot: {animo.emoji} ({animo.feeling})")
        
bot_init()