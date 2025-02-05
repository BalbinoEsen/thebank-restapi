from core.pyba_logic import PybaLogic
import bcrypt


class CardLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # get
    def getCardByNumber(self, number):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM products where number= '{number}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return {}

    # put
    def insertCard(self, card):
        database = self.createDatabaseObj()

        strBalance = card['balance']
        fBalance = float(strBalance)
        strLimit = card['limit']
        fLimit = float(strLimit)

        code = card['code']
        salt = bcrypt.gensalt(rounds=14)
        strSalt = salt.decode("utf-8")
        encCode = code.encode("utf-8")
        hashCode = bcrypt.hashpw(encCode, salt)
        strCode = hashCode.decode("utf-8")

        sql = (
            f"INSERT INTO `products`"
            + f"(`id`,`name`,`number`,`date`,`code`,`salt`,`balance`,`limit`,`state`) "
            + f"VALUES(0,'{card['name']}','{card['number']}','{card['date']}','{strCode}', "
            + f"'{strSalt}',{fBalance},{fLimit},'{card['state']}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    # patch
    def updateCard(self, number, card):
        database = self.createDatabaseObj()

        code = card['code']
        salt = bcrypt.gensalt(rounds=14)
        strSalt = salt.decode("utf-8")
        encCode = code.encode("utf-8")
        hashCode = bcrypt.hashpw(encCode, salt)
        strCode = hashCode.decode("utf-8")

        sql = (
            "UPDATE `products` "
            + "SET "
            + f"`name` = '{card['name']}', "
            + f"`date` = '{card['date']}', "
            + f"`code` = '{strCode}', "
            + f"`salt` = '{strSalt}', "
            + f"`balance` = {card['balance']}, "
            + f"`limit` = {card['limit']}, "
            + f"`state` = '{card['state']}' "
            + f"WHERE `number` = {number}; "
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCardBalance(self, data):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM products where number={data['number']};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            cardDict = result[0]
            actualBalance = cardDict['balance']
            print(actualBalance)

        cardDigits = cardDict['number']
        cardType = cardDigits[0:4]

        if cardType == "7000": #Crédito
            newBalance = float(cardDict['balance']) + float(data['balance'])
            if newBalance > float(cardDict['limit']):
                return "61" #Excede el limite
        elif cardType == "6000": #Débito
            newBalance = float(cardDict['balance']) - data['balance']
            if newBalance < 0:
                return "51" #Saldo insuficiente
        else:
            return "QY" #Tipo de Tarjeta Invalido

        sql = (
            f"UPDATE `products` "
            + f"SET `balance` = {newBalance} "
            + f"WHERE `number` = {data['number']};"
        )
        rows = database.executeNonQueryRows(sql)
        return "00" #OK!
