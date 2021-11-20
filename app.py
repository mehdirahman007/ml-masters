from flask import Flask, render_template, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import numpy as np

engine = create_engine('sqlite:///supermarket.db')

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

# Save reference to the table
market = Base.classes.supermarket

app = Flask(__name__)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.route('/machinelearning')
def parameters():
    return render_template('machinelearning.html')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.route('/tableau')
def tableau():
    return render_template('tableau.html')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



@app.route('/db_call')
def dbCall():
    session = Session(engine)

    
    # Query all passengers
    results = session.query(market.ID, market.Year_Birth,market.Education,market.Marital_Status,market.Income,market.Kidhome,
    market.Teenhome,market.Dt_Customer,market.Recency,market.MntWines,market.MntFruits,market.MntMeatProducts,market.MntFishProducts,
    market.MntSweetProducts,market.MntGoldProds,market.NumDealsPurchases,market.NumWebPurchases,market.NumCatalogPurchases,
    market.NumStorePurchases,market.NumWebVisitsMonth,market.AcceptedCmp3,market.AcceptedCmp4,market.AcceptedCmp5,market.AcceptedCmp1,
    market.AcceptedCmp2,market.Complain,market.Z_CostContact,market.Z_Revenue,market.Response).all()

  


    session.close()
    col_names = [
            "ID", 
            "Year_Birth",
            "Education",
            "Marital_Status",
            "Income",
            "Kidhome",
            "Teenhome",
            "Dt_Customer",
            "Recency",
            "Wines",
            "Fruits",
            "Meat",
            "Fish",
            "Sweets",
            "Gold",
            "Deals_Purchases",
            "Web_Purchases",
            "Catalog_Purchases",
            "Store_Purchases",
            "WebVisits",
            "Cmp3",
            "Cmp4",
            "Cmp5",
            "Cmp1",
            "Cmp2",
            "Complain",
            "Cost",
            "Revenue",
            "Response"

    ]


    data = [dict(zip(col_names,result)) for result in results]




    # for arrest_key, arrest_date, pd_desc, ofns_desc, law_cat_cd, age_group, perp_sex, latitude, longitude, perp_race, district in results:
    #     n = {
    #         "arrest_key" : arrest_key,
    #         "arrest_date": arrest_date,
    #         "pd_desc": pd_desc,
    #         "ofns_desc": ofns_desc,
    #         "law_cat_cd": law_cat_cd,
    #         "age_group": age_group,
    #         "perp_sex": perp_sex,
    #         "latitude": latitude,
    #         "longitude": longitude,
    #         "perp_race": perp_race,
    #         "borough": district

    #     }

    #     market_data.append(n)



    return jsonify(data)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)