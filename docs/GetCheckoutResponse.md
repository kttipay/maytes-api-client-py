# GetCheckoutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Checkout**](Checkout.md) |  | 

## Example

```python
from maytes_api_client.models.get_checkout_response import GetCheckoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCheckoutResponse from a JSON string
get_checkout_response_instance = GetCheckoutResponse.from_json(json)
# print the JSON string representation of the object
print(GetCheckoutResponse.to_json())

# convert the object into a dict
get_checkout_response_dict = get_checkout_response_instance.to_dict()
# create an instance of GetCheckoutResponse from a dict
get_checkout_response_from_dict = GetCheckoutResponse.from_dict(get_checkout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


