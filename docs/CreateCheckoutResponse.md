# CreateCheckoutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CheckoutCreated**](CheckoutCreated.md) |  | 

## Example

```python
from maytes_api_client.models.create_checkout_response import CreateCheckoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCheckoutResponse from a JSON string
create_checkout_response_instance = CreateCheckoutResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCheckoutResponse.to_json())

# convert the object into a dict
create_checkout_response_dict = create_checkout_response_instance.to_dict()
# create an instance of CreateCheckoutResponse from a dict
create_checkout_response_from_dict = CreateCheckoutResponse.from_dict(create_checkout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


