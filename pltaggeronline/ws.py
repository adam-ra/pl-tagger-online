import requests
import time

nlp_url = 'http://ws.clarin-pl.eu/nlprest2/base/'

tool_tagger = 'wcrft2'

status_error = 'ERROR'
status_done = 'DONE'
status_waiting = 'QUEUE'
status_processing = 'PROCESSING'

query_delay_secs = 0.1


def upload(text):
    """Upload given text and return file_id."""
    resp = requests.post(nlp_url + 'upload',
                         data=text.encode('utf-8'),
                         #headers={'Content-Type': 'binary/octet-stream'}
                         headers={'Content-type': 'text/plain; charset=utf-8'})
    resp.raise_for_status()
    return resp.text


def start_task(file_id, tool_name):
    """Start task for an uploaded file using given tool."""
    resp = requests.post(nlp_url + 'startTask',
                       json={'file': file_id, 'tool': tool_name})
    resp.raise_for_status()
    return resp.text


def check_status(task_id):
    """Check status of given processing task."""
    resp = requests.get(nlp_url + 'getStatus/' + task_id)
    resp.raise_for_status()
    return resp.json()


def wait_until_done(task_id):
    """Wait until task is done. If an error is encountered, will raise IOError.
    If succeeded, will return file_id of the task output."""
    while True:
        time.sleep(query_delay_secs)
        status_struct = check_status(task_id)
        status_value = status_struct['status']
        if status_value == status_done:
            records = status_struct['value']
            if len(records) != 1:
                raise IOError('Unexpected tool status: {}'.format(status_struct))
            return records[0]['fileID']
        if status_value == status_error:
            raise IOError('Tool returned error when processing text')
        if status_value not in [status_processing, status_waiting]:
            raise IOError('Unexpected tool status: {}'.format(status_value))


def read_output(file_id):
    """Download a processed output from the server."""
    resp = requests.get(nlp_url + 'download' + file_id)
    resp.raise_for_status()
    return resp.text


def process(text, tool_name=tool_tagger):
    """Process the given text and return the output CCL (XML) content."""
    file_id = upload(text)
    task_id = start_task(file_id, tool_name)
    result_file_id = wait_until_done(task_id)
    return read_output(result_file_id)
