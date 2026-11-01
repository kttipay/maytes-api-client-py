# CheckoutFriendItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ref** | **str** |  | 
**quantity** | **int** | How many units of this line this friend pays for. Omit for the whole line. | [optional] 

## Example

```python
from maytes_api_client.models.checkout_friend_item import CheckoutFriendItem

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutFriendItem from a JSON string
checkout_friend_item_instance = CheckoutFriendItem.from_json(json)
# print the JSON string representation of the object
print(CheckoutFriendItem.to_json())

# convert the object into a dict
checkout_friend_item_dict = checkout_friend_item_instance.to_dict()
# create an instance of CheckoutFriendItem from a dict
checkout_friend_item_from_dict = CheckoutFriendItem.from_dict(checkout_friend_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


