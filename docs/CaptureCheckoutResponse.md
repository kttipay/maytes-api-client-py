# CaptureCheckoutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CheckoutCaptured**](CheckoutCaptured.md) |  | 

## Example

```python
from maytes_api_client.models.capture_checkout_response import CaptureCheckoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureCheckoutResponse from a JSON string
capture_checkout_response_instance = CaptureCheckoutResponse.from_json(json)
# print the JSON string representation of the object
print(CaptureCheckoutResponse.to_json())

# convert the object into a dict
capture_checkout_response_dict = capture_checkout_response_instance.to_dict()
# create an instance of CaptureCheckoutResponse from a dict
capture_checkout_response_from_dict = CaptureCheckoutResponse.from_dict(capture_checkout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


