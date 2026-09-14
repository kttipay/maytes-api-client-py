# CaptureCheckout409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**error** | **str** |  | 
**code** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from maytes_api_client.models.capture_checkout409_response import CaptureCheckout409Response

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureCheckout409Response from a JSON string
capture_checkout409_response_instance = CaptureCheckout409Response.from_json(json)
# print the JSON string representation of the object
print(CaptureCheckout409Response.to_json())

# convert the object into a dict
capture_checkout409_response_dict = capture_checkout409_response_instance.to_dict()
# create an instance of CaptureCheckout409Response from a dict
capture_checkout409_response_from_dict = CaptureCheckout409Response.from_dict(capture_checkout409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


