from flask import Flask
from flask_restful import Api
from resources.card_verif_resource import CardVerify
from resources.card_id_resource import CardId
from resources.card_insert_resource import CardInsert


app = Flask(__name__)
api = Api(app)


api.add_resource(CardVerify, "/verify")
api.add_resource(CardId, "/card/<int:number>")
api.add_resource(CardInsert, "/insert")

if __name__ == "__main__":
    app.run(debug=True, port=12345)
