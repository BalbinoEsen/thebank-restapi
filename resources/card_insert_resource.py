import bcrypt
from flask_restful import Resource, reqparse
from logic.card_logic import CardLogic
import bcrypt


class CardInsert(Resource):
    def __init__(self):
        self.card_put_args = self.createParser()
        self.logic = CardLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("name", type=str, help="name of the client")
        args.add_argument("number", type=str, help="number of the card")
        args.add_argument("date", type=str, help="date of the card")
        args.add_argument("code", type=str, help="code of the card")
        args.add_argument("salt", type=str, help="salt of the card")
        args.add_argument("balance", type=float, help="balance of the card")
        args.add_argument("limit", type=float, help="limit of the card")
        args.add_argument("state", type=str, help="state of the card")
        return args

    def put(self):
        card = self.card_put_args.parse_args()
        rows = self.logic.insertCard(card)
        return {"rowsAffected": rows}
