import slack
from fastapi import FastAPI, Response, status
from starlette.responses import StreamingResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"Status": "OK"}

@app.get("/slack")
async def getSlackEvent():
    

@app.post("/slack")
async def postSlackEvent():


# @app.get("/image")
# async def image(response: Response):
#     global mutex
#     mutex.acquire()

#     frame = streamers.get_latest_frame()
#     res, im_jpg = cv2.imencode(".jpg", frame)

#     mutex.release()
#     return StreamingResponse(io.BytesIO(im_jpg.tobytes()), status_code=200)


if __name__ == '__main__':
    SLACK_TOKEN = 'xoxb-150535160992-2719557105524-Bv7IrjHHHjgIjd0aaLftEFKc'
    SLACK_CHANNEL_ID = 'C02M5GWM1HS'
    slack.pushSlackMessage(SLACK_TOKEN, SLACK_CHANNEL_ID, "Test message")


'''
# 이벤트 핸들하는 함수
def event_handler(event_type, slack_event):
    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        text = get_answer()
        slack.chat.post_message(channel, text)
        return make_response("앱 멘션 메시지가 보내졌습니다.", 200, )
    message = "[%s] 이벤트 핸들러를 찾을 수 없습니다." % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})

@app.route("/slack", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)
    return make_response("슬랙 요청에 이벤트가 없습니다.", 404, {"X-Slack-No-Retry": 1})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
'''