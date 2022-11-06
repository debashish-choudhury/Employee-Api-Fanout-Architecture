import json
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def processor_data(event, data):
  try:
    messages_to_reprocess = []
    batch_failure_response = {}
    # jsondata = json.loads(event['Records'][0]['body'])
    # LOGGER.info(jsondata['Message'])
    for record in event["Records"]:
      try:
        body = json.loads(record['body'])
        # process message
        LOGGER.info(body)
      except Exception as e:
        messages_to_reprocess.append({'itemIdentifier': record['messageId']})
        batch_failure_response['batchItemFailures'] = messages_to_reprocess
    
  except Exception as error:
    LOGGER.error("Exception %s", error)