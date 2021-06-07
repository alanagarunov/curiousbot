import sqlite3
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import time

# initialprice = 5.1264
# theta = 0.001
# totalvolume = 10000


def getdata(named):
    try:
        conn = sqlite3.connect("portfolios.db")
        c = conn.cursor()
        c.execute("SELECT * FROM portfolio WHERE name=:name", {"name": str(named)})
        row = c.fetchall()
        themessage = "Here is your portfolio entry: " + str(row[0])
        conn.close()
        return themessage
    except:
        themessage = "If you are seeing this, you likely do not have a portfolio. Try to buy a stock to make a portfolio."
        return themessage


def getstockprice():
    conn = sqlite3.connect("permanent_stock_value.db")
    c = conn.cursor()
    c.execute("SELECT * FROM stock_values")
    stockrow = c.fetchall()
    newstockrow = stockrow[0]
    initialprice = newstockrow[0]
    totalvolume = newstockrow[1]
    conn.close()
    thethemessage = (
        "The current price is "
        + str(initialprice)
        + " and the current available volume is "
        + str(totalvolume)
    )
    return thethemessage


def adddata(named, sharetype, amount):
    # initialprice = 5.1264
    # theta = 0.001
    # totalvolume = 10000

    conn = sqlite3.connect("portfolios.db")
    conn1 = sqlite3.connect("permanent_stock_value.db")
    c = conn.cursor()
    d = conn1.cursor()
    # c.execute("CREATE TABLE portfolio (name text, sharesowned integer, value real)")
    # d.execute("CREATE TABLE stock_values (shareprice real, volume integer)")
    d.execute(
        "INSERT INTO stock_values VALUES (:shareprice, :volume)",
        {"shareprice": 5.1264, "volume": 10000},
    )
    d.execute("SELECT * FROM stock_values")
    stockrow = d.fetchall()
    newstockrow = stockrow[0]
    initialprice = newstockrow[0]
    totalvolume = newstockrow[1]

    c.execute("SELECT * FROM portfolio WHERE name=:name", {"name": str(named)})
    row = c.fetchall()
    print(row)
    if not row:  # and type(row) is not list
        c.execute(
            "INSERT INTO portfolio VALUES (:name, :sharesowned, :value)",
            {"name": str(named), "sharesowned": 0, "value": 100},
        )
        sucessfulmessage = "You didn't have a portfolio entry before, now you do. Try executing your trade again."
    elif sharetype == "buy":
        newrow = row[0]
        purchase = initialprice * float(amount)
        purchase = round(purchase, 2)
        temppurchase = float(newrow[2]) - float(purchase)
        temppurchase = round(temppurchase, 2)

        if float(newrow[2]) < purchase:
            sucessfulmessage = "You don't have enough money for this anymore!"
        elif (
            int(newrow[1]) > totalvolume
            or int(amount) < 0
            or (totalvolume - int(amount)) < 0
            or int(amount) > (float(totalvolume) * 0.5)
        ):
            sucessfulmessage = "There is no volume for this, or made an illegal operation. The SEC will be notified."
        else:
            tempamount = int(newrow[1]) + int(amount)
            # c.execute("UPDATE portfolio SET sharesowned = :sharesowned, value = :value WHERE name = :name" {'name': named, 'sharesowned': int(tempamount), 'value': float(temppurchase)})
            c.execute(
                "UPDATE portfolio SET sharesowned = :sharesowned WHERE name = :name",
                {"name": str(named), "sharesowned": int(tempamount)},
            )
            c.execute(
                "UPDATE portfolio SET value = :value WHERE name = :name",
                {"name": str(named), "value": float(temppurchase)},
            )
            increaseinprice = int(amount) / 100
            increaseinprice = round(increaseinprice, 2)
            initialprice = initialprice + increaseinprice
            totalvolume = totalvolume - int(amount)
            d.execute(
                "UPDATE stock_values SET shareprice = :shareprice",
                {"shareprice": float(initialprice)},
            )
            d.execute(
                "UPDATE stock_values SET volume = :volume", {"volume": int(totalvolume)}
            )
            """
            thetime = round(time.time())
            price.append(initialprice)
            timesincestart.append(thetime)
            """
            sucessfulmessage = (
                "<@!"
                + str(named)
                + ">"
                + " has bought "
                + str(amount)
                + " of share(s) "
                + "for a total of "
                + str(purchase)
                + ". The stock is now worth "
                + str(initialprice)
            )
    elif sharetype == "sell":
        newrow = row[0]
        purchase = initialprice * float(amount)
        purchase = round(purchase, 2)
        temppurchase = float(newrow[2]) + float(purchase)
        temppurchase = round(temppurchase, 2)
        if (
            newrow[1] < int(amount)
            or int(amount) < 0
            or (totalvolume - int(amount)) < 0
        ):
            sucessfulmessage = "You don't have the shares you're trying to sell! or made an illegal operation. The SEC will be notified."
        else:
            tempamount = int(newrow[1]) - int(amount)
            # c.execute("UPDATE portfolio SET sharesowned = :sharesowned, value = :value WHERE name = :name" {'name': named, 'sharesowned': int(tempamount), 'value': float(temppurchase)})
            c.execute(
                "UPDATE portfolio SET sharesowned = :sharesowned WHERE name = :name",
                {"name": str(named), "sharesowned": int(tempamount)},
            )
            c.execute(
                "UPDATE portfolio SET value = :value WHERE name = :name",
                {"name": str(named), "value": float(temppurchase)},
            )
            decreaseinprice = int(amount) / 100
            decreaseinprice = round(decreaseinprice, 2)
            initialprice = initialprice - decreaseinprice
            totalvolume = totalvolume + int(amount)
            d.execute(
                "UPDATE stock_values SET shareprice = :shareprice",
                {"shareprice": float(initialprice)},
            )
            d.execute(
                "UPDATE stock_values SET volume = :volume", {"volume": int(totalvolume)}
            )
            """
            thetime = round(time.time())
            price.append(initialprice)
            timesincestart.append(thetime)
            """
            sucessfulmessage = (
                "<@!"
                + str(named)
                + ">"
                + " has sold "
                + str(amount)
                + " of share(s) "
                + "for a total of "
                + str(purchase)
                + ". The stock is now worth "
                + str(initialprice)
            )

    else:
        sucessfulmessage = (
            "Either you have more than one portfolio entry or something went wrong."
        )
    conn.commit()
    conn1.commit()
    return sucessfulmessage
