from flask import Flask, request, Response, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook ():
  if request.method == 'POST':
    data = request.json
    print(data)
    return Response(status=200)
  else:
    return Response(status=400)

if __name__ == '__main__':
  app.run()
