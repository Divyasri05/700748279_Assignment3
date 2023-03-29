import boto3
import sqs_module

prefix = 'sqs-usage-demo-'
river_queue = sqs_module.create_queue(
        prefix + 'peculiar-river',
        {
            'MaximumMessageSize': str(1024),
            'ReceiveMessageWaitTimeSeconds': str(20)
        }
    )
print(f"Created queue with URL: {river_queue.url}.")

sqs_module.send_message(river_queue.url)
sqs_module.receive_message (river_queue.url)


queues = sqs_module.get_queues(prefix=prefix)
for queue in queues:
        print(f"Removing queue with URL: {queue.url}.")
        sqs_module.remove_queue(queue)