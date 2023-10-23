import openai

def set_environment_details_turbo():
    openai.api_key = "xxxxxxxxxxxxxxxxxxx"
    openai.api_base = "https://xxxxxxxxx.openai.azure.com/"  # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
    openai.api_type = "azure"
    openai.api_version = "2023-07-01-preview"
    print("set the environment details for azure open ai")

def get_environment_details_turbo():
    return (
        "xxxxxxxxxxxxxxxxxxxxx",
        "https://xxxxxxxxxxx.openai.azure.com/",
        "azure",
        "2023-07-01-preview",
    )

def get_deployment_name_turbo():
    return "turbo0613"

def set_environment_details_gpt4():
    openai.api_key = "xxxxxxxxxxxxxxxxxx"
    openai.api_base = "https://xxxxxxxx.openai.azure.com/"
    openai.api_type = "azure"
    openai.api_version = "2023-07-01-preview"
    print("set the environment details for azure open ai")

def get_deployment_name_turbo():
    return "turbo0613"

def get_deployment_name_gpt4_32k():
    return "gpt-4-32k"

def get_lakehouse_connection_details():
    return (
        "xxxxxxxxxx-ondemand.sql.azuresynapse.net",
        "sample_ext_db",
        "xxxxxxxxxx",
        "xxxxxxxxxxx",
    )
