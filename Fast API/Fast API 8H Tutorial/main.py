from enum import Enum
from typing import Optional, Literal, Union
from uuid import UUID
from datetime import datetime, time, timedelta

from fastapi import Body, FastAPI, Query, Path, Cookie, Header
from pydantic import BaseModel, Field, HttpUrl, EmailStr

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.post("/")
# async def post():
#     return {"message": "hello from the post route"}


# @app.put("/")
# async def put():
#     return {"message": "hello from the put route"}


# @app.get("/user")
# async def list_users():
#     return {"message": "list users route"}

# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
#     return {"user_id": user_id}

# @app.get("/users/me")
# async def get_current_user():
#     return {"message": "this is the current user"}

# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"

# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name": food_name, "message": "you are healthy"}
    
#     if food_name.value == "fruits":
#         return {
#             "food_name": food_name,
#             "message": "you are still healthy, but like sweet things"
#         }
#     return {"food name": food_name, "message": "i like chocolate milk"}


# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/items")
# async def list_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# @app.get("/items/{item_id}")
# async def get_item(item_id: str, sample_query_param: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "sample_query_param": sample_query_param}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus libero." 
#             }
#         )
#     return item

# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus libero." 
#             }
#         )
#     return item

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

# @app.get("/read_items")
# async def read_items(q: str 
#                      | None = Query(
#                          None, 
#                         min_length=3, 
#                         max_length=10, 
#                         title="Sample query string",
#                         description="Sample description",
#                         deprecated=True
#                         )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get('/items_hidden')
# async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {'hidden_query': 'Not found'}

# @app.get("/items_validation/{item_id}")
# async def read_items_validation(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=10, le=100),
#     q: str = 'hello',
#     size: float = Query(..., gt=0, lt=7.75)   
# ):
#     results = {"item_id": item_id, "size": size}
#     if q:
#         results.update({"q": q})
#     return results



# Part 7 -> Body - Multiple Parameters

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class User(BaseModel):
#     user: str
#     full_name: str | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150),
#     q: str | None = None,
#     item: Item | None = None,
#     user: User,
#     importance: int = Body(...)
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     if importance:
#         results.update({"importance": importance})
#     return results
    

# Part 8 -> Body - Fields

# class Item(BaseModel):
#     name: str
#     description: str| None = Field(None, title="The description of the item",
#                                    max_length=300
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero.")
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results

# Part 9 -> Body - Nested Models

# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []
#     image: list[Image] | None = None


# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# @app.post("/offers")
# async def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer

# @app.post("/images/multiple")
# async def create_multiple_images(images: list[Image] = Body(..., embed=True)):
#     return images


# Part 10 Decalre Request Example Data

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# class Config:
#     schema_extra = {
#         "example": {
#             "name": "Foo",
#             "description": "A very nice Item",
#             "price": 16.25,
#             "tax": 1.67
#         }
#     }

# @app.put("/item/{item_id}")
# async def Update_item(item_id: int, 
#                       item: Item = Body(
#                           ...,
#                           example={
#                             "name": "Foo",
#                             "description": "A very nice Item",
#                             "price": 16.25,
#                             "tax": 1.67   
#                           },
#                       ),
# ):
                      
#     results = {"item_id": item_id, "item": item}
#     return results


# Part 11 Extra Data Types
    
# @app.put("/items/{item)id}")
# async def read_items(
#     item_id: UUID, 
#     start_date: datetime | None = Body(None),
#     end_date: datetime | None = Body(None),
#     repeat_at: time | None = Body(None),
#     process_after: timedelta | None = Body(None),
# ):
#     start_process = start_date + process_after
#     duration = end_date - start_process
#     return {
#         "item_id": item_id,
#         "start_date": start_date, 
#         "end_date": end_date, 
#         "repeat_at": repeat_at, 
#         "process_after": process_after, 
#         "start_process": start_process, 
#         "duration": duration
#     }
    
# Part 12 - Cookie and Header Parameters
    
# @app.put("/items")
# async def read_items(
#     cookie_id: str | None = Cookie(None),
#     accept_encoding: str | None = Header(None),
#     sec_ch_ua: str | None = Header(None),
#     user_agent: str | None = Header(None),
#     x_token: list[str] | None = Header(None)
# ):
#     return{
#         "cookie_id": cookie_id,
#         "Acceot-Encoding": accept_encoding,
#         "sec_ch_ua": sec_ch_ua,
#         "User-Agent": user_agent,
#         "X-token values": x_token
#     }
    
# Part 13 - Response Model
    
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []  

# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []} 
# }

# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]


# @app.post("/items/")
# async def create_item(item: Item):
#     return item


# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# class UserIn(UserBase):
#     password: str


# class UserOut(UserBase):
#     pass

# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user

# @app.get(
#         "/items/{item_id}/name", 
#         response_model=Item, 
#         response_model_include={"name", "description"}
# )


# async def read_item_name(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]

# @app.get("/items/{item_id/public}", response_model=Item, response_model_exclude={"tax"})
# async def read_items_public_data(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]
    
# Part 14 - Extra Models
    
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

    
# class UserIn(UserBase):
#     password: str
   

# class UserOut(UserBase):
#     pass

# class UserInDB(UserBase):
#     hashed_password: str
    

# def fake_password_haser(raw_password: str):
#     return f"supersecret{raw_password}"

# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_haser(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print("userin.dict", user_in.dict())
#     print("User 'saved'.")
#     return user_in_db

# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved

# class BaseItem(BaseModel):
#     description: str
#     type: str

# class CarItem(BaseItem):
#     type = "car"

# class PlaneItem(BaseItem):
#     type = "plane"
#     size: int

# items = {
#     "item1": {"description": "All mt friends drive a low raider", type: "car"},
#     "item2": {
#         "description": "Music is my areoplane, it's my areoplane",
#         "type": "plane",
#         "size": 5,
#     }
# }

# @app.get("/items/{item_id}", response_model=Union(PlaneItem, CarItem))
# async def read_item(item_id: Literal["item1", "item2"]):
#     return item_id


