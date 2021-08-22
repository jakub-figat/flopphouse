import uvicorn
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from fastapi import FastAPI

app = FastAPI()

type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()


@query.field("hello")
def resolve_hello(*_):
    return "Hello world!"


schema = make_executable_schema(type_defs, query)


app.mount("/graphql", GraphQL(schema, debug=True))


@app.get("/hello")
async def hello():
    return {"hello": "hello"}
