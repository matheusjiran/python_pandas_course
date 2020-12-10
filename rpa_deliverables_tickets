#Webhook listener that returns deal id

from flask import Flask, request, Response, abort
import pandas as pd
app = Flask(__name__)

def getdealid(payload):
  properties = payload.get('properties')
  df = pd.DataFrame.from_dict(properties)
  df = pd.DataFrame.transpose(df)
  deal_id = df.loc["hs_object_id", "value"]
  return deal_id

@app.route('/webhook', methods=['POST'])
def webhook ():
  if request.method == 'POST':
    data = request.json
    print(getdealid(data))
    return Response(status=200)
  else:
    return Response(status=400)

if __name__ == '__main__':
  app.run()
