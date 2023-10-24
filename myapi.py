import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('RgpK0NAgsOMc6hJlk7oXduG7ncVwqHKt4J1Xro9tHig')

    def sentiment(self,text):
        response=paralleldots.sentiment(text)
        return response

    def ner(self,text):
        response=paralleldots.ner(text)
        return response


    def emotion(self,text):
        response=paralleldots.emotion(text)
        return response
