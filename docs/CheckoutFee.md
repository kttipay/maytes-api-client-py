# CheckoutFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**fee_type** | **str** |  | [optional] 
**scope** | **str** |  | 
**amount** | **int** |  | 
**currency** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**applies_to** | **List[str]** |  | [optional] 

## Example

```python
from maytes_api_client.models.checkout_fee import CheckoutFee

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutFee from a JSON string
checkout_fee_instance = CheckoutFee.from_json(json)
# print the JSON string representation of the object
print(CheckoutFee.to_json())

# convert the object into a dict
checkout_fee_dict = checkout_fee_instance.to_dict()
# create an instance of CheckoutFee from a dict
checkout_fee_from_dict = CheckoutFee.from_dict(checkout_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


