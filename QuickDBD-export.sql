-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "supermarket_data" (
    "id" INT   NOT NULL,
    "year_birth" DATE   NOT NULL,
    "education" string   NOT NULL,
    "marital_status" string   NOT NULL,
    "income" int   NOT NULL,
    "kid_home" int   NOT NULL,
    "teen_home" int   NOT NULL,
    "dt_customer" date   NOT NULL,
    "recency" int   NOT NULL,
    "mnt_wines" int   NOT NULL,
    "mnt_fruits" int   NOT NULL,
    "mnt_meat" int   NOT NULL,
    "mnt_fish" int   NOT NULL,
    "mnt_sweets" int   NOT NULL,
    "mnt_gold" int   NOT NULL,
    "num_deals_purchases" int   NOT NULL,
    "num_web_purchases" int   NOT NULL,
    "num_catalog_purchases" int   NOT NULL,
    "num_store_purchases" int   NOT NULL,
    "num_web_visits_month" int   NOT NULL,
    "accepted_cmp3" int   NOT NULL,
    "accepted_cmp4" int   NOT NULL,
    "accepted_cmp5" int   NOT NULL,
    "accepted_cmp1" int   NOT NULL,
    "accepted_cmp2" int   NOT NULL,
    "complain" int   NOT NULL,
    "z_cost_contact" int   NOT NULL,
    "z_revenue" int   NOT NULL,
    "response" int   NOT NULL,
    CONSTRAINT "pk_supermarket_data" PRIMARY KEY (
        "id"
     )
);

