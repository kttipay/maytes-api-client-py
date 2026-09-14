# CaptureCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_order_id** | **str** |  | [optional] 
**expected_total_amount** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from maytes_api_client.models.capture_checkout_request import CaptureCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureCheckoutRequest from a JSON string
capture_checkout_request_instance = CaptureCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(CaptureCheckoutRequest.to_json())

# convert the object into a dict
capture_checkout_request_dict = capture_checkout_request_instance.to_dict()
# create an instance of CaptureCheckoutRequest from a dict
capture_checkout_request_from_dict = CaptureCheckoutRequest.from_dict(capture_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


