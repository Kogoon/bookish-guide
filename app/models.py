# -*- coding: utf-8 -*-
from datetime import datetime

import flask_login

from app import db 


class UserMixin:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    Allergy_List = db.Column(db.String(50))


class UserModel(UserMixin, flask_login.UserMixin, db.Model):
    __tablename__ = 'users'


class ProductMixin:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(30))
    price = db.Column(db.Integer)
    image_url = db.Column(db.String(200))
    product_info_url = db.Column(db.String(200))
    create_date = db.Column(db.DateTime(), nullable=False)


class ProductModel(ProductMixin, db.Model):
    __tablename__ = 'products'


class ItemMixin:
    Item_id = db.Column(db.String(200))
    Item_key = db.Column(db.String(200), primary_key=True)
    계란 = db.Column(db.Boolean, nullable=True)
    우유 = db.Column(db.Boolean, nullable=True)
    땅콩 = db.Column(db.Boolean, nullable=True)
    견과류 = db.Column(db.Boolean, nullable=True)
    밀 = db.Column(db.Boolean, nullable=True)
    갑각류 = db.Column(db.Boolean, nullable=True)
    대두 = db.Column(db.Boolean, nullable=True)
    메밀 = db.Column(db.Boolean, nullable=True)
    쇠고기 = db.Column(db.Boolean, nullable=True)
    돼지고기 = db.Column(db.Boolean, nullable=True)
    닭고기 = db.Column(db.Boolean, nullable=True)
    생선 = db.Column(db.Boolean, nullable=True)
    과일 = db.Column(db.Boolean, nullable=True)
    Nutrition = db.Column(db.String(1000), nullable=True)
    Ingredient = db.Column(db.String(2000), nullable=True)


class ItemModel(ItemMixin, db.Model):
    __tablename__ = 'Item'


class CustommerList(db.Model):
    __tablename__ = "Custommer_list"

    Custommer_ID = db.Column(db.Integer, primary_key=True)
    Custommer_Name = db.Column(db.String(50), nullable=False)
    Allergy_List = db.Column(db.String(50))


class DeliveryMixin:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    address = db.Column(db.String(255))
    detail_address = db.Column(db.String(255))
    phone = db.Column(db.String(20))


class DeliveryModel(DeliveryMixin, db.Model):
    __tablename__ = 'deliveries'

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
