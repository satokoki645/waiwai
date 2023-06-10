from sqlalchemy import Column, Integer, String ,ForeignKey,DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    user_name = Column(String, unique=True, index=True)
    password = Column(String)

    team = relationship("Team", back_populates="users")

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, unique=True, index=True)

    users = relationship("User", back_populates="team")
    products = relationship("Product", back_populates="team")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    category_id = Column(Integer, ForeignKey("category.category_id"))
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    team = relationship("Team", back_populates="products")
    category = relationship("Category", back_populates="products")

class Category(Base):
    __tablename__ = "category"

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, unique=True, index=True)
    category_color = Column(String)

    products = relationship("Product", back_populates="category")

class ProductCategory(Base):
    __tablename__ = "product_category"

    product_category_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    category_id = Column(Integer, ForeignKey("category.category_id"))