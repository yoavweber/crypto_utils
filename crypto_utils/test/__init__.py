from asyncio import Future
import os
from aio_pika import connect, ExchangeType, Message, DeliveryMode, Exchange, IncomingMessage, Channel
import json



class AMQP_Client():
    def __init__(self):
        self.client = None
        self.futures_exchange = None

    def get_client(self):
        if self.client == None:
            raise ValueError(
                "ampq client was not created. use create_future_client in async function to create one")
        return self.client

    async def create_client(self) -> Channel:
        if self.client != None:
            return self.client

        amqp_url = os.getenv("RABBITMQ_URL")
        if amqp_url:
            connection = await connect(amqp_url)
            channel: Channel = await connection.channel()
            await channel.set_qos(prefetch_count=1)
            self.client = channel
            return channel
        raise Exception("coud not find RABBITMQ_URL env var")

    async def create_exchange(self) -> Exchange:
        if self.futures_exchange != None:
            return self.futures_exchange

        client = await self.create_client()
        # app.logger.info("Creating futures exchange")
        exchange = await client.declare_exchange(
            "futures", ExchangeType.DIRECT, durable=True)
        self.futures_exchange = exchange
        return exchange

    async def create_consumer(self, callback, queue_name: str):
        channel = await self.create_client()
        exchange = await self.create_exchange()
        queue = await channel.declare_queue(durable=True)

        await queue.bind(exchange, routing_key=queue_name)
        consumer_tag = await queue.consume(callback)
        # app.logger.info(f"futures {queue_name} queue ready to consume ")
        return queue, consumer_tag

    # INFO: might make sense to move those 2 into seperate message class
    async def send_data(self, data, routing_key: str,priority: int=0):
        if self.futures_exchange == None:
            # app.logger.warning("Futures exchange was not initilize")
            # app.logger.info("creating futures exchange")
            self.futures_exchange = await self.create_exchange()

        parsed_message = bytes(json.dumps(data), encoding='utf8')
        message = Message(
            parsed_message, delivery_mode=DeliveryMode.PERSISTENT,priority=priority)
        await self.futures_exchange.publish(message, routing_key=routing_key)

    def decode_data(self, message: IncomingMessage):
        data = message.body.decode("utf-8")
        dic = json.loads(data)
        return dic


class RPC_Client:
    def __init__(self, future: Future):
        self.future = future

    def on_response(self, message: Message):
        print(message, "from on response")
        self.future.set_result(message)

    async def consume_exchange(self, amqp: AMQP_Client, route_key, timeout: int):
        await amqp.create_consumer(self.on_response, route_key)
        print("after consumer")
        res = await self.future
        # res =  await wait_for(self.future,timeout)
        if self.future == None:
            # app.logger.warning("future did not completed")
            return self.future
        return res
