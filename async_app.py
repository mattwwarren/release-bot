from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.starlette.async_handler import AsyncSlackRequestHandler
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route

app = AsyncApp()
app_handler = AsyncSlackRequestHandler(app)


@app.event("app_mention")
async def handle_app_mentions(body, say, logger):
    logger.info(body)
    await say("What's up?")


@app.event("app_uninstalled")
async def handle_app_uninstall(body, say, logger):
    logger.info(body)
    await say("What's up?")


@app.event("bot_added")
async def handle_new_server(body, say, logger):
    logger.info(body)
    await say("What's up?")


@app.event("team_join")
async def handle_new_user(body, say, logger):
    logger.info(body)
    await say("What's up?")


@app.event("user_changed")
async def handle_user_deleted(body, say, logger):
    logger.info(body)
    await say("What's up?")


@app.command("/add-release-environment")
async def handle_add_user(ack, body, respond):
    await ack()
    await respond(f"Hello <@{body['user_id']}>")

async def echo(req: Request):
    return await app_handler.handle(req)


api = Starlette(debug=True, routes=[Route("/slack/echo", endpoint=echo, methods=["POST"])])
