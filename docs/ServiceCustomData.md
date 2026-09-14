# ServiceCustomData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_type** | **str** |  | [optional] 

## Example

```python
from maytes_api_client.models.service_custom_data import ServiceCustomData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCustomData from a JSON string
service_custom_data_instance = ServiceCustomData.from_json(json)
# print the JSON string representation of the object
print(ServiceCustomData.to_json())

# convert the object into a dict
service_custom_data_dict = service_custom_data_instance.to_dict()
# create an instance of ServiceCustomData from a dict
service_custom_data_from_dict = ServiceCustomData.from_dict(service_custom_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


