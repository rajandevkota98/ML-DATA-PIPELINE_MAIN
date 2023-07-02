
import os


SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
API_KEY = 'AO4ZGULX45EM4RMZ' # os.getenv('API_KEY',None)
ENDPOINT_SCHEMA_URL  ='https://psrc-10wgj.ap-southeast-2.aws.confluent.cloud'    #os.getenv'#('ENDPOINT_SCHEMA_URL',None)
API_SECRET_KEY = '5Li9/NagVSN3aXwdrU6jH/OyWC1t8nAvZqug8JHVNFFY5CpmDzKzXrw27jBTd3yy' #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = 'pkc-41p56.asia-south1.gcp.confluent.cloud:9092'#os.getenv('BOOTSTRAP_SERVER',None)
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SCHEMA_REGISTRY_API_KEY = 'M7GNR72HUC4CAALX'#os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET ='ARq9GIqWMkF0heT+os0517bhtpSU1YrYShL2gf9nl3cS6eeUfx+GxhNKKcqRYBDG' #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

