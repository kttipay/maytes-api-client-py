# CheckoutCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_uuid** | **str** |  | 
**status** | **str** |  | 
**checkout_url** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from maytes_api_client.models.checkout_created import CheckoutCreated

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutCreated from a JSON string
checkout_created_instance = CheckoutCreated.from_json(json)
# print the JSON string representation of the object
print(CheckoutCreated.to_json())

# convert the object into a dict
checkout_created_dict = checkout_created_instance.to_dict()
# create an instance of CheckoutCreated from a dict
checkout_created_from_dict = CheckoutCreated.from_dict(checkout_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


