import faust
import string

app = faust.App(
    'faust-example',
    broker='kafka://localhost:9093',
    value_serializer='raw',
)

greetings_topic = app.topic('greetings')
farewells_topic = app.topic('farewells')


@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)


@app.agent(farewells_topic)
async def farewell(farewells):
    async for farewell in farewells:
        print(str(farewell).upper())
