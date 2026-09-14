# CancelCheckoutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CheckoutCancelled**](CheckoutCancelled.md) |  | 

## Example

```python
from maytes_api_client.models.cancel_checkout_response import CancelCheckoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelCheckoutResponse from a JSON string
cancel_checkout_response_instance = CancelCheckoutResponse.from_json(json)
# print the JSON string representation of the object
print(CancelCheckoutResponse.to_json())

# convert the object into a dict
cancel_checkout_response_dict = cancel_checkout_response_instance.to_dict()
# create an instance of CancelCheckoutResponse from a dict
cancel_checkout_response_from_dict = CancelCheckoutResponse.from_dict(cancel_checkout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


