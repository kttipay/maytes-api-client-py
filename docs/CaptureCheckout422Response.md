# CaptureCheckout422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**error** | **str** |  | 
**code** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from maytes_api_client.models.capture_checkout422_response import CaptureCheckout422Response

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureCheckout422Response from a JSON string
capture_checkout422_response_instance = CaptureCheckout422Response.from_json(json)
# print the JSON string representation of the object
print(CaptureCheckout422Response.to_json())

# convert the object into a dict
capture_checkout422_response_dict = capture_checkout422_response_instance.to_dict()
# create an instance of CaptureCheckout422Response from a dict
capture_checkout422_response_from_dict = CaptureCheckout422Response.from_dict(capture_checkout422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


