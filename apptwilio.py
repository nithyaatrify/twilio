from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse, Say

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    print(request.form)
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    
    return str(resp)

@app.route("/voice", methods=['POST'])
def voice():
    response = VoiceResponse()
    say = Say('Hi', voice='Polly.Emma')
    say.break_(strength='x-weak', time='100ms')
    say.p('Welcome to the Nithya Agiri voice mail box.')
    say.p('Please subscribe, then leave me a message.')
    say.break_(strength='x-weak', time='50ms')
    say.p('Goodbye!')

    response.append(say)
    response.record()
    response.hangup()

    return str(response)

@app.route('/')
def index():
    return """<p>Subscribe to
    <a href='https://youtube.com/nithyaagiri/'>
        Nithya giri</a>!</p>
    """

if __name__ == '__main__':
    # For deployment, you would typically use a production-ready server like Gunicorn.
    # Example command to run with Gunicorn: gunicorn -b 0.0.0.0:80 your_app_module:app
    app.run(host='0.0.0.0', port=5000)
