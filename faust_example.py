import faust

app = faust.App(
    'faust-example',
    broker='kafka://localhost:9093',
    value_serializer='raw',
)

greetings_topic = app.topic('greetings')


@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)
