# CheckoutCancelled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_uuid** | **str** |  | 
**merchant_order_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from maytes_api_client.models.checkout_cancelled import CheckoutCancelled

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutCancelled from a JSON string
checkout_cancelled_instance = CheckoutCancelled.from_json(json)
# print the JSON string representation of the object
print(CheckoutCancelled.to_json())

# convert the object into a dict
checkout_cancelled_dict = checkout_cancelled_instance.to_dict()
# create an instance of CheckoutCancelled from a dict
checkout_cancelled_from_dict = CheckoutCancelled.from_dict(checkout_cancelled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


