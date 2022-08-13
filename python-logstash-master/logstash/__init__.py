
from logstash.formatter import LogstashFormatterVersion0, LogstashFormatterVersion1

from logstash.handler_tcp import TCPLogstashHandler
from logstash.handler_udp import UDPLogstashHandler, LogstashHandler
print("Q1114144114411")
try:
    from logstash.handler_amqp import AMQPLogstashHandler
except:
   # you need to install AMQP support to enable this handler.
   pass
 


