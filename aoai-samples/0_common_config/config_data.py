import openai

def set_environment_details_turbo():
    openai.api_key = 'f9f6178d2045490eb5dc707d1889c1f6'
    openai.api_base =  'https://aoai-975.openai.azure.com/' # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
    openai.api_type = 'azure'
    openai.api_version = '2023-07-01-preview'
    print('set the environment details for azure open ai')


def get_environment_details_turbo():
    return 'f9f6178d2045490eb5dc707d1889c1f6', 'https://aoai-975.openai.azure.com/', 'azure', '2023-07-01-preview'

def get_deployment_name_turbo():
    return 'turbo0613'


def set_environment_details_gpt4():
    openai.api_key = 'e4c6d4474b294e2fa31e1deb2fd298b6'
    openai.api_base =  'https://oaisvcsansri.openai.azure.com/'
    openai.api_type = 'azure'
    openai.api_version = '2023-07-01-preview'
    print('set the environment details for azure open ai')
    

def get_deployment_name_turbo():
    return 'turbo0613'

def get_deployment_name_gpt4_32k():
    return 'gpt-4-32k'

def get_lakehouse_connection_details():
    return 'mtcinsightswks-ondemand.sql.azuresynapse.net','sample_ext_db','sqladminuser','MyMtcPass$197'